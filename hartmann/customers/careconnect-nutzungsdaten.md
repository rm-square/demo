# Hartmann Antriebstechnik — CareConnect Nutzungsdaten & Service-Analytics

**Owner:** CSM-Team + COO Markus Preis
**Stand:** 30. April 2025
**Datenbasis:** CareConnect-Platform-Export, Service-Tickets, Vor-Ort-Einsatz-Protokolle

---

## 1. Plattform-Übersicht

| Kennzahl | Wert |
|---|---|
| Aktive CareConnect-Konten | 68 |
| Verbundene Antriebe gesamt | 1.847 |
| Ø Antriebe pro Konto | 27 |
| Predictive Alerts ausgelöst Q1/2025 | 312 |
| Davon korrekte Vorwarnungen (verifiziert) | 267 (85,6%) |
| Vermiedene ungeplante Ausfälle (geschätzt) | 43 |
| Ø Kosten ungeplanter Ausfall (Kundenbericht) | €12.400 |
| **Vermiedener Schaden Q1/2025 (geschätzt)** | **€533K** |

---

## 2. Account-Level Nutzungsdaten

### Brenner Automotive Stuttgart (CC-Premium)
| Metrik | Wert |
|---|---|
| Verbundene Antriebe | 274 (180x SDX-22 + 94x PD-3000) |
| Uptime CareConnect-Portal | 99,7% |
| Predictive Alerts Q1 | 47 |
| Korrekte Vorwarnungen | 41 |
| Ungeplante Ausfälle Q1 | 2 (beide OHNE vorherigen Alert — Hardware-Defekt) |
| Vor-Ort-Reaktionszeit (Ø) | 6,2h (SLA: 24h CC-Premium) |
| Kundenzufriedenheit (letzter QBR Jan 2025) | **NPS: 8** |
| Offene Serviceanfragen | 0 |

**Hinweis RFQ Bratislava:** Brenner fordert für Bratislava 8h SLA. Aktuell werden 6,2h im Stammwerk Stuttgart erreicht — aber das ist mit vollem Technik-Team. Bratislava: 2 Techniker, realistisch 48h.

### Müller Maschinenbau Ingolstadt (CC-Plus)
| Metrik | Wert |
|---|---|
| Verbundene Antriebe | 59 (47x PD-500 + 12x SDX-2 SI) |
| Uptime Portal | 98,1% |
| Predictive Alerts Q1 | 8 |
| **Ignorierte Alerts vor Ausfall** | **3** |
| Ungeplante Ausfälle Q1 | 1 (PD-500, 23. März — der SLA-Verletzungsfall) |
| Vor-Ort-Reaktionszeit (Ø) | 31h (SLA: 24h CC-Plus) — SLA verletzt |
| Kundenzufriedenheit | **NPS: 6** (Vorquartal: NPS 8) |

⚠️ **Kritischer Befund:** Vor dem PD-500-Ausfall am 23. März hat das CareConnect-System an den 3 vorherigen Tagen Temperatur-Anomalie-Alerts ausgelöst. Die Alerts wurden im Portal angezeigt aber nicht von Müller-Personal quittiert und nicht von Hartmann CSM bemerkt.

**CC-Premium hätte diesen Ausfall verhindert:** CC-Premium löst bei ignorierten Alerts nach 24h automatisch CSM-Eskalation aus. CC-Plus tut das nicht. Das ist das stärkste Upgrade-Argument für den QBR am 15. Mai.

### KME Kunststofftechnik Ulm (CC-Base)
| Metrik | Wert |
|---|---|
| Verbundene Antriebe | 8 (8x SDX-2 SI) |
| Uptime Portal | 87% (unter Erwartung) |
| Predictive Alerts Q1 | 0 (SDX-2 mit E-Code 0x4210 war nicht verbunden) |
| Ungeplante Ausfälle Q1 | 3 |
| Kundenzufriedenheit | **NPS: 4** |

**Problem:** SDX-2 E-Code 0x4210 tritt bei Drives auf die NICHT mit CareConnect verbunden sind — oder die Verbindung läuft seit dem letzten Firmware-Update ins Leere. Das CC-Base-Paket enthält keinen automatischen Diagnose-Check. Deshalb kein Alert vor den Ausfällen.

