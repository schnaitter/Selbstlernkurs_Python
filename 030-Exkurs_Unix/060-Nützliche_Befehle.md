---
short_title: Nützliche Befehle
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Nützliche Befehle für effizientes Arbeiten

:::::{margin}
::::{tip} Unix-Philosophie in der Praxis

Die Werkzeuge in diesem Kapitel zeigen die Unix-Philosophie in Aktion: Kleine,
spezialisierte Programme, die zusammenarbeiten.

::::
:::::

In diesem Kapitel lernen Sie fortgeschrittene Techniken kennen, die Ihre Arbeit
im Terminal deutlich effizienter machen: Pipes, Ausgabeumleitungen, Wildcards
und Textsuche.

## Pipes: Programme verbinden

Mit Pipes (`|`) leiten Sie die Ausgabe eines Befehls als Eingabe an einen
anderen weiter:

```console
$ befehl1 | befehl2
```

### Beispiel: Sortierte Dateiliste

```console
$ ls -1
zebra.txt
alpha.txt
beta.txt
$ ls -1 | sort
alpha.txt
beta.txt
zebra.txt
```

### Beispiel: Anzahl der Dateien zählen

```console
$ ls | wc -l
42
```

`wc -l` (word count, lines) zählt die Zeilen der Eingabe.

### Beispiel: Die größten Dateien finden

```console
$ ls -lh | sort -k 5 -h | tail -n 5
```

- `ls -lh`: Detaillierte Liste mit lesbaren Größen
- `sort -k 5 -h`: Sortiert nach Spalte 5 (Größe), human-readable
- `tail -n 5`: Zeigt die letzten 5 Zeilen (= größten Dateien)

### Mehrere Pipes kombinieren

```console
$ cat datei.txt | grep "Fehler" | sort | uniq
```

- `cat datei.txt`: Datei ausgeben
- `grep "Fehler"`: Nur Zeilen mit "Fehler"
- `sort`: Sortieren
- `uniq`: Duplikate entfernen

## Ausgabeumleitungen

:::::{margin}
::::{caution} Überschreiben vs. Anhängen

`>` überschreibt die Zieldatei komplett!
`>>` hängt an die bestehende Datei an.

::::
:::::

### Ausgabe in Datei schreiben (`>`)

```console
$ ls > dateiliste.txt
```

Statt auf dem Bildschirm wird die Ausgabe in `dateiliste.txt` geschrieben.

```console
$ echo "Hallo Welt" > hallo.txt
$ cat hallo.txt
Hallo Welt
```

### An Datei anhängen (`>>`)

```console
$ echo "Zeile 1" > datei.txt
$ echo "Zeile 2" >> datei.txt
$ cat datei.txt
Zeile 1
Zeile 2
```

### Eingabe aus Datei lesen (`<`)

```console
$ sort < unsortiert.txt
```

Liest `unsortiert.txt` und sortiert den Inhalt.

### Ausgabe und Fehler trennen

```console
$ befehl > ausgabe.txt 2> fehler.txt
```

- `>` oder `1>`: Normale Ausgabe (stdout)
- `2>`: Fehlerausgabe (stderr)

Beides in eine Datei:

```console
$ befehl > alles.txt 2>&1
```

Oder kürzer (seit bash 4.0):

```console
$ befehl &> alles.txt
```

### Ausgabe verwerfen

```console
$ befehl > /dev/null
```

`/dev/null` ist ein "schwarzes Loch" – alles, was dorthin geschrieben wird,
verschwindet.

## Wildcards (Platzhalter)

:::::{margin}
::::{hint} Globbing

Die Shell expandiert Wildcards automatisch vor der Befehlsausführung. Das nennt
sich "Globbing".

::::
:::::

Wildcards ermöglichen es, mehrere Dateien auf einmal anzusprechen:

### Stern (`*`)

Steht für beliebig viele Zeichen (auch null):

```console
$ ls *.py
main.py  test.py  utils.py
```

```console
$ cp *.txt backup/
```

Kopiert alle `.txt`-Dateien nach `backup/`.

```console
$ rm test*
```

