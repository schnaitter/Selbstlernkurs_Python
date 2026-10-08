---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Cheatsheet

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

```{danger} Einrückung

Python-Code muss korrekt eingerückt sein. Es sollten pro Einrückungsebene genau
4 Leerzeichen genutzt werden.

```

## Variablen

```python
name = "Alice"
alter = 25
ist_student = True
gehalt = 3500.50

# Mehrere Zuweisungen
x, y, z = 1, 2, 3
a = b = c = 0

_a = "Unterstrich am Anfang"
a3 = "Zahlen sind möglich, wenn nicht erstes Zeichen im Namen"
```

## Literale (Literal Values)

Literale sind Werte im Code, die Sie während dem Schreiben des Codes festlegen.

```python
# Zahlen-Literale
42                    # int
3.14                  # float

# String-Literale
"Hallo"               # str
'Welt'                # str

# Boolesche Literale
True                  # bool
False                 # bool

# None - repräsentiert "kein Wert" oder "nicht vorhanden"
# Dies ist eine explizite Definition als "kein Wert" und nicht das Fehlen eines
# Wertes!
None                  # NoneType

# Beispiele für None
def keine_rückgabe():
    print("Tut etwas")
    # Kein return Statement, gibt implizit None zurück

ergebnis = keine_rückgabe()  # ergebnis ist None

# None in Bedingungen
# Tests für `None` sollten immer mit  `is` und nicht mit `==` durchgeführt werden.
if ergebnis is None:
    print("Kein Ergebnis vorhanden")
```

## Zahlen

### `int()`

```python
ganzzahl = 42
ganzzahl = int(42)
von_string = int("123")
von_float = int(3.14)                  # Ergebnis: 3
riesige_zahl = 1234567890987654321
lesbare_zahleneingabe = 4_294_967_296  # 4294967296
```

### `float()`

```python
kommazahl = 3.14
kommazahl = float(3.14)
von_string = float("2.5")
von_int = float(42)       # Ergebnis: 42.0
```

## Zeichenketten (`str()`)

```python
text = "Hallo Welt"
zahl_zu_string = str(42)            # "42"
verkettung = "Hallo" + " " + "Welt" # "Hallo Welt"
wiederholung = "Ha" * 3             # "HaHaHa"
laenge = len("Python")              # 6
grossbuchstaben = "python".upper()  # "PYTHON"
kleinbuchstaben = "PYTHON".lower()  # "python"

# Escape-Sequenzen
text = "Wie geht's?"
text = 'Wie geht\'s?'
erzählung = "Sie sagt: \"So geht das!\""
neue_zeile = "Zeile 1\nZeile 2"
tabulator = "Text\teingerückt\n\tauch eingerückt"

```

## Besondere Python-Strings

In Python gibt es mehrere String-Varianten, wobei wir in diesem Kurs aktuell
nur sogenannte f-Strings nutzen. Der Buchstabe vor einem String-Literal
signalisiert Python, dass der String anders als "normale" Zeichenketten
verarbeitet werden soll.

### f-String = Formatierte String

```python
# Variablen für die nachfolgenden Beispiele.
name = "Alice"
alter = 25
kontostand = 14

# Variablen in Strings einfügen
print(f"Hallo, ich bin {name}!")                    # Hallo, ich bin Alice!
print(f"Ich bin {name} und {alter} Jahre alt")      # Ich bin Alice und 25 Jahre alt

# Ausdrücke in f-Strings
a = 17
b = 5
print(f"{a} geteilt durch {b} ist {a//b} mit Rest {a%b}.")
# 17 geteilt durch 5 ist 3 mit Rest 2.
```

## Boolesche Werte

```python
wahr   = True
falsch = False

wahr   = True and True
wahr   = True or False

wahr   = not False
falsch = not True

falsch = False or False
falsch = True and False
```

## Arithmetik

```python
addition = 5 + 3             # 8
subtraktion = 10 - 4         # 6
multiplikation = 6 * 7       # 42
multiplikation_float = 6.0*7 # 42.0
division = 15 / 3            # 5.0
ganzzahldivision = 17 // 5   # 3
modulo = 17 % 5              # 2
potenz = 2 ** 3              # 8
```

(cheatsheet-bedingungen)=

## Bedingungen (`if`)

```python
alter = 18

if alter >= 18:
    print("Volljährig")
elif alter >= 16:
    print("Fast volljährig")
else:
    print("Minderjährig")

# Vergleichsoperatoren: ==, !=, <, <=, >, >=
# Logische Operatoren: and, or, not
if alter >= 18 and alter < 65:
    print("Arbeitsfähig")
```

