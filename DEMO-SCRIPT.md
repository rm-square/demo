# Demo Script — Revenue Second Brain (Hartmann Antriebstechnik)

**Setup:** `cd ~/rm-square/demo && python3 app.py` → http://localhost:5001

Der Brain enthält 21 interne Hartmann-Dokumente (Produkte, Preise, Kunden, Pipeline, DoA, Battle Cards, HR, CRM-Log usw.). Externe Dokumente kommen via 📎-Button in den Chat — sie werden **nicht** in den Brain gespeichert, sondern live gegen den Brain gehalten.

---

## Szenario 1 — RFQ Analyse: Brenner Bratislava (€740K)

**Was es zeigt:** Das Kernprodukt-Szenario. Ein externes Einkaufsdokument trifft auf interne Wissensbasis — Claude findet Konflikte die kein Mensch in 5 Minuten findet. Und am Ende landet die Analyse dauerhaft im Brain.

### Schritt 1: RFQ hochladen
1. Klick auf **📎** → dann **📁 Datei** und `REQUEST FOR QUOTATION.docx` auswählen
2. Datei wird automatisch eingelesen (kein Copy-Paste nötig)

### Schritt 2: Analyse starten
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

### Schritt 3: Write-Back ins Brain (Flywheel-Moment)
```
Speichere die Kundenanforderungen aus diesem RFQ als Deal-Brief für Brenner Bratislava ins Second Brain.
```

### Was jetzt passiert
- Grüner **💾 Ins Brain speichern**-Button erscheint unter der Antwort
- Klick → neues Dokument `customers/deal-brief-brenner-bratislava-2025` landet im Brain
- Sidebar zeigt neuen Eintrag mit "Neu"-Badge — Brain hat jetzt 25 Dokumente
- **Ab sofort:** Alle weiteren Fragen zu Brenner (Pricing, QBR-Vorbereitung, Angebotsentwurf) ziehen automatisch aus den gespeicherten Anforderungen — ohne den RFP nochmal hochzuladen

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

---

## Szenario 6 — Produkt & Wettbewerb: PrecisionDrive vs. SEW und Siemens

**Was es zeigt:** Produkt-Intelligence mit Roadmap-Check — der Brain verbindet Produktdaten, Battle Cards, Win/Loss-Analyse und Roadmap zu einer ehrlichen Wettbewerbseinschätzung. Zeigt wo Hartmann heute gewinnt, wo verliert, und was auf der Roadmap den Abstand vergrößert oder schließt.

### Prompt
```
Vergleiche unser Produkt PrecisionDrive mit SEW und Siemens und erkläre mir was auf der Roadmap steht. Wie siehst du uns im Wettbewerb mit der gelieferten Roadmap?
```

### Was du siehst
- **Heutiger Vorteil PrecisionDrive:** Spielarme Verzahnung ≤1 Bogenminute (SEW: keine vergleichbare Spezifikation publiziert), Lieferzeit PD-500 3 Wochen vs. SEW 6–8 Wochen, PD-200 Edelstahl (FDA-konform) ohne Siemens-Äquivalent im DACH-Markt
- **Heutiger Nachteil:** DigiLink v1 überträgt nur Temperatur + Betriebsstunden — keine Vibration. SEW MOVI-Plattform hat Vibrationsmessung bereits, Siemens MindSphere ebenfalls
- **Roadmap-Einschätzung:** PD-DigiLink v2.0 (GA Q3/2025) bringt Vibrations-Fingerprint — schließt den IoT-Gap zu SEW direkt. Ab Q4/2025 wird DigiLink Standard in PD-3000 ohne Aufpreis — struktureller Margenvorteil gegenüber SEW (MOVI-Lizenzkosten)
- **🚨 Kritischer Roadmap-Hinweis:** SDX-22 TwinBus ist noch in Felderprobung — nicht als fertig verkaufen. Explizit in Roadmap-Dokument unter Limitierungen dokumentiert
- **Win/Loss-Kontext:** Gegen SEW: 71% Win-Rate, gewinnbar über Lieferzeit + Sonderauslegung. Gegen Siemens: nur 36% — nicht über Preis (nur 1 von 7 Verlusten war Preis), sondern über Wahrnehmung "Siemens ist sicherer"
- **Empfehlung:** Für Siemens-Displacement DigiLink v2.0 als Pilot positionieren ("kommt Q3, Pilot möglich") — das ist der fehlende Beweis für Predictive-Capability
- Quellen: Produktübersicht, Roadmap, Battle Cards, Win/Loss-Analyse

