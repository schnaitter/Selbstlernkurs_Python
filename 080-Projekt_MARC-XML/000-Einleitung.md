---
short_title: "Projekt: MARC-XML"
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Projekt: MARC-XML lesen, filtern und in eine BibTeX-Datei überführen

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

```{seealso} 🎓 Lernziele
:icon: false

In diesem Kapitel erlernen Sie, …

- … wie bibliografische Daten im Format MARC-XML aufgebaut sind.
- … wie Sie XML-Dateien mit der Standardbibliothek
  (`xml.etree.ElementTree`) einlesen.
- … wie Sie Records, Felder und Unterfelder auslesen und filtern.
- … wie Sie JSON-Daten in MARC-XML überführen (Import-Vorbereitung).
- … wie Sie MARC-Daten nach BibTeX exportieren.

```

```{seealso} Vorwissen
:icon: false

Dieses Kapitel baut auf den vorangegangenen Projektkapiteln auf:

- [Projekt: Bestseller finden (CSV)](../040-Projekt_CSV_I/000-Einleitung.md) –
  Dateien öffnen, einlesen und strukturiert verarbeiten.
- [Projekt: Statistiken eines Datensatzes (CSV)](../070-Projekt_CSV_II/000-Einleitung.md) –
  Listen, Dictionaries und Filterlogik.
```

```{hint} 📝 Kleine Aufgabe
:icon: false

Die Aufgabe am Ende dieses Kapitels kann als Kleine Aufgabe angerechnet werden.
```

In diesem Kapitel beschäftigen wir uns mit **MARC-XML**, dem XML-basierten
Austauschformat für bibliografische Daten. Wir lernen zunächst den Aufbau von
MARC-Records kennen, lesen und filtern eine MARC-XML-Datei, wandeln
JSON-Quelldaten in MARC-XML um und exportieren die Daten schließlich nach
**BibTeX**.

Das Kapitel gliedert sich wie folgt:

1. [MARC-XML: Grundlagen](./010-MARC-XML_Grundlagen.md) – Format, Leader,
   Felder, Unterfelder und Namensräume.
1. [Einlesen und Filtern](./020-Einlesen_Filtern.ipynb) – Records mit Python
   parsen und nach Jahr, Sprache und Schlagwort filtern.
1. [JSON zu MARC-XML](./030-JSON_zu_MARC-XML.ipynb) – JSON-Daten auf die
   MARC-Struktur abbilden und valides MARC-XML schreiben.
1. [Export nach BibTeX](./040-Export_BibTeX.ipynb) – MARC-Daten in eine
   `.bib`-Datei übertragen.
1. [Aufgabe](./050-Aufgabe.md) – selbstständige Anwendung mit Abgabe.

```{seealso} 📚 Weiterführende Ressourcen
:icon: false

- **Offizielle Dokumentation:** [xml.etree.ElementTree — The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html)
- **Offizielle Dokumentation:** [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- **Bibliotheksstandard:** [MARCXML — Library of Congress](https://www.loc.gov/standards/marcxml/)
- **Kostenloses Lernmaterial:** [Understanding MARC Bibliographic](https://www.loc.gov/marc/umb/)
- **Bibliotheksspezifische OER:** [Library Carpentry: Working with MARC Data](https://librarycarpentry.org/lc-marcedit/)

```