(cheatsheet-schleifen)=

## Schleifen

### `while`

```python
zaehler = 0
while zaehler < 5:
    print(zaehler)
    zaehler += 1

# Mit break und continue
zaehler = 0
while True:
    if zaehler == 3:
        break        # Abbruch der Schleife
    if zaehler == 1:
        zaehler += 1
        continue     # Überspringe den Rest des Codes in der Schleife und starte die nächste Iteration
    print(zaehler)
    zaehler += 1

# Häufiges Pattern: Eingaben bis leer einlesen
numbers = []
while True:
    text = input(">> ")
    if text == "":   # Leere Eingabe beendet die Schleife
        break
    numbers.append(int(text))
# Danach enthält numbers alle eingegebenen Zahlen

# Walrus-Operator := (Assignment Expression)
# Erlaubt Zuweisung in Bedingungen
while result := calculate():
    print(result)  # Schleife läuft, solange calculate() nicht None/0/False zurückgibt

# Äquivalent zu:
result = calculate()
while result:
    print(result)
    result = calculate()
```

### `for`

```python
# Über eine Liste iterieren
fruechte = ["Apfel", "Banane", "Orange"]
for frucht in fruechte:
    print(frucht)

# Über einen Bereich iterieren
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8, 2):  # 2, 4, 6
    print(i)

# Mit enumerate für Index und Wert
for index, wert in enumerate(fruechte):
    print(f"{index}: {wert}")
```

(cheatsheet-funktionen)=

## Funktionen (`def`)

```python
def begruessung():
    print("Hallo!")

def addiere(a, b):
    return a + b

def quadrat(zahl=1):  # Standardwert
    return zahl ** 2

# Aufrufe
begruessung()
ergebnis = addiere(5, 3)  # 8
wert = quadrat(4)         # 16
standard = quadrat()      # 1
```

## Importieren von Code (`import`)

```python
# Gesamtes Modul importieren
import math
ergebnis = math.sqrt(16)  # 4.0

# Spezifische Funktionen importieren
from math import sqrt, pi
ergebnis = sqrt(25)  # 5.0
kreisflaeche = pi * 5**2

# Modul mit Alias importieren
import datetime as dt
heute = dt.date.today()

# Alles aus einem Modul importieren (nicht empfohlen)
from math import *
```

(cheatsheet-listen)=

## Listen (`list`)

```python
fruechte = ["Apfel", "Banane", "Orange"]
zahlen = [1, 2, 3, 4, 5]
gemischt = ["Text", 42, True, 3.14]

# Zugriff auf Elemente (0-basiert - erstes Element hat Index 0)
erstes = fruechte[0]        # "Apfel" (erstes Element)
zweites = fruechte[1]       # "Banane" (zweites Element)
drittes = fruechte[2]       # "Orange" (drittes Element)
letztes = fruechte[-1]      # "Orange" (letztes Element)
vorletztes = fruechte[-2]   # "Banane" (vorletztes Element)

# Praktisches Beispiel mit Zahlen-Liste
numbers = [10, 20, 30, 40]
op1 = numbers[0]            # 10 (erstes Element)
op2 = numbers[1]            # 20 (zweites Element)

# Länge einer Liste
anzahl = len(fruechte)      # 3

# Elemente hinzufügen
fruechte.append("Mango")    # Am Ende hinzufügen

# Über Liste iterieren
for frucht in fruechte:
    print(frucht)

# Mit Index iterieren
for i, frucht in enumerate(fruechte):
    print(f"{i}: {frucht}")
```

### List Comprehensions (Listen-Ausdrücke)

Eine **List Comprehension** baut in einer Zeile eine neue Liste auf, indem sie
über eine Folge läuft und auf jedes Element einen Ausdruck anwendet.

```python
zahlen = [1, 2, 3, 4, 5]

# Klassisch: leere Liste anlegen und in der Schleife füllen
quadrate = []
for z in zahlen:
    quadrate.append(z ** 2)

# Dasselbe als List Comprehension
quadrate = [z ** 2 for z in zahlen]          # [1, 4, 9, 16, 25]

# Mit Bedingung filtern
gerade = [z for z in zahlen if z % 2 == 0]   # [2, 4]

# Ausdruck und Bedingung kombinieren
gerade_quadrate = [z ** 2 for z in zahlen if z % 2 == 0]  # [4, 16]

# Auf eine Liste von Wörterbüchern anwenden
personen = [{"name": "Alice"}, {"name": "Bob"}]
namen = [p["name"] for p in personen]        # ["Alice", "Bob"]
```