---

## Szenario 7 — CSM: Zeller Fördertechnik proaktiv entwickeln

**Was es zeigt:** Customer Success Intelligence aus mehreren Quellen — CareConnect-Nutzungsdaten, CRM-Log und Renewal-Forecast ergeben zusammen ein Bild, das kein einzelnes Dokument allein zeigen würde. Upgrade-Trigger bereits erfüllt, aber vom Team übersehen.

### Prompt (direkt eingeben, kein Dokument nötig)
```
Ich bin CSM und bereite mich auf ein Gespräch mit Zeller Fördertechnik vor.
Die haben CC-Base und das Renewal steht im August an.
Was soll ich wissen, was soll ich ansprechen, und was ist meine beste Strategie für das Gespräch?
```

### Was du siehst
- **Upgrade-Trigger erfüllt, aber ungenutzt:** 4 ungeplante Serviceeinsätze in 12 Monaten — die interne Kampagne-Regel definiert 3 als Trigger für ein CC-Plus-Upgrade-Gespräch. Niemand hat diesen Prozess ausgelöst
- **Wien-Projekt als natürlicher Einstieg:** 22×PD-1200 + 6×PD-3000, Budget ~€210K, Entscheidung bis Ende Mai. Renewal + Neugeschäft kombinierbar als Paket — Mengenrabatt 10% greift bei >€150K Jahresvolumen
- **⚠️ Churn-Risiko 35%:** Bonfiglioli ist im Wien-Projekt-Gespräch aktiv. Angebot war zum Zeitpunkt des CRM-Logs bereits 2 Wochen überfällig
- **Upsell-Argument:** CC-Plus eliminiert die ungeplanten Einsätze die den Kunden bereits 4× gestört haben — TCO-Rechnung direkt aus den Nutzungsdaten
- Quellen: CareConnect-Nutzungsdaten, CRM-Aktivitäten-Log, Renewal-Forecast, Pipeline-Deals, Preisliste

---

## Szenario 8 — Konflikt-Detektor: Was habe ich dem Kunden versprochen?

**Was es zeigt:** Das System findet Widersprüche zwischen dem was ein AE auf der Messe zugesagt hat und dem was intern freigegeben und technisch möglich ist. Ein externer Text (Gesprächsnotiz) wird gegen drei interne Dokumente gleichzeitig geprüft.

### Schritt 1: Gesprächsnotiz einfügen (📎)
Kopiere folgenden Text in das Dokumentfeld:

```
Gesprächsnotiz Hannover Messe, 07. Mai 2025:
Brenner Automotive (Hoffmann + Müller): Habe bestätigt, dass SDX-22 TwinBus
PROFINET + EtherCAT gleichzeitig unterstützt. Habe außerdem gesagt, Bratislava
8h-SLA ist kein Problem, wir regeln das. Zahlungsziel 60 Tage haben wir "sicher
hinbekommen" zugesagt. Angebot bis 23. Mai.
```

### Schritt 2: Frage eingeben
```
Analysiere diese Gesprächsnotiz. Welche der gemachten Aussagen sind intern gedeckt — und welche nicht?
Was riskieren wir rechtlich und kommerziell, und was muss sofort korrigiert oder eskaliert werden?
```

