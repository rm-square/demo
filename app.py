import os
import re
import glob
import json
import shutil
import subprocess
import anthropic
from flask import Flask, render_template, request, Response, stream_with_context

app = Flask(__name__)

HARTMANN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hartmann')

SYSTEM_PROMPT = """Du bist der Revenue Intelligence Assistant von Hartmann Antriebstechnik GmbH.

Du hast Zugriff auf alle internen Dokumente: Produktinformationen, Preislisten, Vertragsklauseln, Delegation of Authority, Sales Plays, Battle Cards, Kundenaccounts, CS-Eskalationen, Marketing-Daten und Pipeline.

Du beantwortest nicht nur Fragen — du lieferst konkrete Execution:
- Dokumente erstellen: RFP-Antworten, Briefings, Analysen
- Entscheidungen vorbereiten: Pricing, Freigaben, Verhandlungsposition
- Konflikte aufzeigen: wenn eine Information aus Dokument A mit einer Anforderung aus Dokument B kollidiert
- Externe Dokumente analysieren: wenn der Nutzer ein "EXTERNES DOKUMENT" mitschickt, dieses gegen die interne Wissensbasis halten und Konflikte/Risiken identifizieren

Regeln:
- Immer konkrete Zahlen und Fakten aus den Dokumenten nennen
- Wenn eine Freigabe laut DoA nötig ist, das explizit kennzeichnen mit ⚠️
- Konflikte zwischen Dokumenten fett markieren mit 🚨
- Strukturiert antworten: Überschriften, Tabellen, Aufzählungen — kein reiner Fließtext
- Auf Deutsch antworten

QUELLEN-FORMAT (verbindlich, immer als allerletzte Zeile der Antwort):
**Quellen:** pfad/dokument-1, pfad/dokument-2, pfad/dokument-3

- Nutze die exakten Pfade wie sie in den `=== DOKUMENT: ... ===`-Headern stehen, ohne `.md`-Endung
- Komma-separiert in EINER Zeile, kein Bullet, keine zusätzliche Formatierung
- Nur tatsächlich für die Antwort verwendete Dokumente listen"""


def load_knowledge_base():
    docs = {}
    pattern = os.path.join(HARTMANN_DIR, '**', '*.md')
    for path in sorted(glob.glob(pattern, recursive=True)):
        filename = os.path.basename(path)
        if filename.startswith('_'):
            continue  # skip archived/external files
        rel = os.path.relpath(path, HARTMANN_DIR)
        with open(path, encoding='utf-8') as f:
            docs[rel] = f.read()
    return docs


def build_context(docs):
    parts = []
    for name, content in docs.items():
        parts.append(f"=== DOKUMENT: {name} ===\n{content}")
    return "\n\n".join(parts)


KNOWLEDGE_BASE = build_context(load_knowledge_base())
KNOWN_SOURCES = {os.path.splitext(p)[0] for p in load_knowledge_base().keys()}

SOURCES_LINE = re.compile(r'\*\*Quellen:\*\*\s*(.+?)\s*$', re.MULTILINE)


def extract_sources(text: str) -> list[str]:
    """Parse the trailing **Quellen:** line and match against known doc paths."""
    matches = SOURCES_LINE.findall(text)
    if not matches:
        return []
    raw = matches[-1]
    candidates = [c.strip().strip('`').rstrip('.,;').replace('.md', '')
                  for c in raw.split(',')]
    return [c for c in candidates if c in KNOWN_SOURCES]


FULL_SYSTEM_PROMPT = (
    f"{SYSTEM_PROMPT}\n\n"
    f"WISSENSBASIS HARTMANN ANTRIEBSTECHNIK:\n\n{KNOWLEDGE_BASE}"
)


# ─── Engine: Anthropic API (pay-per-token, native cache_control + adaptive thinking) ──
def stream_via_api(message):
    """Yields ('thinking'|'text', delta) and finally ('full', accumulated_text)."""
    client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])
    full_text = ""
    with client.messages.stream(
        model="claude-opus-4-7",
        max_tokens=4000,
        thinking={"type": "adaptive"},
        system=[
            {"type": "text", "text": SYSTEM_PROMPT},
            {
                "type": "text",
                "text": f"WISSENSBASIS HARTMANN ANTRIEBSTECHNIK:\n\n{KNOWLEDGE_BASE}",
                "cache_control": {"type": "ephemeral"}
            }
        ],
        messages=[{"role": "user", "content": message}]
    ) as stream:
        for event in stream:
            if event.type == "thinking":
                yield ("thinking", event.thinking)
            elif event.type == "text":
                full_text += event.text
                yield ("text", event.text)
    yield ("full", full_text)


