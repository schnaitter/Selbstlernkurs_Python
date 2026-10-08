---
short_title: Häufige Fehler & Lösungen
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Häufige Fehler & Lösungen

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

Fehlermeldungen gehören zum Programmieren dazu – auch Profis verbringen einen
großen Teil ihrer Zeit damit, sie zu lesen und zu beheben. Diese Seite ist als
**Nachschlagewerk** gedacht: Sie sammelt die Fehler, die im Kurs am häufigsten
auftreten, erklärt jeweils kurz **Symptom** und **Ursache** und zeigt eine
konkrete **Lösung** als Code- oder Befehlsbeispiel.

Sie müssen die Seite nicht von vorne nach hinten lesen. Suchen Sie einfach die
Fehlermeldung, die auf Ihrem Bildschirm steht (zum Beispiel mit der
Browser-Suche), und springen Sie zum passenden Abschnitt.

:::{seealso} 🎓 Lernziele
:icon: false

Nach der Arbeit mit dieser Seite können Sie …

- … eine Python-Fehlermeldung (*Traceback*) systematisch lesen und die
  entscheidende Zeile finden.
- … die häufigsten Ausnahmen (`SyntaxError`, `NameError`, `TypeError` usw.)
  einordnen und beheben.
- … Probleme mit Dateipfaden und Zeichenkodierung (Encoding) selbstständig
  lösen.
- … Stolperfallen bei CSV-Daten, in JupyterLab, mit Git sowie mit
  pandas/Excel/matplotlib erkennen und umgehen.
- … einschätzen, wann Sie die Musterlösung, das Glossar oder die
  weiterführenden Kapitel zurate ziehen.

:::

:::{note} Wie lese ich diese Seite?
Die Abschnitte sind nach Themen sortiert. Jeder Eintrag folgt dem gleichen
Muster: *Symptom* → *Ursache* → *Lösung*. Codeblöcke sind reine Beispiele und
werden auf dieser Seite **nicht** ausgeführt.
:::

## 1. Python-Grundlagen

### 1.1 Den Traceback lesen

**Symptom:** Ein roter Fehlerblock, der auf den ersten Blick unverständlich
wirkt.

**Ursache:** Python zeigt bei einem Fehler einen *Traceback*: die Kette der
Aufrufe bis zur fehlerhaften Stelle.

**Lösung:** Lesen Sie von **unten nach oben**:

1. Die **letzte Zeile** nennt Fehlertyp und Beschreibung, z. B.
   `ValueError: invalid literal for int() with base 10: 'abc'`.
2. Die Zeile darüber zeigt **Datei und Zeilennummer** des eigentlichen Fehlers.
3. Darüber steht der Code-Ausschnitt (`----> 3 ...`), an dem es knallt.

```text
Traceback (most recent call last):
  File "rechner.py", line 5, in <module>
    zahl = int(eingabe)
ValueError: invalid literal for int() with base 10: 'abc'
```

Hier liegt der Fehler in `rechner.py`, Zeile 5: `'abc'` lässt sich nicht in
eine ganze Zahl umwandeln.

### 1.2 `SyntaxError`

**Symptom:**

```text
SyntaxError: invalid syntax
```

**Ursache:** Der Code verstößt gegen die Regeln der Sprache – z. B. fehlender
Doppelpunkt, nicht geschlossene Klammer oder ein `=` statt `==` im Vergleich.

**Lösung:** Die gemeldete Zeile (und oft die Zeile **davor**) prüfen. Häufige
Fälle:

```python
# Falsch: fehlender Doppelpunkt
if x > 3
    print("groß")

# Richtig
if x > 3:
    print("groß")
```

```python
# Falsch: Zuweisung statt Vergleich
if x = 3:

# Richtig
if x == 3:
```

### 1.3 `IndentationError`

**Symptom:**

```text
IndentationError: unexpected indent
# oder
IndentationError: expected an indented block
```

**Ursache:** Einrückung ist inkonsistent – z. B. Tabs und Leerzeichen gemischt
oder ein Block nach `if`/`for`/`def` wurde nicht eingerückt.

