---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Verzeichnisse

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

## Index

:::{show-index}
:::

## Glossar

:::{glossary}

BibTeX

: Ein Format für die Speicherung von bibliographischen Angaben zur Verwendung
in LaTeX, Literaturverwaltungsprogrammen oder anderen, vorrangig
wissenschaftlich geprägten, Schreibkontexten.

Bibliothek

: Eine (meist extern entwickelte) Sammlung von wiederverwendbarem Programmcode,
die in Python über `import` eingebunden wird. Zentraler Bezugsort ist der
[Python Package Index (PyPI)](https://pypi.org/). In Python spricht man oft auch
von einem *Paket* (siehe {term}`Paket`).

Branch

: Ein Zweig innerhalb eines {term}`Repository`, in dem Änderungen unabhängig
vom Hauptzweig entwickelt werden können, ohne die stabile Version zu
beeinflussen. Siehe auch {term}`Git`.

Commit

: Ein einzelner, dauerhaft festgehaltener Zwischenstand in der
Versionsverwaltung. Ein Commit bündelt Änderungen mit einer beschreibenden
Nachricht sowie Angaben zu Autor\*in und Zeitpunkt. Siehe {term}`Git`.

Counter

: Eine Klasse aus dem Python-Modul `collections`, mit der Häufigkeiten einfach
gezählt werden können. Nützlich für die manuelle Analyse von Daten, z. B. um zu
ermitteln, welcher Wert wie oft vorkommt. Siehe auch den Abschnitt *Manuelle
Analyse* im Cheatsheet.

CSV

: **C**omma **S**eparated **V**alues. Ein einfaches textbasiertes Dateiformat,
in dem tabellarische Daten gespeichert und übertragen werden können.
Spezifiziert im [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180)

DataFrame

: Die zentrale Datenstruktur in {term}`Pandas`. Ein DataFrame ist eine
zweidimensionale Tabelle mit benannten Spalten und einem Index – vergleichbar
mit einem Excel-Blatt oder einer Tabelle in einer Datenbank.

defaultdict

: Eine Klasse aus dem Python-Modul `collections`, bei der fehlende Schlüssel
automatisch einen Standardwert erhalten. Praktisch zum Gruppieren von Werten,
ohne vorher prüfen zu müssen, ob ein Schlüssel existiert.

Excel

: Ein Tabellenverarbeitungsprogramm und das zugehörige Dateiformat `.xslx`,
welches oft für die Übertragung von tabellarischen Daten genutzt wird.

Git

: Ein Versionsverwaltungsprogramm, welches in den letzten Jahren zum
de-facto-Standard für die Entwicklung (freier) Software geworden ist.

JSON

: **J**ava**S**cript **O**bject **N**otation. Ein textbasiertes, weit
verbreitetes Datenaustauschformat, das in Python über das Modul `json` direkt
in Dictionaries und Listen übersetzt wird. Häufig als Schnittstellenformat für
Metadaten und Web-APIs im Bibliotheksbereich.

Jupyter

: Das [_project jupyter_](https://jupyter.org) ist eine Sammlung von Standards,
Projekten und Dienstleistungen zur programmiersprachenübergreifenden
Entwicklung interaktiver Rechenumgebungen.

Jupyter Book

: Jupyter Book ist ein Programm, welches Dateien das Schreiben von Websites und
anderen Ausgabeformaten mit Hilfe von Dateien in Formaten wie [MyST
Markdown](https://mystmd.org) und {term}`Jupyter Notebook` ermöglichen.

Jupyter Notebook

: Jupyter Notebook ist ein Name, der für mehrere zusammengehörige Dinge genutzt
wird. Jupyter Notebook ist ein Dateiformat (mit der Dateinendung `.ipynb`) in
welchem verschiedene statische Elemente wie Text oder Abbildungen mit
ausführbarem Programmcode kombiniert werden können. Des weiteren wird Jupyter
Notebook auch für das Sprechen über eine einzelne Datei in diesem Dateiformat
verwendet. Zudem spricht man auch von der Entwicklungsumgebung Jupyter
Notebook, in der diese Dateien bearbeitet und genutzt werden.

JupyterHub

: Ein Server, auf dem für Nutzer\*innen eine Jupyter-Arbeitsumgebung
bereitgestellt wird.

JupyterLab

: Eine Jupyter-Arbeitsumgebung, welche das Arbeiten mit mehreren Jupyter
Notebooks, Editoren für andere Dateiformate und Terminals ermöglicht.

MARC 21

: Ein bibliothekarisches Austauschformat für Metadaten (Machine-Readable
Cataloging). Es definiert Felder und Unterfelder für Titelaufnahmen; die
XML-Variante ist {term}`MARC-XML`.

MARC-XML

: Ein XML Schema zur Übertragung von MARC 21 Daten. Siehe
<https://www.loc.gov/standards/marcxml/>

Matplotlib

: Eine Programmbibliothek zur Visualisierung von Daten. Siehe
<https://matplotlib.org/>

NumPy

: Eine Programmbibliothek für das effiziente Rechnen mit Vektoren und Matrizen
in Python. Siehe <https://numpy.org/>

openpyxl

: Eine Python-Bibliothek zum Lesen und Schreiben von Excel-Dateien (`.xlsx`).
Wird von {term}`Pandas` bei `read_excel`/`to_excel` im Hintergrund genutzt.

Paket

: Eine Sammlung von Python-Modulen, die gemeinsam verteilt und installiert
wird. Oberbegriff siehe *Bibliothek*.

Pandas

: Eine Programmbibliothek, für die Verarbeitung tabellarischer Daten, die u.a.
durch die Nutzung von NumPy besonders effizient ist. Siehe
<https://pandas.pydata.org/>

Python

: Programmiersprache die einerseits gut zu erlernen und andererseits in der
Forschung weit verbreitet ist. Benannt nach Monty Python.

REPL

: **R**ead-**E**val-**P**rint-**L**oop. Ein Programm, in das Programmcode
(bspw. in Python) eingegeben und dann ausgeführt werden kann. Besonders
nützlich, um interaktiv kleinere Skripte auszutesten oder auszuführen.

Repository

: Ein Projektverzeichnis, das von einem Versionsverwaltungssystem wie
{term}`Git` verwaltet wird. Es enthält den gesamten Änderungsverlauf und kann
lokal oder auf einer Plattform (z. B. GitHub) liegen.

Skript

: Eine Datei, die Programm-Code – meist in eine "Skriptsprache" geschrieben –
enthält, welcher direkt ausgeführt werden kann.

: Ein Programm, welches eine kleine, wohldefinierte Aufgabe ausführt.

Unix

: In diesem Kontext wird ist hier die Familie der Unix-artigen Betriebssysteme
gemeint. Hier spielt vorrangig Linux eine Rolle. Aber auch BSD-basierte
Betriebssystem wie macOS sind für den Kurs als Unix-artig anzusehen.

Versionskontrolle

: Die systematische Verwaltung von Änderungen an Dateien über die Zeit, sodass
frühere Stände nachvollzogen und wiederhergestellt werden können. Siehe
{term}`Git`.

XML

: **E**xtensible **M**arkup **L**anguage. Ein textbasiertes Auszeichnungsformat
zur strukturierten Darstellung hierarchischer Daten. Beispiele im Kurs sind
{term}`MARC-XML` und verwandte bibliothekarische Metadatenformate.

:::
