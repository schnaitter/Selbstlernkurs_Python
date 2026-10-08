---
short_title: "Aufgabe: Excel-Analyse"
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Abschlussaufgabe: Bibliotheksdaten auswerten

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

Diese Aufgabe schließt das Modul und den Kurs ab. Sie führen den kompletten
Workflow aus den vorangegangenen Kapiteln selbstständig durch: einlesen,
bereinigen, auswerten und visualisieren.

```{note} 📬 Abgabevermerk
:icon: false

Bearbeiten Sie die Aufgabe in einem eigenen Jupyter-Notebook. Geben Sie das
Notebook **ausgeführt** (mit sichtbaren Ausgaben und Diagrammen) sowie die
erzeugten Abbildungen als PNG-Dateien ab.

**Abgabe:** über den Kursbereich der Fernuniversität / per E-Mail an die
Kursleitung. Sprechen Sie die Frist bitte mit Ihrer Betreuung ab.

Die Aufgabe kann als **Kleine Aufgabe** angerechnet werden.

```

## Ausgangsdaten

Verwenden Sie die {term}`Excel`-Datei `assets/data/bibliothek_unsauber.xlsx`. Sie stammt aus
einem fiktiven Bibliothekssystem, enthält aber genau die Probleme, die auch bei
echten Exporten auftreten. Die Datei erzeugen Sie bei Bedarf neu mit:

```bash
$ python3 090-Projekt_Excel/generate_excel_data.py
```

Die Spalten lauten: `Titel`, `Autor*in`, `Erscheinungsjahr`, `Ausleihzahlen`,
`Standort`, `Medium`, `Zugangsdatum`. Das zweite Tabellenblatt `Standorte`
enthält eine saubere Nachschlagetabelle.

## Teilaufgabe 1 – Datenqualität prüfen und bereinigen

Erstellen Sie ein Notebook, das die Rohdaten einliest und bereinigt.

1. Lesen Sie das Tabellenblatt `Ausleihen` ein und verschaffen Sie sich mit
   `shape`, `info()` und `dtypes` einen Überblick.
2. Dokumentieren Sie in kurzen Markdown-Zellen, welche Probleme Sie finden:
   fehlende Werte, Duplikate, Spalten mit falschem Datentyp und uneinheitliche
   Kategorien.
3. Bereinigen Sie den Datensatz:
   * Duplikate entfernen,
   * `Erscheinungsjahr` in eine Zahl umwandeln,
   * `Ausleihzahlen` in eine Zahl umwandeln (Achtung: deutsche
     Tausenderpunkte!),
   * `Zugangsdatum` in ein Datum umwandeln,
   * `Standort` und `Medium` vereinheitlichen,
   * Spaltennamen in kleingeschriebene `snake_case`-Namen umbenennen.
4. Geben Sie am Ende an, wie viele Zeilen vorher und nachher vorhanden sind.

## Teilaufgabe 2 – Statistiken und Visualisierung

Führen Sie auf dem bereinigten Datensatz mindestens drei Auswertungen durch und
erstellen Sie dazu drei Diagramme.

1. **Kennzahlen je Standort:** Erstellen Sie mit {term}`Pandas` `groupby` eine Tabelle mit
   Anzahl, Summe, Mittelwert und Median der Ausleihzahlen je Standort.
2. **Häufigkeiten:** Ermitteln Sie mit `value_counts`, wie sich die Medienarten
   und Standorte verteilen.
3. **Diagramme:** Erstellen Sie
   * ein **Balkendiagramm** „Ausleihen je Standort“,
   * ein **Liniendiagramm** „Ausleihen nach Erscheinungsjahr“,
   * ein **Histogramm** „Verteilung der Ausleihzahlen“.

   Alle {term}`Matplotlib`-Diagramme benötigen **deutsche** Achsenbeschriftungen und Titel. Speichern
   Sie jedes Diagramm als PNG-Datei unter `assets/090/`.

4. Interpretieren Sie jedes Diagramm in ein bis zwei Sätzen: Was fällt auf?

## Teilaufgabe 3 – Erweiterung (optional)

Wählen Sie **eine** der folgenden Erweiterungen:

* Verknüpfen Sie den bereinigten Datensatz mit der Nachschlagetabelle
  `Standorte` (`merge`) und ergänzen Sie die Öffnungsstunden. Untersuchen Sie,
  ob Standorte mit mehr Öffnungsstunden auch mehr Ausleihen verzeichnen.
* Bauen Sie eine Auswertung „Top 10 der ausleihstärksten Titel“ und stellen Sie
  sie als horizontales Balkendiagramm dar.
* Recherchieren Sie einen echten offenen Bibliotheksdatensatz (z. B. über die
  Open-Data-Portale von Bibliotheken oder `data.europa.eu`) und wiederholen Sie
  die Bereinigung und Auswertung. Dokumentieren Sie die Quelle.

## Hinweise

* Orientieren Sie sich an den Kapiteln
  [Excel einlesen](010-Excel_einlesen.ipynb),
  [Daten bereinigen](020-Datenbereinigen.ipynb),
  [Statistiken](030-Statistiken.ipynb) und
  [Visualisierung](040-Visualisierung.ipynb).
* Kommentieren Sie Ihren Code und strukturieren Sie das Notebook mit
  Markdown-Überschriften.
* Achten Sie auf genderneutrale Schreibweise und deutsche Beschriftungen.
* Ein Notebook gilt als lauffähig, wenn es über *Restart Kernel and Run All
  Cells* fehlerfrei durchläuft.

```{seealso} Bewertungskriterien
:icon: false

| Kriterium | Beispiele |
| --- | --- |
| Korrektheit | Daten werden fehlerfrei eingelesen und bereinigt. |
| Vollständigkeit | Alle geforderten Auswertungen und Diagramme sind vorhanden. |
| Verständlichkeit | Code und Markdown sind nachvollziehbar kommentiert. |
| Darstellung | Diagramme haben deutsche Beschriftungen und sind korrekt gespeichert. |
| Reflexion | Ergebnisse werden sinnvoll interpretiert. |

```

## Beispiellösung

Zur Orientierung zeigt die folgende Abbildung ein mögliches Ergebnis für das
Balkendiagramm „Ausleihen je Standort“:

```{figure} ../assets/090/ausleihen_je_standort.png
:alt: Balkendiagramm der Ausleihen je Standort
:name: abb-beispiel-standort

Beispielhaftes Balkendiagramm „Ausleihen je Standort“.
```
