import os
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
- Am Ende jeder Antwort: "**Quellen:** [Liste der genutzten Dokumente]"
- Wenn eine Freigabe laut DoA nötig ist, das explizit kennzeichnen mit ⚠️
- Konflikte zwischen Dokumenten fett markieren mit 🚨
- Strukturiert antworten: Überschriften, Tabellen, Aufzählungen — kein reiner Fließtext
- Auf Deutsch antworten"""


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

    docs = load_knowledge_base()
    context = build_context(docs)
    client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

    def generate():
        try:
            with client.messages.stream(
                model="claude-opus-4-7",
                max_tokens=4000,
                thinking={"type": "adaptive"},
                system=SYSTEM_PROMPT,
                messages=[{
                    "role": "user",
                    "content": f"WISSENSBASIS HARTMANN ANTRIEBSTECHNIK:\n\n{context}\n\n---\n\nANFRAGE: {message}"
                }]
            ) as stream:
                for text in stream.text_stream:
                    yield f"data: {json.dumps({'type': 'text', 'content': text})}\n\n"
            yield f"data: {json.dumps({'type': 'done'})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
    )


if __name__ == '__main__':
    app.run(debug=True, port=5001)
