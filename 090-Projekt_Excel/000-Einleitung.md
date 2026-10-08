---
short_title: "Projekt: Excel"
numbering:
    heading_1: true
    heading_2: false
    title: true
---

# Projekt: Excel-Daten analysieren

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

Excel-Exporte gehören zum Alltag in Bibliotheken: Ausleihstatistiken,
Bestandslisten oder Medienetiketten werden häufig als `.xlsx`-Datei
weitergegeben. In diesem Abschlussprojekt lernen Sie, solche Dateien mit
**pandas** einzulesen, zu bereinigen, statistisch zu beschreiben und mit
**matplotlib** zu visualisieren.

```{seealso} 🎓 Lernziele
:icon: false

In diesem Kapitel erlernen Sie, …

- … wie Sie Excel-Dateien mit `pandas.read_excel` einlesen und Tabellenblätter
  (Sheets) gezielt ansprechen.
- … wie Sie typische Datenprobleme erkennen und mit pandas bereinigen
  (fehlende Werte, Duplikate, falsche Datentypen, uneinheitliche Kategorien).
- … wie Sie aus einem Datensatz mit `describe`, `groupby` und `value_counts`
  aussagekräftige Kennzahlen je Standort und Medium gewinnen.
- … wie Sie mit matplotlib Balken-, Linien- und Histogramm-Diagramme mit
  deutschen Beschriftungen erstellen und als PNG speichern.
- … wie Sie einen vollständigen Analyse-Workflow vom Rohdatenexport bis zur
  Abbildung selbstständig durchführen.

```

```{seealso} Vorwissen
:icon: false

Dieses Projekt baut auf den beiden CSV-Projekten auf.

- In [Projekt CSV I](../040-Projekt_CSV_I/000-Einleitung.md) haben Sie gelernt,
  Dateien zu öffnen und Daten einzulesen.
- In [Projekt CSV II](../070-Projekt_CSV_II/000-Einleitung.md) haben Sie
  Datensätze „von Hand“ ausgewertet. Hier wechseln Sie nun zur
  State-of-the-Art-Variante mit pandas.
- Falls Sie Begriffe wie *DataFrame*, *Datenbereinigung* oder *Tidy Data*
  nachschlagen möchten, hilft das
  [Glossar](../999-Epilog/Verzeichnisse.md).

```

## Fahrplan durch dieses Kapitel

Die Beispieldaten werden mit dem Skript
[`generate_excel_data.py`](generate_excel_data.py) reproduzierbar erzeugt: eine
bewusst „unsaubere“ Excel-Datei (`assets/data/bibliothek_unsauber.xlsx`) mit
fehlenden Werten, Duplikaten, falsch typisierten Spalten und uneinheitlichen
Kategorien.

1. [Excel einlesen](010-Excel_einlesen.ipynb) – `read_excel`, Sheets, erster
   Überblick und das Erkennen von Typ-Problemen.
2. [Daten bereinigen](020-Datenbereinigen.ipynb) – fehlende Werte, Duplikate,
   Typkonvertierung und Tidy Data.
3. [Statistiken berechnen](030-Statistiken.ipynb) – `describe`, `groupby`,
   `value_counts` und Kennzahlen je Standort und Medium.
4. [Daten visualisieren](040-Visualisierung.ipynb) – Balken-, Linien- und
   Histogramm-Diagramme mit deutschen Beschriftungen.
5. [Abschlussaufgabe](050-Aufgabe.md) – eine vollständige Analyse als
   anrechenbare Leistung.

```{hint} 📝 Abschlussprojekt
:icon: false

Die [Aufgabe am Ende des Kapitels](050-Aufgabe.md) ist das Abschlussprojekt
dieses Kurses. Sie können es als Kleine Aufgabe anrechnen lassen.

```

```{seealso} 📚 Weiterführende Ressourcen
:icon: false

- **Offizielle Dokumentation:** [pandas.read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
- **Offizielle Dokumentation:** [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- **Offizielle Dokumentation:** [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- **Buch (kostenlos):** Wes McKinney, [*Python for Data Analysis* (3. Auflage, online)](https://wesmckinney.com/book/)
- **Bibliotheksspezifische OER:** [Library Carpentry: Tidy Data for Librarians](https://librarycarpentry.org/lc-spreadsheets/)

```
