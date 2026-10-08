---
short_title: Ausblick
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Ausblick

```{seealso} 🎓 Lernziele
:icon: false

Nach diesem kurzen Ausblick können Sie einordnen, …

- … welche Aufgaben die manuelle Analyse (noch) löst und wo ihre Grenzen liegen.
- … welche Werkzeuge im weiteren Kurs aufbauen ({term}`Pandas`, {term}`Excel`, {term}`XML`).
- … warum die hier gelernten Grundlagen auch mit Komfort-Bibliotheken nützlich bleiben.

```

```{seealso} Vorwissen
:icon: false

Dieser Ausblick schließt an das Vorkapitel
[Projekt: CSV I](../040-Projekt_CSV_I/000-Einleitung.md) sowie an die
vorangehenden Kapitel dieses Moduls an.

```

## Was Sie jetzt können

Sie haben einen realen Datensatz mit reinen Python-Bordmitteln ausgewertet:
Zeichenkodierung verstehen, unregelmäßige Zeilen abfangen, Kennzahlen wie
Mittelwert, Median und Standardabweichung selbst berechnen sowie mit
Dictionaries und `collections` gruppieren und aggregieren. Damit können Sie
jede überschaubare Datenanalyse ohne Zusatzpakete umsetzen.

Die manuelle Analyse stößt dort an Grenzen, wo

- sehr viele Spalten gleichzeitig ausgewertet werden sollen,
- komplexe Gruppierungen und Verknüpfungen mehrerer Tabellen nötig sind,
- Daten visualisiert (Diagramme) oder in andere Formate exportiert werden.

## Wie es weitergeht

- **Projekt: MARC-XML** – bibliothekarische Metadaten in einem
  {term}`XML`-Format lesen, filtern und in andere Formate transformieren.
  Siehe [Einleitung zu MARC-XML](../080-Projekt_MARC-XML/000-Einleitung.md).
- **Projekt: Excel** – dasselbe Analyseziel wie hier, aber mit der
  Komfort-Bibliothek `pandas` und mit Visualisierungen.
  Siehe [Einleitung zu Excel](../090-Projekt_Excel/000-Einleitung.md).
- **Cheatsheet (900)** – Kurzreferenz für `csv`, Dictionaries und
  `collections`: [Cheatsheet](../900-Cheatsheet.md).

Die hier geübte Denkweise – erst einlesen und prüfen, dann in Dictionaries
strukturieren, dann aggregieren – ist genau die Denkweise, die Ihnen später
auch bei `pandas` wieder begegnet. Nur übernimmt dort die Bibliothek einen Teil
der Schreibarbeit.
