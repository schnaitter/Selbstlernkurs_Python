---
short_title: Übungen
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Praktische Übungen

In diesem Kapitel üben Sie alle gelernten Unix-Befehle in praxisnahen
Szenarien. Die Übungen orientieren sich an typischen Aufgaben in der
Bibliotheks- und Informationspraxis.

## Übung 1: Python-Projektstruktur erstellen

:::::{admonition} 💪 Aufgabe: Bibliotheks-Datenverarbeitungsprojekt
:icon: false

Erstellen Sie eine vollständige Projektstruktur für ein Python-Projekt zur
Verarbeitung von Bibliotheksdaten:

```
bibliotheks-tools/
├── README.md
├── requirements.txt
├── src/
│   ├── katalog.py
│   ├── statistik.py
│   └── export.py
├── data/
│   ├── input/
│   └── output/
├── tests/
│   └── test_katalog.py
└── docs/
    └── anleitung.md
```

**Schritte:**

1. Erstellen Sie die Verzeichnisstruktur mit einem einzigen `mkdir`-Befehl
2. Erstellen Sie alle Dateien mit `touch`
3. Listen Sie die Struktur mit `ls -R` auf
4. Fügen Sie in `README.md` eine Zeile ein: "# Bibliotheks-Tools"
5. Überprüfen Sie mit `cat README.md`

:::{dropdown} ✅ Lösung

```console
$ mkdir -p bibliotheks-tools/{src,data/{input,output},tests,docs}
$ cd bibliotheks-tools
$ touch README.md requirements.txt
$ touch src/katalog.py src/statistik.py src/export.py
$ touch tests/test_katalog.py
$ touch docs/anleitung.md
$ ls -R
.:
data  docs  README.md  requirements.txt  src  tests

./data:
input  output

./data/input:

./data/output:

./docs:
anleitung.md

./src:
export.py  katalog.py  statistik.py

./tests:
test_katalog.py
$ echo "# Bibliotheks-Tools" > README.md
$ cat README.md
# Bibliotheks-Tools
```

:::
:::::

## Übung 2: Ausführbares Datenverarbeitungs-Skript

:::::{admonition} 💪 Aufgabe: CSV-Verarbeitung ausführbar machen
:icon: false

Erstellen Sie ein ausführbares Python-Skript zur Verarbeitung von CSV-Daten:

**Schritte:**

1. Erstellen Sie eine Datei `verarbeite_katalog.py` mit folgendem Inhalt:

    ```python
    #! /usr/bin/env python3

    import csv
    import sys

    def main():
        print("Katalogdaten-Verarbeitung")
        print(f"Python-Version: {sys.version}")
        print("Bereit zur Verarbeitung...")

    if __name__ == "__main__":
        main()
    ```

2. Überprüfen Sie die Dateiberechtigungen
3. Versuchen Sie, das Skript mit `./verarbeite_katalog.py` auszuführen
4. Machen Sie es ausführbar
5. Führen Sie es erneut aus
6. Erstellen Sie eine Backup-Kopie mit dem Namen `verarbeite_katalog.py.backup`

:::{dropdown} ✅ Lösung

```console
$ cat > verarbeite_katalog.py << 'EOF'
#! /usr/bin/env python3

import csv
import sys

def main():
    print("Katalogdaten-Verarbeitung")
    print(f"Python-Version: {sys.version}")
    print("Bereit zur Verarbeitung...")

if __name__ == "__main__":
    main()
EOF
$ ls -l verarbeite_katalog.py
-rw-r--r--  1 user users  234 Okt 17 14:00 verarbeite_katalog.py
$ ./verarbeite_katalog.py
bash: ./verarbeite_katalog.py: Permission denied
$ chmod +x verarbeite_katalog.py
$ ls -l verarbeite_katalog.py
-rwxr-xr-x  1 user users  234 Okt 17 14:00 verarbeite_katalog.py
$ ./verarbeite_katalog.py
Katalogdaten-Verarbeitung
Python-Version: 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0]
Bereit zur Verarbeitung...
$ cp verarbeite_katalog.py verarbeite_katalog.py.backup
$ ls
verarbeite_katalog.py  verarbeite_katalog.py.backup
```