**Lösung:** Pro Ebene **genau 4 Leerzeichen** verwenden, niemals Tabs. In
JupyterLab über *Edit → Indent/Outdent* oder automatische Einrückung arbeiten.

```python
# Falsch
for i in range(3):
print(i)

# Richtig
for i in range(3):
    print(i)
```

### 1.4 `NameError`

**Symptom:**

```text
NameError: name 'summe' is not defined
```

**Ursache:** Eine Variable oder Funktion wird verwendet, bevor sie definiert
wurde – oft wegen Tippfehler, Groß-/Kleinschreibung oder weil eine Zelle noch
nicht ausgeführt wurde.

**Lösung:** Schreibweise prüfen und sicherstellen, dass die Definitionszeile
zuerst läuft.

```python
summe = 0
for i in range(3):
    summe += i
print(summe)      # 3
```

::: {note}
In JupyterLab müssen Zellen **in der richtigen Reihenfolge** ausgeführt werden.
Zeigt das Kürzel links der Zelle `[ ]` oder eine hohe Zahl, wurde sie noch
nicht bzw. zuletzt ausgeführt.
:::

### 1.5 `TypeError`

**Symptom:**

```text
TypeError: can only concatenate str (not "int") to str
```

**Ursache:** Operationen werden auf inkompatible Datentypen angewendet – z. B.
Text und Zahl addieren.

**Lösung:** Typen mit `type()` prüfen und bei Bedarf umwandeln
(`str()`, `int()`, `float()`) oder f-Strings nutzen.

```python
alter = 25
# Falsch
print("Alter: " + alter)

# Richtig
print("Alter: " + str(alter))
print(f"Alter: {alter}")
```

### 1.6 `ValueError`

**Symptom:**

```text
ValueError: invalid literal for int() with base 10: 'zwölf'
```

**Ursache:** Der Datentyp passt, aber der *Inhalt* lässt sich nicht umwandeln
(`int("zwölf")`) oder ein Wert liegt außerhalb des erlaubten Bereichs (z. B.
`int("1.5")`).

**Lösung:** Eingaben prüfen bzw. schrittweise umwandeln:

```python
eingabe = "1.5"

# Falsch
# zahl = int(eingabe)

# Richtig: erst als Kommazahl, dann ggf. runden
zahl = int(float(eingabe))       # 1
```

Für unsichere Eingaben eignet sich `try`/`except`:

```python
try:
    zahl = int(eingabe)
except ValueError:
    print(f"'{eingabe}' ist keine ganze Zahl.")
```

### 1.7 `KeyError` und `IndexError`

**Symptom:**

```text
KeyError: 'Autor'
IndexError: list index out of range
```

**Ursache:** Bei einem Dictionary gibt es den Schlüssel nicht (`KeyError`),
bei einer Liste/Zeichenkette den Index nicht (`IndexError`). Denken Sie daran:
Indizes beginnen bei **0**.

**Lösung:** Schlüssel mit `in` prüfen bzw. `.get()` verwenden; Index gegen die
Länge absichern.

```python
person = {"titel": "Faust"}

# Falsch
# print(person["autor"])

# Richtig
print(person.get("autor", "unbekannt"))   # unbekannt

werte = [10, 20, 30]
# Richtig: nur gültige Indizes 0..2
print(werte[0])                           # 10
if len(werte) > 3:
    print(werte[3])
```

### 1.8 `ModuleNotFoundError`

**Symptom:**

```text
ModuleNotFoundError: No module named 'pandas'
```

**Ursache:** Die Bibliothek ist im aktuellen Python-Environment nicht
installiert – oder Sie sprechen den falschen Kernel an.

**Lösung:** Paket installieren bzw. Kernel prüfen:

```bash
# Lokal mit uv (siehe pyproject.toml)
uv add pandas
uv sync

# Alternativ mit pip im aktiven Environment
pip install pandas
```

In JupyterLab unter *Kernel → Change Kernel* sicherstellen, dass der Kernel zum
Environment passt, in dem das Paket installiert wurde.

## 2. Dateien & Zeichenkodierung

### 2.1 `FileNotFoundError`

**Symptom:**

```text
FileNotFoundError: [Errno 2] No such file or directory: 'daten.csv'
```

