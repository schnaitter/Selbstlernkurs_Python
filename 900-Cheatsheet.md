---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Cheatsheet

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
## Besondere Python-String

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

## Listen (`list`)

```python
fruechte = ["Apfel", "Banane", "Orange"]
zahlen = [1, 2, 3, 4, 5]
gemischt = ["Text", 42, True, 3.14]

# Zugriff auf Elemente (0-basiert)
erstes = fruechte[0]        # "Apfel"
letztes = fruechte[-1]      # "Orange"

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

### `input()`

```python
text = input("Wie heißen Sie? ")

zahl = float(input("Zahl > ")   # Achtung, kann `ValueError()` "werfen"
```

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

## CSV-Dateien

```python
import csv

# CSV lesen
with open("daten.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    for zeile in reader:
        print(zeile)  # zeile ist eine Liste

# CSV mit Spaltennamen lesen
with open("daten.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=";")
    for zeile in reader:
        print(zeile["spaltenname"])  # zeile ist ein Wörterbuch

# CSV schreiben
with open("ausgabe.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Name", "Alter", "Stadt"])
    writer.writerow(["Alice", "25", "Berlin"])
```

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