Aufbau: `[ausdruck for element in folge if bedingung]`

- Der `if`-Teil ist optional.
- Das Ergebnis ist immer eine **neue** Liste; die ursprüngliche Folge bleibt unverändert.

In der [manuellen Analyse](#cheatsheet-manuelle-analyse) werden List
Comprehensions genutzt, um eine Spalte aus einer Liste von Wörterbüchern
herauszuziehen, z. B. `[satz["sales"] for satz in daten]`.

(cheatsheet-woerterbuecher)=

## Wörterbücher (`dict`)

```python
person = {
    "name": "Alice",
    "alter": 25,
    "stadt": "Berlin"
}

# Zugriff auf Werte
name = person["name"]           # "Alice"
alter = person.get("alter")     # 25
gehalt = person.get("gehalt", 0) # 0 (Standardwert)

# Werte setzen
person["beruf"] = "Entwicklerin"

# Über Wörterbuch iterieren
for schluessel, wert in person.items():
    print(f"{schluessel}: {wert}")

for schluessel in person.keys():
    print(schluessel)
```

## Nützliche eingebaute Funktionen

### `print()`

```python
print("Hallo Welt")                    # Hallo Welt
print("Name:", "Alice", "Alter:", 25)  # Name: Alice Alter: 25
print("Ergebnis", 42, sep=" -> ")      # Ergebnis -> 42
print("Ende", end="!\n")               # Ende!

# Formatierung
name = "Bob"
alter = 30
print(f"Ich bin {name} und {alter} Jahre alt")


# Zugriff auf Variable ohne Wert
print(nicht_existent)                  # Achtung, wirft `NameError()`
```

(cheatsheet-eingabe)=

### `input()`

```python
text = input("Wie heißen Sie? ")

zahl = float(input("Zahl > "))   # Achtung, kann `ValueError()` "werfen"
```

### `assert` - Überprüfungen im Code

```python
# assert überprüft eine Bedingung und wirft AssertionError bei False
# Ein assert macht eine Annahme über den nachfolgenden Code explizit.
def addiere(a, b):
    return a + b

assert addiere(2, 3) == 5, "Fehler: 2 + 3 sollte 5 sein"
assert addiere(10, 25) == 35, "Fehler: 10 + 25 sollte 35 sein"

# Nützlich für Tests und Debugging
ergebnis = calculate()
assert ergebnis is not None, "Berechnung gab None zurück"
assert ergebnis > 0, f"Ergebnis sollte positiv sein, war aber {ergebnis}"
```

### `help()` - Dokumentation anzeigen

```python
# Zeigt Dokumentation zu Funktionen, Modulen, etc.
help(print)
help(len)
help(str.upper)

# Für eigene Funktionen mit docstrings
def meine_funktion():
    """Diese Funktion macht etwas Tolles."""
    pass

help(meine_funktion)  # Zeigt "Diese Funktion macht etwas Tolles."
```

(cheatsheet-dateien)=

## Dateien lesen und schreiben

```python
# Datei lesen
with open("datei.txt", "r") as f:
    inhalt = f.read()           # Gesamten Inhalt lesen

with open("datei.txt", "r") as f:
    zeilen = f.readlines()      # Alle Zeilen als Liste

with open("datei.txt", "r") as f:
    for zeile in f:             # Zeile für Zeile
        print(zeile.strip())

# Datei schreiben
with open("ausgabe.txt", "w") as f:
    f.write("Hallo Welt\n")

# An Datei anhängen
with open("log.txt", "a") as f:
    f.write("Neuer Eintrag\n")
```

(cheatsheet-csv)=

## CSV-Dateien

```python
import csv

# CSV lesen
with open("daten.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    for zeile in reader:
        print(zeile)  # zeile ist eine Liste

# CSV mit Spaltennamen lesen (csv.DictReader)
with open("daten.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    print(reader.fieldnames)      # Liste der Spaltennamen
    for zeile in reader:
        print(zeile["spaltenname"])  # zeile ist ein Wörterbuch

# CSV schreiben
with open("ausgabe.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Name", "Alter", "Stadt"])
    writer.writerow(["Alice", "25", "Berlin"])

# CSV mit Spaltennamen schreiben (csv.DictWriter)
with open("ausgabe.csv", "w", newline="", encoding="utf-8") as f:
    felder = ["Name", "Alter", "Stadt"]
    writer = csv.DictWriter(f, fieldnames=felder, delimiter=";")
    writer.writeheader()  # Kopfzeile schreiben
    writer.writerow({"Name": "Alice", "Alter": 25, "Stadt": "Berlin"})

# Nützliche Parameter
# delimiter=";"           Feldtrenner
# quotechar='"'           Zeichen für Felder, die den Trenner enthalten
# quoting=csv.QUOTE_ALL   Alle Felder in Anführungszeichen setzen
# encoding="utf-8"        Zeichenkodierung (z. B. auch "latin-1")
```

(cheatsheet-manuelle-analyse)=

## Manuelle Analyse (Listen, Dictionaries, `collections`)

Ohne `pandas` lassen sich tabellarische Daten "von Hand" auswerten: Jede Zeile
wird ein Wörterbuch, die Gesamtheit eine Liste von Wörterbüchern – genau die
Form, die `csv.DictReader` liefert.

```python
from collections import Counter, defaultdict

# Liste von Dictionaries (typisch für csv.DictReader)
zeilen = [
    {"titel": "Buch A", "jahr": "2020", "verlag": "Muster"},
    {"titel": "Buch B", "jahr": "2021", "verlag": "Muster"},
    {"titel": "Buch C", "jahr": "2020", "verlag": "Beispiel"},
]

# Umfang und Spalten ermitteln
anzahl_zeilen = len(zeilen)
spalten = list(zeilen[0].keys())

# Werte auslesen (get() mit Standardwert, falls Spalte fehlt)
titel = [z.get("titel", "unbekannt") for z in zeilen]

# Zählen mit Counter
jahr_zaehler = Counter(z["jahr"] for z in zeilen)
print(jahr_zaehler)                  # Counter({'2020': 2, '2021': 1})
print(jahr_zaehler["2020"])          # 2
print(jahr_zaehler.most_common(1))   # [('2020', 2)]

# Gruppieren mit defaultdict
nach_verlag = defaultdict(list)
for z in zeilen:
    nach_verlag[z["verlag"]].append(z["titel"])
print(dict(nach_verlag))

# Sortieren (ohne die Originaldaten zu verändern)
nach_jahr = sorted(zeilen, key=lambda z: z["jahr"])

# Numerische Spalten umwandeln und aufsummieren
jahre = [int(z["jahr"]) for z in zeilen]
print(sum(jahre) / len(jahre))       # Mittelwert
```

(cheatsheet-pandas)=

## Pandas (tabellarische Daten)

`pandas` ist eine Bibliothek für die Verarbeitung tabellarischer Daten. Die
wichtigste Struktur ist der **DataFrame** – vergleichbar mit einem Excel-Blatt
oder einer Tabelle in einer Datenbank.

```python
import pandas as pd

# CSV/Excel einlesen
df = pd.read_csv("daten.csv", delimiter=";", encoding="utf-8")
df = pd.read_excel("daten.xlsx", sheet_name="Tabelle1")

# Erste/letzte Zeilen ansehen
df.head()      # erste 5 Zeilen
df.tail(3)     # letzte 3 Zeilen

# Struktur und Kennzahlen
df.info()          # Spalten, Datentypen, fehlende Werte
df.shape           # (Zeilen, Spalten)
df.columns         # Spaltennamen
df.dtypes          # Datentypen je Spalte

# Beschreibende Statistik
df.describe()                      # Statistik numerischer Spalten
df["jahr"].value_counts()          # Häufigkeiten einer Spalte
df["jahr"].mean()                  # Mittelwert
df["jahr"].unique()                # verschiedene Werte

# Auswählen und filtern
df["titel"]                        # eine Spalte (Series)
df[["titel", "jahr"]]              # mehrere Spalten
df[df["jahr"] > 2020]              # Zeilen filtern

# Gruppieren und aggregieren
df.groupby("verlag")["jahr"].mean()
df.groupby("verlag").size()        # Anzahl je Gruppe

# Fehlende Werte
df.isna().sum()
df = df.dropna()                   # Zeilen mit fehlenden Werten entfernen
df["jahr"] = df["jahr"].fillna(0)

# Neue Spalte berechnen
df["jahrzehnt"] = (df["jahr"] // 10) * 10

# Speichern
df.to_csv("ergebnis.csv", index=False)
df.to_excel("ergebnis.xlsx", index=False)
```

(cheatsheet-matplotlib)=

## Matplotlib (Visualisierung)

`matplotlib` erzeugt Diagramme (Balken, Linien, Histogramme). Für tabellarische
Daten wird häufig die `plot`-Methode von `pandas` genutzt.

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("daten.csv", delimiter=";")

# Balkendiagramm aus einer Häufigkeitsverteilung
df["verlag"].value_counts().plot(kind="bar")
plt.title("Titelverteilung je Verlag")
plt.xlabel("Verlag")
plt.ylabel("Anzahl")
plt.tight_layout()
plt.savefig("balken.png")   # vor plt.show() speichern
plt.show()

# Liniendiagramm
df.plot(kind="line", x="jahr", y="bestand", marker="o")

# Histogramm einer Zahlenspalte
df["jahr"].plot(kind="hist", bins=10)

# Direkt über die matplotlib-API (ohne DataFrame)
plt.bar(["A", "B"], [3, 5])
plt.show()
```

(cheatsheet-ausnahmen)=

## Ausnahmebehandlung (`try`/`except`)

```python
try:
    zahl = int(input("Zahl eingeben: "))
    ergebnis = 10 / zahl
    print(ergebnis)
except ValueError:
    print("Das war keine gültige Zahl!")
except ZeroDivisionError:
    print("Division durch Null nicht möglich!")
except Exception as e:
    print(f"Unerwarteter Fehler: {e}")
finally:
    print("Wird immer ausgeführt")
```

## Dokumentation

### Kommentare

```python
kein_kommentar # Kommentar
```

### docstrings

Am Anfang einer Datei, Funktion, Klasse, … kann ein String plaziert werden, welche von der Funktion `help()` für die Dokumentation genutzt wird. Es haben sich verschiedene Formatierungen entwickelt. Hier wird eine vorgestellt.

```python
"""Lend or return media, if within allowed number of media on account.

Parameters:
-----------
account_balance (int): The current balance before the transaction is attempted.
        Valid values: 0 <= x <= 15

number_of_media (int): The number of the media to be lent or returned.
        A positive number signifies lending and a negative Number signifies returning.

Returns:
--------
int: The current account balance.
"""
```

(cheatsheet-skripte)=

## Ausführbare Skripte

### Shebang

Nur die erste Zeile des Skripts kann als Shebang benutzt werden!

```python
#! /usr/bin/env python3
```

### `if __name__ == "__main__":`

```python
wird_immer_ausgeführt = 1 # bspw. beim Importieren
def das_auch():
    print("wird ausgeführt, wenn die Funktion aufgerufen wird")
    ...

if __name__ == "__main__":
    wird_nur_als_skript = "ausgeführt"
    das_auch()
```

### Datei ausführbar machen

In Unix-artigen Betriebssystemen.

```bash
$ chmod +x datei.py
```

## Python Code ausführen

```bash
$ python3 code.py
...
$ python3 -i code.py
...
>>> interaktive_weiterarbeit_möglich = True
```

## Git

### Tägliche Arbeit

```bash
git status              # Status prüfen
git add datei.py        # Datei zur Staging Area hinzufügen
git add .               # Alle Änderungen hinzufügen
git commit -m "Text"    # Commit mit Message erstellen
git push                # Zum Remote hochladen
git pull                # Vom Remote herunterladen
```

### Historie

```bash
git log                 # Commit-Historie anzeigen
git log --oneline       # Kompakte Historie
git log --oneline --graph --all  # Branch-Struktur visualisieren
git diff                # Änderungen im Working Directory
git diff --staged       # Änderungen in der Staging Area
git revert <commit>     # Commit rückgängig machen (neuer Commit)
```

### Branches

```bash
git branch              # Branches anzeigen
git branch <name>       # Branch erstellen
git checkout <name>     # Zu Branch wechseln
git checkout -b <name>  # Branch erstellen + wechseln
git merge <name>        # Branch in aktuellen Branch mergen
git branch -d <name>    # Branch löschen
```

### Remote

```bash
git clone <url>                # Repository herunterladen
git remote -v                  # Remote-Verbindungen anzeigen
git remote add origin <url>    # Remote-Verbindung hinzufügen
git push -u origin main        # Branch erstmalig hochladen
```

### Konfiguration

```bash
git config --global user.name "Ihr Name"
git config --global user.email "ihre.email@example.com"
git config --list              # Aktuelle Einstellungen anzeigen
git --version                  # Installierte Git-Version prüfen
```

### Troubleshooting

```bash
git restore datei.py    # Änderungen verwerfen
git restore --staged .  # Aus der Staging Area entfernen
git status              # Orientierung finden
git merge --abort       # Merge abbrechen
```
