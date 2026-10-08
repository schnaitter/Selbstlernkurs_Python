---
short_title: Aufgabe
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Aufgabe: MARC-Daten auswerten und exportieren

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

```{seealso} Vorwissen
:icon: false

Diese Aufgabe fasst die Inhalte aus [Einlesen und Filtern](./020-Einlesen_Filtern.ipynb),
[JSON zu MARC-XML](./030-JSON_zu_MARC-XML.ipynb) und dem
[Export nach BibTeX](./040-Export_BibTeX.ipynb) zusammen. Die Arbeit mit
Dictionaries und Zählungen kennen Sie bereits aus dem
[Projekt CSV II](../070-Projekt_CSV_II/000-Einleitung.md) und dem
[Projekt CSV I](../040-Projekt_CSV_I/000-Einleitung.md).
```

## Überblick

In dieser Aufgabe wenden Sie den vollständigen Transformationsweg selbstständig
an: {term}`MARC-XML` einlesen, filtern, auswerten und nach {term}`BibTeX` exportieren. Die
Grundlage bilden die synthetischen Beispieldaten aus dem Skript
`generate_marc_data.py`:

- `assets/data/beispieldaten.json` – bibliografische Quelldaten
- `assets/data/beispieldaten.marcxml` – dieselben Titel als MARC-XML

Legen Sie Ihre Skripte und Ergebnisdateien im Ordner `080-Projekt_MARC-XML/`
beziehungsweise in `assets/data/` ab.

## Aufgabe 1: Filtern, Auswerten und Exportieren

Schreiben Sie ein ausführbares Python-Skript `marc_auswertung.py`, das folgende
Schritte durchführt:

1. `assets/data/beispieldaten.marcxml` mit `xml.etree.ElementTree` einlesen.
2. Für jeden Record die Felder `001`, `020 $a`, `041 $a`, `100 $a`, `245 $a/$b`
   und `264 $c` in ein Dictionary überführen (wie im
   [Kapitel zum Einlesen](./020-Einlesen_Filtern.ipynb)).
3. Alle Titel herausfiltern, die **deutschsprachig** (`ger`) sind **oder** das
   Schlagwort `Metadaten` tragen.
4. Für jeden Treffer eine Zeile mit Jahr, Autor\*in, Titel und ISBN ausgeben.
5. Eine kleine Statistik ausgeben:
   - die Anzahl der Titel je Sprache (nutzen Sie ein Dictionary),
   - das früheste und das späteste Erscheinungsjahr,
   - die Gesamtzahl der Titel.
6. Die gefilterten Titel als BibTeX-Einträge (`@book`) in die Datei
   `assets/data/aufgabe.bib` schreiben (wie im
   [Export-Kapitel](./040-Export_BibTeX.ipynb)).

```{hint} Hinweis
:icon: false

Achten Sie auf eine saubere Funktionstrennung (Einlesen, Filtern, Auswerten,
Exportieren) und auf die PEP-8-Konventionen aus dem Kurs. Die Datei
`aufgabe.bib` muss von einem gängigen Literaturverwaltungsprogramm oder von
LaTeX gelesen werden können.
```

## Aufgabe 2: Eigene Titel importieren

Erweitern Sie den Importweg um eigene Daten:

1. Ergänzen Sie `assets/data/beispieldaten.json` um **drei frei erfundene
   Titel**. Verwenden Sie dieselben Felder wie die vorhandenen Einträge
   (`id`, `isbn`, `autor`, `titel`, `untertitel`, `ort`, `verlag`, `jahr`,
   `sprache`, `schlagwoerter`). Denken Sie an eine eindeutige `id`.
2. Schreiben Sie ein ausführbares Python-Skript `json_zu_marc.py`, das die
   {term}`JSON`-Daten einliest und daraus eine valide MARC-XML-Datei
   `assets/data/aufgabe.marcxml` erzeugt.
3. Prüfen Sie am Ende des Skripts mit `ElementTree`, dass die erzeugte Datei
   genauso viele Records enthält wie die JSON-Datei Titel. Geben Sie das
   Ergebnis auf der Kommandozeile aus.

```{note} Kein `pymarc` nötig
:icon: false

Verwenden Sie wie im Kurs ausschließlich die Standardbibliothek
`xml.etree.ElementTree`. Das Paket `pymarc` wurde im Kapitel
[MARC-XML: Grundlagen](./010-MARC-XML_Grundlagen.md) nur als professioneller
Ausblick vorgestellt.
```

## Erwartete Ergebnisdateien

| Datei | Inhalt |
| --- | --- |
| `080-Projekt_MARC-XML/marc_auswertung.py` | Skript zu Aufgabe 1 (Filter, Statistik, BibTeX-Export) |
| `assets/data/aufgabe.bib` | BibTeX-Einträge der gefilterten Titel |
| `080-Projekt_MARC-XML/json_zu_marc.py` | Skript zu Aufgabe 2 (JSON → MARC-XML) |
| `assets/data/aufgabe.marcxml` | valides MARC-XML mit allen Titeln |

## Abgabe

```{hint} 📝 Kleine Aufgabe
:icon: false

Diese Aufgabe kann als **Kleine Aufgabe** abgegeben werden. Reichen Sie dazu
die vier Dateien aus der Tabelle oben ein. Achten Sie darauf, dass beide
Skripte ausführbar sind, eine Shebang-Zeile (`#! /usr/bin/env python3`)
besitzen und ohne Fehler durchlaufen.
```