**Ursache:** Der Pfad stimmt nicht – falscher Ordnername, Tippfehler oder die
Datei liegt relativ zum **aktuellen Arbeitsverzeichnis** woanders.

**Lösung:** Zuerst prüfen, wo das Programm läuft und wie der Pfad lautet:

```python
from pathlib import Path

print(Path.cwd())              # aktuelles Arbeitsverzeichnis
print(Path("daten.csv").exists())
```

Dann entweder den Pfad korrigieren oder die Datei in den erwarteten Ordner
legen. Verwenden Sie nach Möglichkeit `pathlib`:

```python
from pathlib import Path

pfad = Path("..") / "assets" / "data" / "daten.csv"
with pfad.open(encoding="utf-8") as datei:
    inhalt = datei.read()
```

### 2.2 `UnicodeDecodeError`

**Symptom:**

```text
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xfc in position 12
```

**Ursache:** Die Datei ist nicht UTF-8-kodiert (z. B. Windows-1252, „Latin-1“)
oder umgekehrt. Python vermutet UTF-8.

**Lösung:** Das passende Encoding explizit angeben:

```python
# Windows-Exporte sind oft in cp1252 / latin-1
with open("daten.csv", encoding="cp1252") as datei:
    for zeile in datei:
        print(zeile, end="")
```

Bevorzugt Dateien als UTF-8 (ohne BOM) speichern. In Excel: *Speichern unter →
CSV UTF-8*.

### 2.3 Relative vs. absolute Pfade

**Symptom:** Derselbe Code funktioniert je nach Startordner mal und mal nicht.

**Ursache:** Relative Pfade werden vom **aktuellen Arbeitsverzeichnis** aus
gesucht, nicht vom Speicherort der Skriptdatei.

**Lösung:** Absolute Pfade oder `pathlib` mit Bezug zur Skriptdatei nutzen:

```python
from pathlib import Path

# Absoluter Pfad
pfad = Path("/Users/name/Selbstlernkurs_Python/assets/data/daten.csv")

# Relativ zum Skriptstandort (robust)
basis = Path(__file__).parent
pfad = basis / "data" / "daten.csv"
```

### 2.4 Dateien sauber schließen: `with open(...)`

**Symptom:** Datei bleibt gesperrt, Änderungen sind nicht sichtbar, oder es
gehen Daten verloren.

**Ursache:** Eine Datei wurde geöffnet, aber nie geschlossen.

**Lösung:** Immer den Kontextmanager `with` verwenden – er schließt die Datei
automatisch, auch bei Fehlern:

```python
# Gut
with open("ausgabe.txt", "w", encoding="utf-8") as datei:
    datei.write("Hallo\n")
# Datei ist hier bereits geschlossen und gespeichert
```

### 2.5 CSV mit `newline=""` öffnen

**Symptom:** Beim Schreiben von CSV entstehen leere Zeilen zwischen den
Datensätzen.

**Ursache:** Auf Windows übersetzt `open` Zeilenumbrüche, das `csv`-Modul
schreibt aber bereits eigene – es kommt zu doppelten Umbrüchen.

**Lösung:** Beim CSV-Schreiben `newline=""` setzen:

```python
import csv

with open("ausgabe.csv", "w", encoding="utf-8", newline="") as datei:
    schreiber = csv.writer(datei)
    schreiber.writerow(["Titel", "Jahr"])
    schreiber.writerow(["Faust", 1808])
```

## 3. CSV & Daten

### 3.1 Falsches Trennzeichen oder Anführungszeichen

**Symptom:** Alle Werte landen in einer einzigen Spalte, oder Einträge mit
Komma zerreißen die Zeile.

**Ursache:** Die Datei nutzt ein anderes Trennzeichen (z. B. `;` oder Tabulator)
oder ein anderes Quote-Zeichen als angenommen.

**Lösung:** `delimiter` und `quotechar` explizit angeben:

```python
import csv

with open("daten.csv", encoding="utf-8", newline="") as datei:
    leser = csv.DictReader(datei, delimiter=";", quotechar='"')
    for zeile in leser:
        print(zeile)
```

Im Zweifel die ersten Zeilen mit einem Texteditor betrachten – so erkennen Sie
Trennzeichen und Kodierung direkt.

