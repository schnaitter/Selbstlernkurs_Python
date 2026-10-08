---
short_title: "Projekt: CSV I"
numbering:
    heading_1: true
    heading_2: false
    title: true
---

# Projekt: Bestseller finden (CSV)

```{seealso} 🎓 Lernziele
:icon: false

In diesem Kapitel erlernen Sie, …

- … wie Sie Dateien öffnen, lesen und zuverlässig wieder schließen.
- … wie Sie CSV-Dateien „von Hand“ mit `split()` und `strip()` verarbeiten.
- … wie Sie das Standardmodul `csv` mit `csv.reader` und `csv.DictReader` nutzen.
- … wie Sie eingelesene Datensätze validieren und fehlerhafte Zeilen behandeln.
- … wie Ihre Skripte Kommandozeilen-Parameter (command-line arguments) nutzen
  können.

```

```{hint} 📝 Kleine Aufgabe
:icon: false

Die Aufgabe am Ende dieses Kapitels ({ref}`bestseller-finden`) kann als Kleine
Aufgabe angerechnet werden.

```

## Fahrplan durch dieses Kapitel

Als durchgängiges Beispiel dient der synthetisch erzeugte Datensatz
`assets/data/books_powerlaw_dataset.csv`. Er enthält für die Jahre 2020 bis
2025 Verkaufszahlen zu einer Reihe von Büchern.

**Kapitelinhalt:**

1. [Dateiformat CSV](./010-Dateiformat.md) – Aufbau, Trennzeichen und
   Anführungszeichen einer CSV-Datei.
2. [Dateien öffnen](./020-Dateien_öffnen.ipynb) – `open()`, der
   `with`-Kontextmanager, Lesemethoden, Encoding und typische Fehler.
3. [CSV von Hand einlesen](./030-CSV_einlesen_manuell.ipynb) – `split()`,
   `strip()`, Header-Trennung, Liste von Listen und die Grenzen des manuellen
   Parsens.
4. [Das Modul `csv`](./040-CSV_einlesen_Modul.ipynb) – `csv.reader`,
   `csv.DictReader`, `delimiter`, `quotechar` und Edge Cases.
5. [Datenvalidierung](./045-Datenvalidierung.ipynb) – Spaltenzahl prüfen,
   fehlerhafte Zeilen protokollieren und Typkonvertierungen absichern.
6. [Kommandozeilen-Parameter](./046-Kommandozeilen_Parameter.ipynb) – den
   CSV-Pfad beim Aufruf mit `sys.argv` übergeben.
7. [Aufgabe: Bestseller finden](./050-Aufgabe_Bestseller.ipynb) – Auswertung des
   Datensatzes als Kleine Aufgabe.

```{seealso} Vorwissen
:icon: false

Dieses Kapitel setzt das [Projekt: Taschenrechner
I](../020-Projekt_Taschenrechner_I/000-Einleitung.md) voraus. Dort haben Sie
gelernt, Variablen, Schleifen, Bedingungen, Listen und Funktionen zu verwenden
und [ausführbare Skripte](../020-Projekt_Taschenrechner_I/050-Ausführbare_Skripte.md)
zu schreiben. Für den Umgang mit Dateipfaden sind Kenntnisse aus dem
[Exkurs Unix](../030-Exkurs_Unix/030-Dateisystem_Navigation.md) hilfreich.

```

```{seealso} 📚 Weiterführende Ressourcen
:icon: false

- **Offizielle Dokumentation:** [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
- **Offizielle Dokumentation:** [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) im Python-Tutorial
- **Buch (kostenlos):** Al Sweigart, [*Automate the Boring Stuff with Python* – Kapitel 9: Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/)
- **Bibliotheksspezifische OER:** [Library Carpentry: Introduction to Python](https://librarycarpentry.org/lc-python-intro/)

```