:::
:::::

## Übung 3: Dateien organisieren und filtern

:::::{admonition} 💪 Aufgabe: Metadaten-Dateien sortieren
:icon: false

Sie haben verschiedene Metadaten-Dateien und möchten diese organisieren.

**Vorbereitung:** Erstellen Sie zuerst Testdateien:

```console
$ mkdir metadaten-projekt
$ cd metadaten-projekt
$ touch katalog_2023.xml katalog_2024.xml katalog_2025.xml
$ touch statistik_2023.csv statistik_2024.csv
$ touch export_alt.txt export_neu.txt
$ touch README.md dokumentation.md
```

**Aufgaben:**

1. Listen Sie nur die XML-Dateien auf
2. Listen Sie nur die Dateien aus 2024 auf
3. Verschieben Sie alle XML-Dateien in ein Unterverzeichnis `xml/`
4. Verschieben Sie alle CSV-Dateien in ein Unterverzeichnis `csv/`
5. Löschen Sie alle Dateien, die "alt" im Namen haben
6. Zählen Sie, wie viele Dateien übrig sind

:::{dropdown} ✅ Lösung

```console
$ ls *.xml
katalog_2023.xml  katalog_2024.xml  katalog_2025.xml
$ ls *2024*
katalog_2024.xml  statistik_2024.csv
$ mkdir xml
$ mv *.xml xml/
$ mkdir csv
$ mv *.csv csv/
$ rm *alt*
$ ls
csv  dokumentation.md  export_neu.txt  README.md  xml
$ find . -type f | wc -l
6
```

Erklärung: 3 XML + 2 CSV + 1 export_neu.txt + 2 Markdown = 8 Dateien insgesamt,
aber `ls` zählt nur die 4 sichtbaren im Hauptverzeichnis.

Mit `find` finden wir alle Dateien (inkl. Unterverzeichnisse):

```console
$ find . -type f
./xml/katalog_2023.xml
./xml/katalog_2024.xml
./xml/katalog_2025.xml
./csv/statistik_2023.csv
./csv/statistik_2024.csv
./export_neu.txt
./README.md
./dokumentation.md
```

:::
:::::

## Übung 4: Log-Dateien analysieren

:::::{admonition} 💪 Aufgabe: Bibliothekssystem-Logs auswerten
:icon: false

Erstellen Sie eine Beispiel-Log-Datei und analysieren Sie diese:

**Vorbereitung:**

```console
$ cat > system.log << 'EOF'
2025-10-17 10:00:01 INFO Nutzer alice hat sich angemeldet
2025-10-17 10:05:23 INFO Suche nach "Python"
2025-10-17 10:08:45 WARNING Langsame Datenbankabfrage (3.2s)
2025-10-17 10:12:10 INFO Nutzer bob hat sich angemeldet
2025-10-17 10:15:33 ERROR Verbindung zur Datenbank fehlgeschlagen
2025-10-17 10:16:01 INFO Verbindung wiederhergestellt
2025-10-17 10:20:45 INFO Suche nach "Bibliothek"
2025-10-17 10:25:12 ERROR Datei nicht gefunden: katalog.xml
2025-10-17 10:30:00 WARNING Arbeitsspeicher bei 85%
2025-10-17 10:35:15 INFO Nutzer alice hat sich abgemeldet
EOF
```

**Aufgaben:**

1. Zeigen Sie nur die Zeilen mit ERROR
2. Zeigen Sie nur die Zeilen mit ERROR oder WARNING
3. Zählen Sie, wie viele ERROR-Meldungen es gibt
4. Speichern Sie alle ERROR-Meldungen in einer Datei `errors.log`
5. Zeigen Sie die letzten 3 Log-Einträge
6. Finden Sie alle Zeilen, in denen Nutzer\*innen erwähnt werden
7. Erstellen Sie eine Liste aller Nutzer\*innen (alice, bob)