### 3.2 Fehlerhafte oder unvollständige Zeilen

**Symptom:** `csv.Error: line contains NUL` oder eine Zeile hat zu wenige
Felder.

**Ursache:** Beschädigte Exporte, eingebettete Zeilenumbrüche oder manuell
geänderte Zeilen.

**Lösung:** Zeilen defensiv verarbeiten und fehlerhafte überspringen:

```python
import csv

with open("daten.csv", encoding="utf-8", newline="") as datei:
    leser = csv.reader(datei)
    kopf = next(leser)                     # Kopfzeile
    for nummer, zeile in enumerate(leser, start=2):
        if len(zeile) != len(kopf):
            print(f"Zeile {nummer} übersprungen: {zeile}")
            continue
        # ... weiterverarbeiten
```

### 3.3 Typkonvertierung

**Symptom:** Sortieren liefert unsinnige Reihenfolgen (`"10"` vor `"2"`),
Rechnen mit Zahlen schlägt fehl.

**Ursache:** Aus CSV gelesene Werte sind **immer** Zeichenketten (`str`).

**Lösung:** Beim Einlesen gezielt konvertieren und Fehler abfangen:

```python
def als_zahl(wert, standard=0):
    wert = wert.strip().replace(",", ".")
    try:
        return int(wert)
    except ValueError:
        try:
            return float(wert)
        except ValueError:
            return standard
```

### 3.4 Leere Werte

**Symptom:** `ValueError` bei der Umwandlung oder falsche Summen.

**Ursache:** Fehlende Felder im CSV sind leer (`""`), nicht `0`.

**Lösung:** Leere Werte vor der Konvertierung prüfen:

```python
for zeile in leser:
    roh = zeile["jahr"]
    jahr = int(roh) if roh.strip() else None
```

## 4. Jupyter / JupyterHub / JupyterLab

### 4.1 Kernel startet nicht

**Symptom:** Dauerhaft „Kernel starting, please wait …“ oder ein toter Kernel.

**Ursache:** Überlasteter Server (JupyterHub), fehlgeschlagene Installation
oder verwaister Prozess.

**Lösung:**

1. *Kernel → Restart Kernel* ausprobieren.
2. *Kernel → Shut Down Kernel*, dann Seite neu laden.
3. Bei JupyterHub: Abmelden und neu anmelden; hilft das nicht, den Support
   informieren.
4. Lokal: Terminal prüfen, JupyterLab neu starten.

### 4.2 Zelle hängt (läuft „ewig“)

**Symptom:** Vor der Zelle steht `[*]` und es passiert nichts.

**Ursache:** Endlosschleife, sehr große Datenmenge oder eine auf Eingabe
wartende Funktion.

**Lösung:** Zelle über den ■-Button (Interrupt) abbrechen. Ursache im Code
suchen – bei Schleifen prüfen, ob sich die Abbruchbedingung wirklich ändert:

```python
# Falsch: i wird nie verändert -> Endlosschleife
i = 0
while i < 10:
    print(i)

# Richtig
i = 0
while i < 10:
    print(i)
    i += 1
```

### 4.3 Datei wird im Notebook „nicht gefunden“

**Symptom:** `FileNotFoundError`, obwohl die Datei im Dateibrowser sichtbar ist.

**Ursache:** Der relative Pfad bezieht sich auf den Ordner des Notebooks, nicht
auf das Wurzelverzeichnis.

**Lösung:** Im Notebook den aktuellen Ordner anzeigen und den Pfad anpassen:

```python
from pathlib import Path

print(Path.cwd())
# Bei Daten im Ordner "assets/data" zwei Ebenen über dem Projekt-Unterordner:
pfad = Path("..") / "assets" / "data" / "daten.csv"
```

### 4.4 Notebook wurde nicht gespeichert

**Symptom:** Nach dem Neuladen fehlen Änderungen.

**Ursache:** Autosave ist nicht immer aktiv, oder der Browser-Tab wurde vor dem
Speichern geschlossen.

**Lösung:** Regelmäßig `Strg`/`Cmd` + `S` drücken. Ein Sternchen `*` bzw. ein
Punkt im Tab-Titel zeigt ungespeicherte Änderungen an. Vor längeren Pausen
zusätzlich committen (siehe Abschnitt 5).

