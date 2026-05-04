# Revenue Second Brain — Demo

Interaktive Demo des Revenue Second Brain Konzepts. Fiktives Unternehmen: **Hartmann Antriebstechnik GmbH** (720 MA, €95M Umsatz, DACH-Mittelstand, Antriebstechnik).

Zeigt wie Claude Opus 4.7 über 15 vernetzte Unternehmensdokumente aus dem GTM-Bereich reasont — nicht nur Q&A, sondern Execution: RFP-Antworten, Meeting-Briefings, Pricing-Entscheidungen, Konflikt-Detektion.

---

## Schnellstart

```bash
git clone https://github.com/rm-square/demo.git
cd demo
pip install -r requirements.txt
python3 app.py
```

Dann öffnen:
- **http://localhost:5001** — Chat-Interface mit Claude
- **http://localhost:5001/graph** — Interaktiver Wissensgraph

### Auth-Modi (auto-detect)

Die App wählt beim Start automatisch eine von zwei Engines:

| Modus | Trigger | Wann nutzen |
|---|---|---|
| **API** | `ANTHROPIC_API_KEY` ist gesetzt | Produktionsähnlich, pay-per-token. Voll: Prompt-Caching (`cache_control`), Adaptive Thinking, Reasoning-Trace im UI. |
| **Subscription** | kein API-Key → fällt auf lokale `claude` CLI zurück | Demo-Tests gegen die Pro/Max-Subscription, ohne API-Kosten. Voraussetzung: `claude` CLI installiert + einmal `claude /login`. Caching macht der CLI automatisch (1h-TTL). Thinking-Events werden im Subscription-Modus aktuell nicht über die CLI durchgereicht — die Reasoning-Trace-Box bleibt dann leer (alle anderen Features arbeiten normal). |

Welche Engine aktiv ist, zeigt das Badge in der Topbar (`API` / `Subscription`) sobald die erste Antwort ankommt; beim Start steht es im Server-Log:

```
[demo] auth engine: cli  (claude CLI / Subscription)
```

---

## Was drin ist

### Wissensbasis (15 Dokumente)

| Bereich | Inhalt |
|---|---|
| Firmenprofil | Org-Chart, ICP, 720 MA, €95M Umsatz |
| Messen & Events | 7 Messen 2025, Hannover läuft, €380K Budget |
| Produktportfolio | PrecisionDrive + ServoDrive X + CareConnect, 16 Varianten |
| Roadmap 2025/26 | Releases Q2–Q4, 5 bekannte Limitierungen, EOL |
| Preisliste 2025 | Listenpreise, 4 Rabattstufen (0–18%) |
| Deal Desk | Angebotsprozess, DB-Grenzen, 72 offene Deals |
| Quota & Pipeline | €98M Ziel, 3 AEs unter Plan, Brenner €740K Hauptdeal |
| Delegation of Authority | Rabatt- + Zahlungsziel-Freigabestufen |
| Vertragsklauseln | Lieferung, Haftung, DSGVO/AVV |
| Sales Plays | 3 Plays: New Logo, Expansion, Competitive Displacement |
| Battle Cards | vs. SEW-Eurodrive, vs. Siemens, vs. Bonfiglioli |
| Lead Management | MQL/SQL-Definitionen, 38% SLA-Verstoß, 3 Kampagnen |
| Kundenaccounts | 5 Accounts mit Deal-Historien + Signalen |
| CS Dashboard Q1/25 | 3 Eskalationen, NPS 52, 23 Renewals Q2/Q3 |
| RFP Brenner Bratislava | €740K RFQ, Frist 23. Mai, Siemens Wettbewerber |

### Wissensgraph (`/graph`)

D3.js Force-Graph mit ~70 Nodes und 130+ Links. Zeigt die Vernetzung des Second Brains:
- Klick auf Node → Detail-Panel rechts + alle verbundenen Nodes highlighten
- Rote Kanten = Konflikte (hover für Beschreibung)
- Expand/Collapse für jede Dokumentebene

### Eingebettete Konflikte

Die Demo enthält absichtlich Spannungen die nur durch Verknüpfung mehrerer Dokumente sichtbar werden:

- 🚨 AE geht in QBR Müller (15. Mai) ohne Wissen über offene CS-Eskalation
- 🚨 Brenner RFQ fordert 8h SLA Bratislava — intern aktuell nur 2 Techniker (48h realistisch)
- 🚨 SDX-22 TwinBus wird am Hannover-Messe-Stand gezeigt — Felderprobung läuft noch
- 🚨 Brenner RFQ: 60T + kein Anzahlung = CRO+CFO Pflicht, AE hat keine Kompetenz
- 🚨 Bergmann Inbound €41K liegt unbearbeitet — AE in Elternzeit

---

## Demo-Szenarien

Drei vordefinierte Szenen im Chat-Sidebar, oder direkt eingeben:

**Vorgebaut:**
- RFP-Antwort auf Brenner Bratislava (€740K, vs. Siemens)
- Kundentermin-Briefing Müller QBR 15. Mai
- Pricing-Empfehlung Brenner mit DoA-Freigaben

**Weitere gute Fragen:**
- "Welche Deals laufen gerade und wo ist das größte Risiko?"
- "Was passiert wenn Brenner absagt — wie sieht unser Forecast dann aus?"
- "Welche Kunden könnten zu SEW wechseln und warum?"
- "Was brauche ich für den Abschluss des Brenner-Deals — welche Freigaben, welche Personen?"

---

## Architektur

```
EXECUTION LAYER    →  Claude-generierte Dokumente, Briefings, Analysen
INTELLIGENCE LAYER →  Claude Opus 4.7 + Adaptive Thinking (Anthropic API)
KNOWLEDGE LAYER    →  15 Markdown-Dokumente (= das "Second Brain")
```

In der echten Unternehmens-IT: n8n für Ingestion/Sync, DSGVO-konforme EU-Architektur, Kundendaten in kundenkontrollierter Storage.

---

## Stack

- Python 3 + Flask (SSE-Streaming)
- [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-python) + Claude Opus 4.7
- D3.js v7 (Wissensgraph)
- Kein externes Frontend-Framework
