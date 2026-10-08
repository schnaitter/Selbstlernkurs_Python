---
short_title: "Projekt: CSV II"
numbering:
    heading_1: true
    heading_2: false
    title: true
---

# Projekt: Statistiken eines Datensatzes (CSV)

```{seealso} 🎓 Lernziele
:icon: false

In diesem Kapitel erlernen Sie, …

- … wie Sie Daten mit Dictionaries und dem Modul `collections` strukturiert ablegen.
- … wie Sie auch ältere Zeichenkodierungen (Latin-1) und kaputte Zeichen beherrschen und Textfelder in passende Datentypen umwandeln.
- … wie Sie eine beschreibende Statistik mit Python-Bordmitteln (Listen, Dictionaries, `collections`) erstellen – also ohne `pandas`.
- … wie Sie Fehler mit `try`/`except` behandeln und große Dateien speicherschonend zeilenweise verarbeiten.
- … wie Sie die Laufzeit kleiner Programme messen und einfache Optimierungen anwenden.
- … wie Sie Rohdaten in eine besser nutzbare Zielstruktur überführen (Datenmigration).

```

```{hint} 📝 Kleine Aufgabe
:icon: false

Die Aufgabe am Ende dieses Kapitels kann als Kleine Aufgabe angerechnet werden.

```

## Worum geht es?

Im Projekt [**CSV I**](../040-Projekt_CSV_I/000-Einleitung.md) haben Sie gelernt, wie Sie Dateien öffnen, eine
CSV-Datei „von Hand“ und mit dem Modul `csv` einlesen. Die Daten lagen danach
als Liste von Zeilen bzw. als Liste von Dictionaries vor. Sie haben aber noch
nicht systematisch damit *gerechnet*.

Genau das holen wir in diesem Kapitel nach: Wir beantworten Fragen an einen
Datensatz mit den Mitteln, die Python „an Bord“ hat – **ohne `pandas`**. Das
klingt umständlicher als nötig, hat aber einen didaktischen Zweck: Wer die
manuelle Analyse beherrscht, versteht, was Komfort-Bibliotheken wie `pandas`
(später in [Projekt Excel](../090-Projekt_Excel/000-Einleitung.md)) im Hintergrund für uns erledigen. Außerdem kommen Sie mit reinen
Bordmitteln überall dort zurecht, wo keine Zusatzpakete installiert werden
dürfen.

## Der Datensatz

In diesem Modul nutzen wir dieselbe synthetisch erzeugte Datei wie im
Vorkapitel [Projekt CSV I](../040-Projekt_CSV_I/000-Einleitung.md):

`assets/data/books_powerlaw_dataset.csv`

Die Datei enthält Verkaufszahlen von 30 Büchern über sechs Jahre und hat
folgende Spalten:

| Spalte       | Bedeutung                                             |
| ---          | ---                                                   |
| `isbn`       | ISBN-13 des Werks                                     |
| `author`     | Autor\*in (Format `Nachname, Vorname`)                |
| `year`       | Erscheinungsjahr des Werks                            |
| `title`      | Titel                                                 |
| `sales_year` | Jahr, in dem die Verkäufe gezählt wurden              |
| `sales`      | Anzahl der Verkäufe in diesem Jahr                    |

Die Verkaufszahlen folgen einer *Power-Law*-Verteilung (viele kleine, wenige
sehr große Werte). Dadurch sind Mittelwert und Median deutlich verschieden – ein
schöner Anlass, um über Kennzahlen nachzudenken.

## Kapitelüberblick

| Kapitel                                        | Inhalt                                                              |
| ---                                            | ---                                                                 |
| [Datenstrukturen](005-Datenstrukturen.ipynb)               | Dictionaries und `collections` systematisch einführen              |
| [Erweiterte CSV-Verarbeitung](010-Erweiterte_CSV_Verarbeitung.ipynb) | Alte Encodings (Latin-1), Feinsteuerung von Quotes, Typkonvertierung |
| [Manuelle Analyse](020-Manuelle_Analyse.ipynb)             | Beschreibende Statistik, Gruppieren und Aggregieren                  |
| [Fehlerbehandlung & Performance](030-Fehlerbehandlung_Performance.ipynb) | `try`/`except`, Streaming, Laufzeitmessung, Datenmigration |
| [Aufgabe: Statistik](040-Aufgabe_Statistik.ipynb)         | Anrechenbare Aufgabe                                                |
| [Ausblick](050-Ausblick.md)                              | Wie es mit `pandas`, Excel und MARC-XML weitergeht                  |

```{seealso} Vorwissen aus Projekt CSV I
:icon: false

Dieses Kapitel baut unmittelbar auf dem Vorkapitel auf. Wenn Ihnen das Öffnen
von Dateien, das Einlesen mit dem Modul `csv` oder der Umgang mit Dictionaries
nicht mehr präsent ist, arbeiten Sie zuerst

- [Projekt: Bestseller finden (CSV)](../040-Projekt_CSV_I/000-Einleitung.md)

durch. Insbesondere die Kapitel zu `csv.reader`/`csv.DictReader` und zur
Typkonvertierung werden hier vorausgesetzt.

```

```{seealso} 📚 Weiterführende Ressourcen
:icon: false

- **Offizielle Dokumentation:** [collections — Container datatypes](https://docs.python.org/3/library/collections.html)
- **Offizielle Dokumentation:** [statistics — Mathematical statistics functions](https://docs.python.org/3/library/statistics.html)
- **Buch (kostenlos):** Wes McKinney, [*Python for Data Analysis* (3. Auflage, online)](https://wesmckinney.com/book/)
- **Bibliotheksspezifische OER:** [Library Carpentry: Introduction to Data](https://librarycarpentry.org/lc-data-intro/)

```