### 4.5 Orientierung im Dateibrowser

**Symptom:** Dateien scheinen „verschwunden“ zu sein.

**Ursache:** Der Dateibrowser zeigt den aktuellen Ordner; Dateien außerhalb
werden nicht angezeigt.

**Lösung:** Pfadzeile über dem Browser beachten, mit dem Haus-Symbol zum
Stammordner zurückkehren und Dateinamen inklusive Endung prüfen. Versteckte
Dateien (z. B. `.gitignore`) beginnen mit einem Punkt.

## 5. Git & Versionskontrolle

Eine ausführliche Einführung bietet das Kapitel
[Git im Kurs nutzen](../050-Exkurs_Git/050-Git_im_Kurs.md); Rückgängig-Techniken
finden Sie in der [Vertiefung](../095-Exkurs_Git_Vertiefung/040-Rueckgaengig_machen.md).

### 5.1 Falscher Commit (noch nicht gepusht)

**Symptom:** Die letzte Commit-Message ist falsch oder eine Datei wurde
vergessen.

**Ursache:** Zu früh committet.

**Lösung:** Solange der Commit **nicht gepusht** wurde, korrigieren:

```bash
# Message ändern
git commit --amend -m "Korrigierte Nachricht"

# Vergessene Datei ergänzen
git add vergessene_datei.py
git commit --amend --no-edit
```

::: {warning}
`--amend` verändert die Historie. **Niemals** bei bereits gepushten Commits
verwenden – das führt bei anderen zu Problemen.
:::

### 5.2 Versehentlich committete Dateien

**Symptom:** Eine große oder vertrauliche Datei ist im Repository.

**Ursache:** `git add .` hat alle Dateien erfasst.

**Lösung:** Datei aus der Versionierung nehmen (im Arbeitsverzeichnis bleibt
sie erhalten):

```bash
git rm --cached grosse_datei.zip
git commit -m "Große Datei aus der Versionierung entfernt"
```

Anschließend in `.gitignore` aufnehmen (siehe 5.3). Bereits gepushte,
vertrauliche Daten müssen zusätzlich rotiert werden – die Historie bleibt
sonst erhalten.

### 5.3 `.gitignore`

**Symptom:** Temporäre Dateien, Caches oder Zugangsdaten tauchen ständig in
`git status` auf.

**Ursache:** Es fehlt eine Ignorier-Datei.

**Lösung:** Eine `.gitignore` im Projektwurzelverzeichnis anlegen:

```gitignore
# Python
__pycache__/
*.py[cod]
.venv/
.ipynb_checkpoints/

# Jupyter
*.ipynb~

# Zugangsdaten
.env
*.key
```

### 5.4 Merge-Konflikte

**Symptom:**

```text
CONFLICT (content): Merge conflict in daten.csv
```

**Ursache:** Zwei Branches haben dieselbe Stelle unterschiedlich verändert.

**Lösung:** Konfliktmarkierungen im Editor auflösen, dann committen:

```text
<<<<<<< HEAD
meine Version
=======
andere Version
>>>>>>> feature-branch
```

```bash
# Nach dem Bearbeiten:
git add daten.csv
git commit -m "Merge-Konflikt aufgelöst"
```

Mehr dazu im Kapitel
[Merge-Konflikte](../095-Exkurs_Git_Vertiefung/030-Merge_Konflikte.md).

### 5.5 Passwörter und Secrets

**Symptom:** Zugangsdaten stehen im Klartext im Repository.

**Ursache:** Eine Konfigurationsdatei mit Token oder Passwort wurde committet.

**Lösung:** Secrets niemals committen. Stattdessen eine `.env`-Datei (in
`.gitignore`) oder Umgebungsvariablen nutzen:

```python
import os

token = os.environ["MEIN_TOKEN"]
```

Falls bereits committet: Secret **sofort ändern/rotieren** und aus der
Versionierung entfernen.

## 6. pandas, Excel & matplotlib

Grundlagen zu diesem Abschnitt finden Sie im
[Projekt Excel](../090-Projekt_Excel/000-Einleitung.md).