# ─── Engine: claude CLI subprocess (uses Pro/Max subscription via OAuth, no API key) ──
def stream_via_cli(message):
    """Yields ('thinking'|'text', delta) and finally ('full', accumulated_text).

    Uses the locally-installed `claude` CLI in --print mode. Auth flows through whatever
    the CLI is logged into (Subscription via keychain OAuth on macOS). The output format
    `stream-json --include-partial-messages` emits raw Anthropic stream events under the
    `event` key, including `thinking_delta` and `text_delta` content_block_deltas.
    """
    cli = shutil.which("claude")
    if not cli:
        raise RuntimeError(
            "claude CLI not found in PATH. Install Claude Code and run `claude /login`, "
            "or set ANTHROPIC_API_KEY to use the API engine."
        )

    cmd = [
        cli, "-p",
        "--verbose",  # required by --output-format=stream-json
        "--model", "claude-opus-4-7",
        "--effort", "high",
        "--output-format", "stream-json",
        "--include-partial-messages",
        "--no-session-persistence",
        "--disable-slash-commands",
        "--system-prompt", FULL_SYSTEM_PROMPT,
        message,
    ]

    # Force OAuth/Subscription path: drop any inherited ANTHROPIC_API_KEY
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}

    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, bufsize=1, env=env,
    )

    full_text = ""
    try:
        for line in proc.stdout:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            if obj.get("type") == "stream_event":
                evt = obj.get("event", {})
                if evt.get("type") == "content_block_delta":
                    delta = evt.get("delta", {})
                    dtype = delta.get("type")
                    if dtype == "thinking_delta":
                        chunk = delta.get("thinking", "")
                        if chunk:
                            yield ("thinking", chunk)
                    elif dtype == "text_delta":
                        chunk = delta.get("text", "")
                        if chunk:
                            full_text += chunk
                            yield ("text", chunk)
            elif obj.get("type") == "result" and obj.get("is_error"):
                err = obj.get("result") or "claude CLI returned an error"
                raise RuntimeError(err)
    finally:
        proc.wait(timeout=30)
        if proc.returncode not in (0, None):
            stderr = proc.stderr.read() if proc.stderr else ""
            if not full_text:
                raise RuntimeError(f"claude CLI exited {proc.returncode}: {stderr.strip()[:400]}")

    yield ("full", full_text)


def select_engine():
    """Choose engine. API key wins if present, otherwise fall back to CLI/Subscription."""
    if os.environ.get('ANTHROPIC_API_KEY'):
        return stream_via_api, "api"
    return stream_via_cli, "cli"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    body = request.get_json()
    message = body.get('message', '').strip()
    attached_doc = body.get('attached_doc', '').strip()
    if not message:
        return Response('data: {"type":"error","content":"Leere Anfrage"}\n\n',
                        mimetype='text/event-stream')

    if attached_doc:
        full_message = f"EXTERNES DOKUMENT (vom Kunden / von außen eingereicht):\n\n{attached_doc}\n\n---\n\nANFRAGE: {message}"
    else:
        full_message = message

    engine_fn, engine_name = select_engine()

    def generate():
        try:
            yield f"data: {json.dumps({'type': 'engine', 'content': engine_name})}\n\n"
            full_text = ""
            for kind, payload in engine_fn(full_message):
                if kind == "full":
                    full_text = payload
                else:
                    yield f"data: {json.dumps({'type': kind, 'content': payload})}\n\n"
            yield f"data: {json.dumps({'type': 'sources', 'content': extract_sources(full_text)})}\n\n"
            yield f"data: {json.dumps({'type': 'done'})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
    )


if __name__ == '__main__':
    _, engine_name = select_engine()
    print(f"[demo] auth engine: {engine_name}  ({'API key' if engine_name == 'api' else 'claude CLI / Subscription'})")
    app.run(debug=False, port=5001)