:::{dropdown} ✅ Lösung

```console
$ grep "ERROR" system.log
2025-10-17 10:15:33 ERROR Verbindung zur Datenbank fehlgeschlagen
2025-10-17 10:25:12 ERROR Datei nicht gefunden: katalog.xml

$ grep -E "ERROR|WARNING" system.log
2025-10-17 10:08:45 WARNING Langsame Datenbankabfrage (3.2s)
2025-10-17 10:15:33 ERROR Verbindung zur Datenbank fehlgeschlagen
2025-10-17 10:25:12 ERROR Datei nicht gefunden: katalog.xml
2025-10-17 10:30:00 WARNING Arbeitsspeicher bei 85%

$ grep -c "ERROR" system.log
2

$ grep "ERROR" system.log > errors.log
$ cat errors.log
2025-10-17 10:15:33 ERROR Verbindung zur Datenbank fehlgeschlagen
2025-10-17 10:25:12 ERROR Datei nicht gefunden: katalog.xml

$ tail -n 3 system.log
2025-10-17 10:30:00 WARNING Arbeitsspeicher bei 85%
2025-10-17 10:35:15 INFO Nutzer alice hat sich abgemeldet

$ grep "Nutzer" system.log
2025-10-17 10:00:01 INFO Nutzer alice hat sich angemeldet
2025-10-17 10:12:10 INFO Nutzer bob hat sich angemeldet
2025-10-17 10:35:15 INFO Nutzer alice hat sich abgemeldet

$ grep "Nutzer" system.log | grep -o "Nutzer [a-z]*" | cut -d' ' -f2 | sort | uniq
alice
bob
```

Alternative für die letzte Aufgabe:

```console
$ grep -oP "Nutzer \K[a-z]+" system.log | sort | uniq
alice
bob
```

:::
:::::

## Übung 5: Kombinierte Datenverarbeitung

:::::{admonition} 💪 Aufgabe: Bibliotheks-Statistiken
:icon: false

Erstellen Sie eine einfache Ausleih-Statistik-Datei und werten Sie diese aus:

**Vorbereitung:**

```console
$ cat > ausleihen.csv << 'EOF'
nutzer,buch,datum
alice,Python Basics,2025-10-01
bob,Git Handbuch,2025-10-02
alice,Unix Guide,2025-10-03
charlie,Python Basics,2025-10-04
alice,Excel Tipps,2025-10-05
bob,Python Basics,2025-10-06
alice,Python Advanced,2025-10-07
EOF
```

**Aufgaben:**

1. Zeigen Sie die ersten 3 Zeilen der Datei
2. Zählen Sie, wie viele Zeilen (ohne Überschrift) die Datei hat
3. Finden Sie alle Ausleihen von "alice"
4. Finden Sie alle Bücher, die "Python" im Titel haben
5. Erstellen Sie eine sortierte Liste aller Nutzer\*innen (ohne Duplikate)
6. Zählen Sie, wie oft jede\*r Nutzer\*in geliehen hat
7. Finden Sie das beliebteste Buch

:::{dropdown} ✅ Lösung

```console
$ head -n 3 ausleihen.csv
nutzer,buch,datum
alice,Python Basics,2025-10-01
bob,Git Handbuch,2025-10-02

$ tail -n +2 ausleihen.csv | wc -l
6

$ grep "alice" ausleihen.csv
alice,Python Basics,2025-10-01
alice,Unix Guide,2025-10-03
alice,Excel Tipps,2025-10-05
alice,Python Advanced,2025-10-07

$ grep "Python" ausleihen.csv
alice,Python Basics,2025-10-01
charlie,Python Basics,2025-10-04
bob,Python Basics,2025-10-06
alice,Python Advanced,2025-10-07

$ tail -n +2 ausleihen.csv | cut -d',' -f1 | sort | uniq
alice
bob
charlie

$ tail -n +2 ausleihen.csv | cut -d',' -f1 | sort | uniq -c | sort -nr
   4 alice
   2 bob
   1 charlie

$ tail -n +2 ausleihen.csv | cut -d',' -f2 | sort | uniq -c | sort -nr | head -1
   3 Python Basics
```