### 6.1 `read_excel` liefert falsche Datentypen

**Symptom:** Zahlen werden als Text erkannt, Datumswerte als `object`,
Berechnungen schlagen fehl.

**Ursache:** Excel speichert gemischte Zellinhalte; pandas errät den Typ.

**Lösung:** Typen beim Einlesen oder danach explizit setzen:

```python
import pandas as pd

df = pd.read_excel(
    "../assets/data/bibliothek.xlsx",
    sheet_name="Ausleihen",
    dtype={"Jahr": "Int64"},          # nullable Ganzzahl
    parse_dates=["Ausleihdatum"],
)

# Oder nachträglich konvertieren
df["Jahr"] = pd.to_numeric(df["Jahr"], errors="coerce")
```

| Symptom | Ursache | Lösung |
| --- | --- | --- |
| Zahl als Text | Leerzeichen/Comma | `str.strip()`, `str.replace(",", ".")` |
| Datum als Text | Nicht erkannt | `parse_dates=["Spalte"]` |
| Gemischte Typen | Uneinheitliche Zellen | `pd.to_numeric(..., errors="coerce")` |

### 6.2 Fehlende Werte

**Symptom:** `NaN` in Summen, Diagramme mit Lücken, unerwartete Ergebnisse.

**Ursache:** Leere Zellen werden in pandas zu `NaN` (Not a Number).

**Lösung:** Fehlende Werte sichtbar machen und bewusst behandeln:

```python
print(df.isna().sum())              # pro Spalte zählen

df = df.dropna(subset=["Titel"])    # Zeilen ohne Titel entfernen
df["Jahr"] = df["Jahr"].fillna(0)   # oder ersetzen
```

### 6.3 `SettingWithCopyWarning`

**Symptom:**

```text
SettingWithCopyWarning: A value is trying to be set on a copy of a DataFrame ...
```

**Ursache:** Eine Änderung wird auf einer Teilmenge (Slice) ausgeführt, deren
Verhältnis zum Original unklar ist.

**Lösung:** Mit `.copy()` eine eigenständige Kopie erzeugen:

```python
# Warnung auslösend
teil = df[df["Jahr"] > 2000]
teil["Neu"] = 1

# Sauber
teil = df[df["Jahr"] > 2000].copy()
teil["Neu"] = 1
```

### 6.4 Fehlende Spalten oder Backends

**Symptom:**

```text
KeyError: 'Standort'
ModuleNotFoundError: No module named 'openpyxl'
ImportError: No module named 'matplotlib'
```

**Ursache:** Spaltenname weicht ab (Groß-/Kleinschreibung, Leerzeichen), oder
das Paket für Excel bzw. Plots fehlt.

**Lösung:** Spaltennamen prüfen und Pakete installieren:

```python
print(df.columns.tolist())          # exakte Namen anzeigen
df.columns = df.columns.str.strip() # Leerzeichen entfernen
```

```bash
uv add openpyxl matplotlib
uv sync
```

Für Plots zusätzlich ein Backend wählen; in JupyterLab genügt meist:

```python
import matplotlib.pyplot as plt
%matplotlib inline
```

:::{seealso} Referenzen und weiterführende Seiten
- [Cheatsheet](../900-Cheatsheet.md) – kompakte Sprachreferenz zum Nachschlagen.
- [Verzeichnisse & Glossar](Verzeichnisse.md) – Begriffe wie *DataFrame*,
  *Traceback* oder *Repository* nachschlagen.
- [Git im Kurs nutzen](../050-Exkurs_Git/050-Git_im_Kurs.md) – Kurs-Workflow,
  `.gitignore` und Sicherheits-Checkliste.
- [Projekt CSV I](../040-Projekt_CSV_I/000-Einleitung.md) – Dateien öffnen,
  Encoding und CSV manuell einlesen.
- [Projekt Excel](../090-Projekt_Excel/000-Einleitung.md) – pandas,
  Datenbereinigung und matplotlib.
- [Änderungen rückgängig machen](../095-Exkurs_Git_Vertiefung/040-Rueckgaengig_machen.md)
  – `restore`, `revert`, `reset` im Vergleich.
:::