### Was du siehst
- **🚨 TwinBus-Aussage falsch:** Roadmap explizit: "SDX-22 TwinBus: gleichzeitiger Betrieb PROFINET+EtherCAT in Felderprobung bei 2 Kunden — nicht breit kommunizieren." AE hat das Gegenteil zugesagt
- **🚨 Bratislava-SLA nicht haltbar:** CS-Eskalation #HAT-2025-0341 dokumentiert: 8h Reaktionszeit aktuell nicht leistbar (2 Techniker, realistisch 48h). COO hat Aufbau genehmigt, aber erst Q3/2025 abgeschlossen
- **🚨 Zahlungsziel 60 Tage ohne Freigabe:** DoA eindeutig: 60 Tage = CRO + CFO-Freigabe nötig. Die mündliche Zusage ohne Eskalationspfad ist in deal-desk-prozess.md als Muster-Fehlerfall dokumentiert
- **Empfohlene Aktionen:** KAM Stern vor nächstem Brenner-Kontakt informieren → COO Bratislava-Zeitplan abfragen → CFO-Freigabe beantragen oder Aussage schriftlich zurücknehmen
- Quellen: Roadmap 2025/2026, CS-Dashboard, Messen-Events, Vertragsklauseln, Deal-Desk-Prozess, DoA

---

## Szenario 9 — CMO-Briefing: Budget neu priorisieren nach Hannover

**Was es zeigt:** Marketing kann dem CMO eine datenbasierte Budget-Empfehlung vorlegen — das System erkennt den Widerspruch zwischen gemessenem ROI und geplanter Budgeterhöhung. Zeigt auch den SLA-Gap zwischen Marketing und Vertrieb mit konkreten Namen und Zahlen.

### Prompt (direkt eingeben)
```
Ich bin CMO. Wir haben gerade die Hannover Messe hinter uns und ich muss das Jahresbudget
für Marketing neu priorisieren. Wo soll ich mehr investieren, wo weniger?
Gibt es Probleme an der Marketing-Sales-Schnittstelle die ich angehen muss?
```

### Was du siehst
- **🚨 Budget-Widerspruch:** Events binden 36% des Budgets und liefern nur 21% des attributierten Revenue (CAC €18.400–22.500). Digitale Kanäle: 22% Budget → 78% Revenue (CAC €1.300–4.200). Trotzdem ist Messe-Budget-Erhöhung auf €420K (+10%) geplant
- **Webinar als Hidden Champion:** ROI 27,8x, 79% SQL-zu-Opportunity-Rate, aber nur €12.000 Investition. Signifikant unterinvestiert
- **SLA-Krise:** 28% der SQLs werden nicht in 24h kontaktiert. Hauptverursacher mit Name + Compliance-Rate aus den Daten sichtbar. Action Item "Auto-Reminder HubSpot" seit Februar offen
- **Content-Gaps mit Deal-Impact:** Edelstahl-Broschüre PD-200 fehlt → 4 dokumentierte Deal-Verluste. CC-Premium Case Study fehlt → 6 AEs können Upsell-Gespräch nicht führen
- **Hannover-Echtzeit:** 180 Badge-Scans nach Tag 3, Prognose ~240, erwartete Pipeline €1,2M — besser als 2024, aber 3 Leads wollten TwinBus-GA-Zusagen
- Quellen: Kampagnen-ROI-Attribution, Lead-Management, Leads-Datenbank, Messen-Events, Roadmap

---

## Szenario 10 — Inbound-Notfall: Kunden kontaktieren uns, niemand reagiert

**Was es zeigt:** Das System verbindet einen unbearbeiteten Inbound-Lead mit Personalrisiko-Daten und Deadline-Tracking — und zeigt warum der Lead nicht bearbeitet wurde und was passiert wenn nicht sofort gehandelt wird.

### Prompt (direkt eingeben)
```
Ich bin Regional Manager. Bergmann & Söhne hat uns kontaktiert und will ein Angebot.
Ich glaube da ist was schiefgelaufen. Was ist der Status, was ist das Risiko,
und was muss ich in den nächsten 24 Stunden tun?
```