Interpretation: "Python Basics" wurde 3 Mal ausgeliehen und ist damit das
beliebteste Buch.

:::
:::::

## Übung 6: Aufräumen und Backup

:::::{admonition} 💪 Aufgabe: Projekt-Wartung
:icon: false

Typische Wartungsaufgaben für ein Python-Projekt:

**Vorbereitung:** Erstellen Sie ein Projekt mit verschiedenen Dateien:

```console
$ mkdir wartung-projekt
$ cd wartung-projekt
$ touch main.py utils.py test.py
$ touch data.csv data.csv.backup results.txt
$ touch .gitignore README.md
$ mkdir __pycache__
$ touch __pycache__/main.cpython-313.pyc
$ touch temp_file.txt debug.log
```

**Aufgaben:**

1. Listen Sie alle Dateien (inklusive versteckter) auf
2. Finden Sie alle Python-Dateien
3. Erstellen Sie ein Backup-Verzeichnis und kopieren Sie alle `.py`-Dateien
   dorthin
4. Löschen Sie alle `.pyc`-Dateien und das `__pycache__`-Verzeichnis
5. Löschen Sie alle Dateien, die mit "temp" oder "debug" beginnen
6. Erstellen Sie eine Liste aller verbleibenden Dateien in `dateien.txt`

:::{dropdown} ✅ Lösung

```console
$ ls -la
total 16
drwxr-xr-x  4 user users 4096 Okt 17 15:00 .
drwxr-xr-x 10 user users 4096 Okt 17 14:55 ..
drwxr-xr-x  2 user users 4096 Okt 17 15:00 __pycache__
-rw-r--r--  1 user users    0 Okt 17 15:00 data.csv
-rw-r--r--  1 user users    0 Okt 17 15:00 data.csv.backup
-rw-r--r--  1 user users    0 Okt 17 15:00 debug.log
-rw-r--r--  1 user users    0 Okt 17 15:00 .gitignore
-rw-r--r--  1 user users    0 Okt 17 15:00 main.py
-rw-r--r--  1 user users    0 Okt 17 15:00 README.md
-rw-r--r--  1 user users    0 Okt 17 15:00 results.txt
-rw-r--r--  1 user users    0 Okt 17 15:00 temp_file.txt
-rw-r--r--  1 user users    0 Okt 17 15:00 test.py
-rw-r--r--  1 user users    0 Okt 17 15:00 utils.py

$ ls *.py
main.py  test.py  utils.py

$ mkdir backup
$ cp *.py backup/
$ ls backup/
main.py  test.py  utils.py

$ rm -r __pycache__

$ rm temp* debug*

$ ls > dateien.txt
$ cat dateien.txt
backup
data.csv
data.csv.backup
dateien.txt
main.py
README.md
results.txt
test.py
utils.py
```

Alternative: Alle Dateien ohne versteckte und ohne Verzeichnisse:

```console
$ find . -maxdepth 1 -type f ! -name ".*" > dateien.txt
```

:::
:::::

## Zusammenfassung

Diese Übungen haben alle wichtigen Unix-Befehle kombiniert:

- Verzeichnisse und Dateien erstellen (`mkdir`, `touch`)
- Navigieren (`cd`, `pwd`, `ls`)
- Dateien kopieren, verschieben, löschen (`cp`, `mv`, `rm`)
- Berechtigungen setzen (`chmod`)
- Wildcards nutzen (`*`, `?`, `[]`)
- Text suchen (`grep`)
- Ausgaben umleiten (`>`, `>>`)
- Pipes verwenden (`|`)
- Daten verarbeiten (`sort`, `uniq`, `cut`, `wc`)

Mit diesen Fähigkeiten sind Sie gut gerüstet für die Arbeit mit
Python-Projekten auf Unix-Systemen!
