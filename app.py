import os
import re
import glob
import json
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
    if not message:
        return Response('data: {"type":"error","content":"Leere Anfrage"}\n\n',
                        mimetype='text/event-stream')

    client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

    def generate():
        try:
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
                        yield f"data: {json.dumps({'type': 'thinking', 'content': event.thinking})}\n\n"
                    elif event.type == "text":
                        full_text += event.text
                        yield f"data: {json.dumps({'type': 'text', 'content': event.text})}\n\n"
            sources = extract_sources(full_text)
            yield f"data: {json.dumps({'type': 'sources', 'content': sources})}\n\n"
            yield f"data: {json.dumps({'type': 'done'})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
    )


if __name__ == '__main__':
    app.run(debug=False, port=5001)