Löscht alle Dateien, die mit "test" beginnen.

### Fragezeichen (`?`)

Steht für **genau ein** Zeichen:

```console
$ ls datei?.txt
datei1.txt  datei2.txt  datei3.txt
```

```console
$ ls datei??.txt
datei01.txt  datei10.txt  datei99.txt
```

### Eckige Klammern (`[]`)

Steht für **ein** Zeichen aus der angegebenen Menge:

```console
$ ls datei[123].txt
datei1.txt  datei2.txt  datei3.txt
```

```console
$ ls datei[0-9].txt
datei0.txt  datei1.txt  ...  datei9.txt
```

```console
$ ls [A-Z]*.py
Main.py  Utils.py
```

### Geschweifte Klammern (`{}`)

Expandiert zu mehreren Varianten:

```console
$ echo {apple,banana,cherry}.txt
apple.txt banana.txt cherry.txt
```

```console
$ mkdir -p projekt/{src,tests,docs}
```

Erstellt drei Verzeichnisse.

```console
$ cp script.py{,.backup}
```

Äquivalent zu: `cp script.py script.py.backup`

## Textsuche mit `grep`

:::::{margin}
::::{note} grep = Global Regular Expression Print

`grep` ist eines der mächtigsten Unix-Werkzeuge. Es nutzt reguläre Ausdrücke
(Regular Expressions) für komplexe Suchmuster.

::::
:::::

Mit `grep` suchen Sie nach Textmustern in Dateien:

### Grundlegende Suche

```console
$ grep "import" main.py
import sys
import csv
```

Zeigt alle Zeilen, die "import" enthalten.

### In mehreren Dateien suchen

```console
$ grep "def" *.py
main.py:def verarbeite(daten):
utils.py:def lese_csv(dateiname):
utils.py:def schreibe_csv(dateiname, daten):
```

### Groß-/Kleinschreibung ignorieren

```console
$ grep -i "fehler" logfile.txt
```

Findet "Fehler", "fehler", "FEHLER", etc.

### Zeilennummern anzeigen

```console
$ grep -n "TODO" *.py
main.py:42:# TODO: Fehlerbehandlung verbessern
utils.py:15:# TODO: Dokumentation schreiben
```

### Rekursiv in Verzeichnissen suchen

```console
$ grep -r "class" src/
```

Sucht in allen Dateien im `src/`-Verzeichnis.

### Nur Dateinamen anzeigen

```console
$ grep -l "import pandas" *.py
data_analysis.py
processing.py
```

### Invertierte Suche

```console
$ grep -v "^#" config.py
```

Zeigt alle Zeilen, die **nicht** mit `#` beginnen (z.B. um Kommentare
auszublenden).

### Mit regulären Ausdrücken

```console
$ grep "^def " *.py
```

Findet Zeilen, die mit "def " beginnen (Funktionsdefinitionen).

```console
$ grep "[0-9]{3,}" datei.txt
```

Findet Zahlen mit mindestens 3 Ziffern.

## Praktische Kombinationen

### Python-Funktionen in einem Projekt finden

```console
$ grep -rn "^def " src/ | head -10
```

Zeigt die ersten 10 Funktionsdefinitionen mit Dateiname und Zeilennummer.

### Log-Dateien nach Fehlern durchsuchen

```console
$ grep -i "error" logfile.txt | tail -20
```

Zeigt die letzten 20 Fehler.

### Häufigste Wörter in einer Datei

```console
$ cat datei.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head -10
```

- `tr ' ' '\n'`: Ersetzt Leerzeichen durch Zeilenumbrüche (ein Wort pro Zeile)
- `sort`: Sortiert
- `uniq -c`: Zählt Duplikate
- `sort -nr`: Sortiert numerisch, absteigend
- `head -10`: Top 10

### Alle Python-Dateien finden und Zeilen zählen

```console
$ find . -name "*.py" -exec wc -l {} + | sort -n
```

- `find . -name "*.py"`: Findet alle `.py`-Dateien
- `-exec wc -l {} +`: Zählt Zeilen
- `sort -n`: Sortiert numerisch