### Was du siehst
- **🔴 Inbound seit 7 Tagen unbeantwortet:** Bergmann sendete 28. April Anfrage ~€41K (8×PD-500 Edelstahl + SDX-2 + Inbetriebnahme). HubSpot: "E-Mail geöffnet: Nein". Angebotsfrist 15. Mai läuft ab
- **Ursache = Personalrisiko:** Lisa Hofmann (Account Owner) in Elternzeit. Vertretung Martin Engel betreut gleichzeitig seine eigene Quota + Hofmann-Region + steht selbst unter Performance-Watch (41% Win-Rate). Die Doppelbelastung ist im HR-Dokument als direkter Erklärungsfaktor für Engels Underperformance dokumentiert
- **Strategischer Hebel:** Bergmann ist NPS 10, Pharma-Referenzkunde ("PD-200 Edelstahl war entscheidend für unseren Pharmakunden") — verlieren wir den Deal, verlieren wir die Referenz
- **Konkrete Nächste Schritte:** Engel heute ansprechen, Bergmann bis morgen persönlich kontaktieren (nicht über Engel), Angebot: PD-200 Edelstahl €2.340/Stk + CC-Base €4.800 (FDA-Audit-Trail-Argument), Deal in CRM als aktiv anlegen
- Quellen: CRM-Aktivitäten-Log, Kundenaccounts, Kundendatenbank, Personalplanung, Preisliste

---

## Szenario 11 — AE-Coaching: Warum verliert Klaus Schreiber?

**Was es zeigt:** Head of Sales bekommt ein vollständiges Bild eines underperformenden AE — Performance-Zahlen, Pipeline-Pathologie, CRM-Verhalten und HR-Kontext werden verknüpft. Das System stellt eine Coaching-Diagnose die kein einzelnes Report-Tool zeigen würde.

### Prompt (direkt eingeben)
```
Ich habe am 15. Mai das Performance-Review mit Klaus Schreiber (AE Nord).
Er ist seit Monaten unter Quota. Bereite mich vor:
Was zeigen die Daten wirklich? Was ist die Ursache?
Und was schlage ich ihm vor — und was passiert wenn es nicht klappt?
```

### Was du siehst
- **Datenbild:** €145K unter Quota, 39% Win-Rate (Team-Ø ~58%), Sales Cycle 12,3W (Benchmark 7,2W), 9 Aktivitäten/Woche (Benchmark 22), letzter Kundenkontakt 14. April
- **Pipeline-Pathologie:** 4 von 6 Deals seit >8 Wochen ohne Stage-Fortschritt. "Maschinenbau Drescher" (€78K, Stage: Angebot versandt) liegt seit Woche 7 ohne Follow-Up — SEW ist aktiv
- **Verhaltensmuster:** Kein einziger CareConnect-Bundle in Q1 (Team-Benchmark: 40% aller Deals). Höchste Rabatte im Team (Ø 11,8%) — laut Win/Loss-Analyse helfen Rabatte über 10% statistisch nicht (Win-Rate bleibt gleich, Marge sinkt)
- **Vergleich mit Top-Performer:** Zimmermann, gleiche Produktpalette: 74% Win-Rate, 5,8W Cycle, 87% CC-Bundle-Rate. Ihr Playbook ist konkret abrufbar: Fokus auf COO statt Einkauf, 3-Tage-Follow-Up, Battle Cards in CRM dokumentiert
- **⚠️ Exit-Konsequenz:** Region Nord (31 Accounts, €312K Pipeline) hat keinen internen Nachfolger. Ramp-Zeit Ø 4,2 Monate = Region Nord bis Q1/2026 unter Kapazität, Pipeline-Impact ~€180K Q3/Q4
- Quellen: AE-Performance Q1/2025, Pipeline-Deals, CRM-Aktivitäten-Log, Win/Loss-Analyse, Personalplanung, Quota-Pipeline