### Zeller Fördertechnik Nürnberg (CC-Base)
| Metrik | Wert |
|---|---|
| Verbundene Antriebe | 42 (28x PD-1200 + 14x PD-3000) |
| Uptime Portal | 96,3% |
| Predictive Alerts Q1 | 6 |
| Korrekte Vorwarnungen | 5 |
| Ungeplante Ausfälle Q1 | 2 |
| Vor-Ort-Reaktionszeit (Ø) | 28h (SLA: 24h CC-Base) — 2x SLA verletzt |
| Kundenzufriedenheit | **NPS: 7** |
| **Ungeplante Einsätze letzter 12 Monate** | **4** |

⚠️ **Upgrade-Trigger erfüllt:** Laut Kampagne 2 (CareConnect) ist der Trigger für Upgrade-Gespräch: ≥3 ungeplante Einsätze in 12 Monaten. Zeller hat **4**. Niemand hat den Upsell-Prozess ausgelöst. Wien-Projekt bietet natürlichen Kontext.

### Bergmann & Söhne Bielefeld (kein CareConnect)
| Metrik | Wert |
|---|---|
| Verbundene Antriebe | 0 |
| Aktive Serviceverträge | Keiner |
| Service-Anfragen (ad hoc) | 2 in Q1 (telefonisch, ohne Ticket) |
| Letzter Vor-Ort-Einsatz | November 2024 |

**Upsell-Potenzial:** 6x PD-200 Edelstahl. CC-Base wäre €4.800/Jahr. Inbound-Anfrage €41K liegt unbearbeitet — darin wahrscheinlich Service-Komponente.

---

## 3. SLA-Performance nach CC-Tier (alle Accounts)

| CC-Tier | Konten | Ø Reaktionszeit | SLA-Ziel | SLA-Einhaltung |
|---|---|---|---|---|
| CC-Premium | 8 | 5,8h | 8h Vor-Ort | **96%** |
| CC-Plus | 22 | 26,4h | 24h | **71%** |
| CC-Base | 38 | 41,2h | 48h | **84%** |

⚠️ **CC-Plus SLA-Einhaltung 71% ist kritisch.** Ein Drittel aller CC-Plus-Kunden wartet länger als 24h. Ursache: mangelnde Ersatzteil-Verfügbarkeit vor Ort + Techniker-Routenplanung nicht optimiert.

---

## 4. Predictive Failure Score — Top Alerts Mai 2025

Aktive Warnungen die sofortige Aufmerksamkeit benötigen:

| Account | Drive | Alert-Typ | Score | Dringlichkeit |
|---|---|---|---|---|
| Logistikzentrum Süd GmbH | PD-3000 #7 | Temperaturanstieg +18°C über Baseline | 82/100 | 🔴 Kritisch — innerhalb 2 Wochen Ausfall möglich |
| Pharmariese Hartmann-Koch AG | SDX-7 #3 | Vibrations-Anomalie erkannt | 71/100 | 🟡 Mittel — Inspektion empfohlen |
| Heizungsbauer Kern GmbH | PD-500 #2 | Betriebsstunden > Wartungsintervall | 65/100 | 🟡 Mittel — Wartung überfällig |

---

## 5. Nutzungs-Tiefe nach Tier (Feature Adoption)

| Feature | CC-Base | CC-Plus | CC-Premium |
|---|---|---|---|
| Dashboard-Login/Monat | 2,1x | 4,8x | 12,3x |
| Alert-Quittierung < 24h | 31% | 58% | 89% |
| Predictive Failure Score aktiv | Nein | Nein | Ja |
| Auto-Eskalation bei ignoriertem Alert | Nein | Nein | Ja |
| QBR-Vorbereitung durch CSM | Nein | 1x/Jahr | 2x/Jahr |
| Direktleitung CSM | Nein | Ja | Ja |

**Erkenntnis:** CC-Base-Kunden loggen sich kaum ein. Das CareConnect-Wert-Versprechen kommt bei Base-Kunden nicht an. Übergang zu CC-Plus verdoppelt Engagement, CC-Premium vervierfacht es.
