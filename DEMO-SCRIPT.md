# Demo Script — Revenue Second Brain (Hartmann Antriebstechnik)

**Setup:** `cd ~/rm-square/demo && python3 app.py` → http://localhost:5001

Der Brain enthält 21 interne Hartmann-Dokumente (Produkte, Preise, Kunden, Pipeline, DoA, Battle Cards, HR, CRM-Log usw.). Externe Dokumente kommen via 📎-Button in den Chat — sie werden **nicht** in den Brain gespeichert, sondern live gegen den Brain gehalten.

---

## Szenario 1 — RFQ Analyse: Brenner Bratislava (€740K)

**Was es zeigt:** Das Kernprodukt-Szenario. Ein externes Einkaufsdokument trifft auf interne Wissensbasis — Claude findet Konflikte die kein Mensch in 5 Minuten findet.

### Schritt 1: RFQ einfügen
1. Klick auf **📎** (Büroklammer, links neben dem Eingabefeld)
2. Öffne `~/rm-square/demo/hartmann/customers/REQUEST FOR QUOTATION.docx` in Word oder TextEdit
3. Alles markieren (`Cmd+A`) und in den grauen Dokumentbereich einfügen

### Schritt 2: Frage eingeben
```
Ich habe gerade diesen RFQ erhalten. Analysiere ihn:
Welche Anforderungen können wir erfüllen, welche nicht?
Wo gibt es Konflikte mit unseren internen Daten (DoA, SLA, Roadmap)?
Was muss ich vor der Antwort klären?
```

### Was du siehst
- **🚨 SLA-Konflikt:** RFQ fordert 8h Reaktionszeit Bratislava — unser Standard-CareConnect hat 8h nur für DACH. Bratislava (Ausland) ist im Contract nicht gedeckt → braucht Custom-Klausel + Freigabe
- **🚨 Feldbuskonflikt:** EtherCAT UND PROFINET gleichzeitig — SDX-22 SI unterstützt PROFINET nativ, EtherCAT nur mit TwinBus-Gateway (Zusatzkosten ~€8K, Lieferzeit +4 Wochen)
- **⚠️ DoA-Grenze:** Deal-Volumen €740K → AE darf max. 12% Rabatt eigenständig. Alles darüber = RD-Freigabe notwendig
- **Preis-Rechnung:** 60×SDX-22 SI + 30×PD-3000 + CareConnect-36M → Listenpreis ~€810K, Zielpreis für Win ~€695–740K
- Quellen-Highlights links: Preisliste, DoA, Service-SLA, Produktblatt SDX-22, Battle Card

---

## Szenario 2 — Terminvorbereitung: QBR Müller Maschinenbau

**Was es zeigt:** Cross-Document-Intelligenz über Kunden-Account hinweg — Eskalationen, Gesprächspartner-Profil, offene Risiken, Verhandlungsposition, alles in einem Zug.

### Prompt (direkt eingeben, kein Dokument nötig)
```
Ich habe in 20 Minuten den QBR-Termin bei Müller Maschinenbau in Ingolstadt.
Mein Gesprächspartner ist Einkaufsleiter Bernd Koch.

Bereite mich vollständig vor:
1. Was ist der aktuelle Status des Accounts — was läuft gut, was nicht?
2. Was weiß ich über Bernd Koch und wie er verhandelt?
3. Gibt es offene Probleme oder Eskalationen die er ansprechen wird — und wie antworte ich darauf?
4. Was ist mein Ziel für diesen Termin und wie argumentiere ich es?
5. Was darf ich ihm versprechen — und was nicht (Produkte, Preise, Konditionen)?
6. Was ist meine Verhandlungsstrategie für die CC-Renewal?
```

### Was du siehst
- **Bernd Koch-Profil:** Fordert immer schriftliche Bestätigungen, hat letzte Preiserhöhung 6 Monate verzögert, bevorzugt TCO-Argumente
- **🚨 Offene Eskalation:** CS-Ticket #4471 (Wartungsintervall-Streit) noch nicht geschlossen — er wird das ansprechen
- **⚠️ CareConnect Alert:** 3 Anomalie-Warnungen im Werk Ingolstadt letzte 30 Tage — proaktiv ansprechen statt warten
- **Upgrade-Opportunity:** CC-Basic → CC-Premium würde Anomalie-Monitoring automatisieren, passt zu seinem Risiko-Profil
- **Renewal-Fenster:** Läuft in 4 Monaten aus, Standarderhöhung 4% — er kennt den Markt, Siemens hat ihm Angebot gemacht
- Quellen: Müller-Account, CS-Eskalationen, CareConnect-Nutzung, Preisliste

---

## Szenario 3 — Pricing-Empfehlung: Siemens-Wettbewerb

**Was es zeigt:** Komplexe Pricing-Entscheidung mit DoA-Gate-Erkennung — was der AE selbst entscheiden darf vs. was eskaliert werden muss.

### Prompt
```
Wir sind im Wettbewerb mit Siemens um den Brenner Bratislava Deal (€740K Volumen, 90 Komponenten).

Gib mir eine konkrete Pricing-Empfehlung:
1. Was ist unser kalkulierter Listenpreis für alle drei Positionen (60x SDX-22 SI + 30x PD-3000 + CareConnect 36M)?
2. Welchen Rabatt kann ich eigenständig geben — und welchen erst nach Freigabe?
3. Wie preisen wir gegen Siemens? Wo sind wir günstiger, wo teurer, und wie argumentieren wir den Mehrwert?
4. Gibt es eine "aggressive but defensible" Preisposition die den Deal gewinnt ohne die Marge zu zerstören?
5. Welche Gegenleistung soll ich für jeden Rabattschritt fordern?
```