---

---

## Szenario 12 — Meeting-Transkript: Teams-Aufzeichnung analysieren

**Was es zeigt:** Ein aufgezeichneter Kundentermin (Teams-Transkript) wird ins Second Brain gegeben. Claude erkennt automatisch Buy Signals, Churn-Warnungen, Konflikte mit Interndaten und konkrete To-Dos — in Sekunden, ohne dass jemand das Protokoll manuell auswertet.

### Schritt 1: Transkript einfügen (📎)
Öffne `~/rm-square/demo/hartmann/customers/Müller QBR Transkript Mai 2025.docx` und füge den Inhalt in den Dokumentbereich ein — oder wähle die Datei direkt per Datei-Picker.

### Schritt 2: Frage eingeben
```
Das ist das automatische Transkript unseres QBR-Termins mit Müller Maschinenbau von heute.
Analysiere es vollständig:
1. Welche Kauf- und Expansions-Signale stecken drin?
2. Welche Churn- oder Risiko-Signale?
3. Gibt es Aussagen die mit unseren internen Daten kollidieren?
4. Welche konkreten To-Dos entstehen — für wen, bis wann?
5. Was darf ich zusagen — und was braucht intern eine Freigabe?
```

### Was du siehst
- **💰 Buy Signal — Linie 4:** Dr. Winkler erwähnt neue Produktionslinie Q1/2026 mit 14×PD-500 + 4–6×SDX-7 + PD-1200. Kalkuliertes Volumen ~€185–220K. Noch kein Angebot angefragt — Hartmann muss proaktiv Workshop initiieren
- **💰 Buy Signal — CC-Premium Upgrade:** Koch fragt direkt nach Preis und will ROI-Szenario. Zahlungsbereitschaft erkennbar wenn Gesamtpaket stimmt. Upgrade-Delta €25.600/Jahr
- **💰 Buy Signal — DigiLink v2.0:** Winkler will Vibrationsmessung, hat aktuell externen Dienstleister. Direkte Substitution möglich — Pilot-Opportunity Q3
- **🚨 Churn-Signal — Siemens-Gespräch:** Koch hat SINAMICS S200 Präsentation gesehen und nennt "12–15% günstiger". Battle Card sagt das Gegenteil: SDX ist 15–25% günstiger als Siemens. Trotzdem: Signalwert hoch — Koch ist aktiv am Markt
- **🚨 Churn-Signal — 0x4210 Wiederholung:** Fehlercode jetzt an zweiter Maschine aufgetreten. Im CS-Dashboard als offene Eskalation bei KME dokumentiert — taucht jetzt auch bei Müller auf. Systemisches Problem?
- **⚠️ Konflikt — Zahlungsziel:** Koch sagt 60 Tage netto sei "Teil des Gesamtpakets". DoA: 60 Tage erfordert CRO + CFO-Freigabe. Zimmermann hat "bis Freitag" zugesagt ohne Freigabe zu haben — selbes Muster wie Brenner-Messe-Notiz
- **⚠️ Konflikt — CC-Preis:** Koch nennt "14.000 Euro" für CC-Plus aus dem Gedächtnis — tatsächlicher Preis laut Preisliste ist €12.400. Kleiner Unterschied, aber zeigt dass Kunde keine aktuelle Preisübersicht hat
- **📋 To-Dos mit Deadlines:** TCO-Vergleich Siemens (Zimmermann, Freitag) · CC-Premium ROI-Aufstellung (Kraus, Freitag) · Termin Support-Ingenieur 0x4210 (Kraus, heute) · Folgetermin kommerziell (Kalendereinladung mit Agenda, 2 Wochen) · Zahlungsziel 60T intern eskalieren (Zimmermann, Freitag) · Workshop Linie 4 (terminieren für Juni/Juli)
- Quellen: Kundenaccounts, CS-Dashboard, CareConnect-Nutzungsdaten, Preisliste, DoA, Battle Cards, Roadmap

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