## Weitere nützliche Befehle

### `wc` – Word Count

```console
$ wc datei.txt
  42  315 2048 datei.txt
```

Zeigt: Zeilen, Wörter, Bytes.

Nur Zeilen:

```console
$ wc -l datei.txt
```

### `sort` – Sortieren

```console
$ sort datei.txt
$ sort -r datei.txt      # Rückwärts
$ sort -n zahlen.txt     # Numerisch
```

### `uniq` – Duplikate entfernen

```console
$ sort datei.txt | uniq
$ sort datei.txt | uniq -c    # Mit Anzahl
```

**Wichtig:** `uniq` funktioniert nur auf sortierten Daten!

### `cut` – Spalten extrahieren

```console
$ cut -d',' -f1,3 data.csv
```

Extrahiert Spalten 1 und 3 aus einer CSV-Datei (Trennzeichen: Komma).

### `tr` – Zeichen ersetzen

```console
$ echo "HALLO" | tr 'A-Z' 'a-z'
hallo
```

```console
$ cat datei.txt | tr -d '\r'
```

Entfernt Carriage Returns (Windows-Zeilenenden).

:::::{admonition} 💪 Übung
:icon: false

Gegeben ist eine Datei `kurse.txt` mit folgendem Inhalt:

```
Python Grundlagen
Git Workshop
Python Fortgeschritten
Unix Einführung
Python für Bibliotheken
```

Führen Sie folgende Aufgaben aus (erstellen Sie die Datei zuerst):

1. Zählen Sie die Zeilen in der Datei
2. Finden Sie alle Zeilen, die "Python" enthalten
3. Finden Sie alle Zeilen, die "Python" enthalten (case-insensitive)
4. Schreiben Sie alle Python-Kurse in eine neue Datei `python-kurse.txt`
5. Sortieren Sie die Datei alphabetisch und zeigen Sie das Ergebnis
6. Zählen Sie, wie oft das Wort "Python" vorkommt

:::{dropdown} ✅ Lösung

```console
$ cat > kurse.txt << 'EOF'
Python Grundlagen
Git Workshop
Python Fortgeschritten
Unix Einführung
Python für Bibliotheken
EOF

$ wc -l kurse.txt
5 kurse.txt

$ grep "Python" kurse.txt
Python Grundlagen
Python Fortgeschritten
Python für Bibliotheken

$ grep -i "python" kurse.txt
Python Grundlagen
Python Fortgeschritten
Python für Bibliotheken

$ grep "Python" kurse.txt > python-kurse.txt
$ cat python-kurse.txt
Python Grundlagen
Python Fortgeschritten
Python für Bibliotheken

$ sort kurse.txt
Git Workshop
Python Fortgeschritten
Python Grundlagen
Python für Bibliotheken
Unix Einführung

$ grep -o "Python" kurse.txt | wc -l
3
```

Alternative für Aufgabe 6:

```console
$ grep -c "Python" kurse.txt
3
```

:::
:::::

## Zusammenfassung

| Technik                   | Syntax         | Beispiel                   |
| ------------------------- | -------------- | -------------------------- |
| **Pipe**                  | `cmd1 \| cmd2` | `ls \| sort`               |
| **Umleitung (schreiben)** | `>`            | `echo "text" > datei.txt`  |
| **Umleitung (anhängen)**  | `>>`           | `echo "mehr" >> datei.txt` |
| **Eingabe aus Datei**     | `<`            | `sort < datei.txt`         |
| **Wildcards**             | `*`, `?`, `[]` | `ls *.py`                  |
| **Textsuche**             | `grep`         | `grep "import" *.py`       |
| **Sortieren**             | `sort`         | `sort datei.txt`           |
| **Duplikate entfernen**   | `uniq`         | `sort \| uniq`             |
| **Zeilen/Wörter zählen**  | `wc`           | `wc -l datei.txt`          |

Diese Werkzeuge machen die Unix-Kommandozeile so mächtig. Mit etwas Übung
können Sie komplexe Datenverarbeitungen in einer einzigen Zeile durchführen!