### Was du siehst
- Listenpreis-Kalkulation pro Position mit Hartmann-Preisblatt-Zahlen
- **⚠️ DoA-Schwelle:** >12% Rabatt (= unter ~€713K) → Regional Director Freigabe. >18% → VP Sales
- **🚨 Battle Card Konflikt:** Siemens bietet SINAMICS S200 an — Battle Card sagt wir gewinnen auf Safety-Integration (SIL2 nativ), verlieren auf Lieferzeit wenn EtherCAT-Gateway nötig
- **Empfehlung:** 8% Eigenrabatt anbieten (€745K), Gegenleistung: 36M CareConnect Premium statt Basic, 3-Jahres-Rahmenvertrag
- Quellen: Preisliste, DoA, Battle Card Siemens, Produktblatt SDX-22

---

## Szenario 4 — Pipeline-Risiken: Was brennt diese Woche?

**Was es zeigt:** Übergreifende Pipeline-Analyse mit Personalrisiko — Claude verbindet HR-Daten mit Deals in der Pipeline.

### Prompt
```
Ich bin Head of Sales. Zeig mir alle aktiven Pipeline-Risiken:
- Welche Deals sind gefährdet und warum?
- Wo gibt es Wettbewerb und wie ist unser Stand?
- Gibt es personelle Risiken die Deals gefährden?
- Was muss ich diese Woche zwingend tun?
```

### Was du siehst
- **🚨 Pieters Manufacturing:** SEW-Eurodrive hat ein Angebot eingereicht, Pieters war 3 Wochen nicht erreichbar — Deal auf Kippe
- **⚠️ HR × Pipeline:** AE Stefan Weber (Owner von 2 großen Deals) hat in der HR-Planung ein Entwicklungsgespräch-Flag — Fluktuationsrisiko sollte proaktiv adressiert werden
- **Renewal-Cluster:** KME und Voigt laufen in Q3 aus, KME hatte CS-Probleme → höheres Churn-Risiko
- Priorisierungsliste mit konkreten nächsten Schritten
- Quellen: Pipeline, Win-Loss, AE-Performance, HR-Planung, CRM-Log

---

## Szenario 5 — Renewal-Risiko: KME Müller

**Was es zeigt:** Customer Success Intelligence — Churn-Signal aus mehreren Datenquellen kombiniert mit Upsell-Argument.

### Prompt
```
KME Müller hat Renewal im nächsten Quartal. Ich glaube der Kunde ist at-risk.
Analysiere: Wie hoch ist das Churn-Risiko und warum?
Was ist unser bestes Argument für die Verlängerung?
Gibt es eine Upsell-Möglichkeit die das Risiko senkt?
Was muss ich konkret tun und bis wann?
```

### Was du siehst
- **Churn-Score 85%:** Drei Warnsignale kombiniert — offenes CS-Ticket ungelöst seit 6 Wochen, CareConnect-Nutzung unter 30% (zahlen für Features die sie nicht nutzen), letzter Kontakt >60 Tage
- **Upsell-Argument:** CC-Premium hat Predictive-Maintenance-Feature das direkt auf ihr offenes Problem einzahlt — Upgrade rechtfertigt Vertragsverlängerung
- **⚠️ DoA:** Retention-Rabatt bis 8% eigenständig möglich; wenn Kombination Rabatt + Upgrade-Preis nötig → RD-Schleife
- Konkrete Aktionsschritte mit Zeitplan
- Quellen: Renewal-Forecast, CareConnect-Nutzung, CS-Eskalationen, Preisliste

---

## Bonus: Externer Vertrag analysieren

Für ein weiteres Live-Szenario: Kopiere irgendeine Vertragsklausel oder AGB-Passage in das 📎-Feld (z.B. eine Lieferbedingung mit ungewöhnlichen Haftungsklauseln) und frage:

```
Analysiere diese Vertragsklausel gegen unsere Standard-AGB und DoA.
Welche Punkte weichen ab? Was darf ich selbst akzeptieren, was braucht Legal?
```

---

## Tipps für die Demo

- **Quellen-Sidebar links** — nach jeder Antwort leuchten die verwendeten Dokumente auf. Zeigt: der Brain weiß welche Dokumente er warum verwendet hat.
- **Engine-Anzeige** — oben im Chatfenster erscheint kurz `api` oder `cli` (je nach Auth-Modus). Kein API-Key gesetzt = läuft über Claude-Subscription.
- **Thinking** — bei komplexen Fragen erscheint kurz ein Denkbereich bevor die Antwort kommt. Das ist adaptive reasoning.
- **Dokumentgröße** — der 📎-Bereich zeigt die Zeichenanzahl. Der RFQ hat ~3.500 Zeichen. Problemlos bis ~100K Zeichen (Verträge, Protokolle, Excel-Exports als CSV).
- **Freitext** — es gibt keine vordefinierten Prompts mehr. Jede Frage in natürlichem Deutsch funktioniert.
