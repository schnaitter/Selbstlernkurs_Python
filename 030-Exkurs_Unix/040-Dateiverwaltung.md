---
short_title: Dateiverwaltung
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Dateiverwaltung

In diesem Kapitel lernen Sie, wie Sie Verzeichnisse erstellen, Dateien
kopieren, verschieben und löschen – alles über das Terminal.

## Verzeichnisse erstellen (`mkdir`)

:::::{margin}
::::{hint} `mkdir` = Make Directory

Der Befehl `mkdir` erstellt ein neues Verzeichnis.

::::
:::::

Mit `mkdir` erstellen Sie neue Verzeichnisse:

```console
$ mkdir python-projekt
$ ls
python-projekt
```

### Mehrere Verzeichnisse auf einmal

```console
$ mkdir projekt1 projekt2 projekt3
$ ls
projekt1  projekt2  projekt3
```

### Verschachtelte Verzeichnisse

Mit der Option `-p` (parents) erstellen Sie auch alle übergeordneten
Verzeichnisse:

```console
$ mkdir -p projekte/python/bibliothek-tools
$ ls projekte/python/
bibliothek-tools
```

Ohne `-p` würde dieser Befehl fehlschlagen, wenn `projekte/` oder
`projekte/python/` noch nicht existieren.

## Leere Dateien erstellen (`touch`)

Der Befehl `touch` erstellt eine leere Datei (oder aktualisiert den Zeitstempel
einer existierenden Datei):

```console
$ touch README.md
$ ls
README.md
```

Das ist praktisch, um schnell Platzhalter-Dateien zu erstellen:

```console
$ touch main.py data.csv requirements.txt
$ ls
data.csv  main.py  README.md  requirements.txt
```

## Dateien kopieren (`cp`)

:::::{margin}
::::{caution} Überschreiben

`cp` überschreibt bestehende Dateien ohne Warnung! Nutzen Sie `cp -i` für eine
interaktive Nachfrage.

::::
:::::

Mit `cp` (copy) kopieren Sie Dateien:

```console
$ cp quelle.txt ziel.txt
```

### Datei in ein Verzeichnis kopieren

```console
$ cp main.py backup/
```

Kopiert `main.py` in das Verzeichnis `backup/` (Dateiname bleibt gleich).

### Mehrere Dateien kopieren

```console
$ cp datei1.txt datei2.txt datei3.txt zielverzeichnis/
```

Das letzte Argument muss ein Verzeichnis sein.

### Verzeichnisse kopieren

Für Verzeichnisse benötigen Sie die Option `-r` (recursive):

```console
$ cp -r projekt/ projekt-backup/
```

Kopiert das gesamte Verzeichnis `projekt/` mit allem Inhalt nach
`projekt-backup/`.

## Dateien und Verzeichnisse verschieben/umbenennen (`mv`)

:::::{margin}
::::{note} `mv` = Move

`mv` verschiebt Dateien **und** benennt sie um – beides ist die gleiche
Operation (Änderung des Pfades).

::::
:::::

Mit `mv` (move) verschieben Sie Dateien oder benennen sie um:

### Datei umbenennen

```console
$ mv alter-name.txt neuer-name.txt
```

### Datei verschieben

```console
$ mv datei.txt anderes-verzeichnis/
```

### Mehrere Dateien verschieben

```console
$ mv datei1.txt datei2.txt zielverzeichnis/
```

### Verzeichnis umbenennen

```console
$ mv altes-verzeichnis neues-verzeichnis
```

Im Gegensatz zu `cp` benötigt `mv` **keine** `-r` Option für Verzeichnisse.

## Dateien und Verzeichnisse löschen (`rm`, `rmdir`)

:::::{margin}
::::{danger} Achtung: Kein Papierkorb!

`rm` löscht Dateien **endgültig**. Es gibt keinen Papierkorb. Gelöschte Dateien
sind unwiederbringlich verloren!

Tipp: Nutzen Sie `rm -i` für eine Sicherheitsabfrage vor jedem Löschen.

::::
:::::

### Dateien löschen (`rm`)

```console
$ rm datei.txt
```

Mehrere Dateien:

```console
$ rm datei1.txt datei2.txt datei3.txt
```

Mit Sicherheitsabfrage:

```console
$ rm -i wichtige-datei.txt
rm: remove regular file 'wichtige-datei.txt'? y
```

### Leere Verzeichnisse löschen (`rmdir`)

```console
$ rmdir leeres-verzeichnis
```

Funktioniert nur bei leeren Verzeichnissen!

### Verzeichnisse mit Inhalt löschen (`rm -r`)

:::::{margin}
::::{danger} Besonders gefährlich

`rm -rf` löscht alles rekursiv ohne Nachfrage. Doppelt prüfen vor der
Ausführung!

**Niemals** `rm -rf /` ausführen (löscht das gesamte System).

::::
:::::

Mit der Option `-r` (recursive) löschen Sie Verzeichnisse mit ihrem gesamten
Inhalt:

```console
$ rm -r verzeichnis/
```

Kombination mit `-i` für Sicherheit:

```console
$ rm -ri verzeichnis/
```

Für erzwungenes Löschen ohne Nachfrage (Vorsicht!):

```console
$ rm -rf verzeichnis/
```

## Dateiinhalte anzeigen

### Komplette Datei anzeigen (`cat`)

:::::{margin}
::::{hint} `cat` = Concatenate

`cat` wurde ursprünglich zum Zusammenfügen (concatenate) mehrerer Dateien
entwickelt, wird aber meist zum Anzeigen einzelner Dateien genutzt.

::::
:::::

```console
$ cat README.md
# Mein Python-Projekt

Dies ist ein Beispielprojekt.
```

Mehrere Dateien:

```console
$ cat datei1.txt datei2.txt
```

### Seitenweise anzeigen (`less`)

Für längere Dateien ist `less` besser geeignet:

```console
$ less lange-datei.txt
```

Navigation in `less`:

- {kbd}`Space` oder {kbd}`Page Down`: Eine Seite vor
- {kbd}`b` oder {kbd}`Page Up`: Eine Seite zurück
- {kbd}`/suchbegriff`: Suchen
- {kbd}`q`: Beenden

### Anfang einer Datei (`head`)

```console
$ head datei.txt
```

Zeigt die ersten 10 Zeilen. Für eine andere Anzahl:

```console
$ head -n 5 datei.txt
```

Zeigt die ersten 5 Zeilen.

### Ende einer Datei (`tail`)

```console
$ tail datei.txt
```

Zeigt die letzten 10 Zeilen. Praktisch für Log-Dateien:

```console
$ tail -n 20 logfile.log
```

Zeigt die letzten 20 Zeilen.

Live-Anzeige (folgt neuen Zeilen):

```console
$ tail -f logfile.log
```

Nützlich, um Log-Dateien in Echtzeit zu beobachten. Beenden mit
{kbd}`Strg`+{kbd}`C`.

## Praktisches Beispiel: Projektstruktur erstellen

Erstellen Sie eine typische {term}`Python`-Projektstruktur:

```console
$ mkdir -p python-projekt/{src,tests,docs,data}
$ cd python-projekt
$ touch README.md requirements.txt
$ touch src/main.py src/utils.py
$ touch tests/test_main.py
$ touch docs/anleitung.md
$ ls -R
.:
data  docs  README.md  requirements.txt  src  tests

./data:

./docs:
anleitung.md

./src:
main.py  utils.py

./tests:
test_main.py
```

````{exercise}
:label: unix-dateiverwaltung

Erstellen Sie folgende Struktur und üben Sie die Befehle:

1. Erstellen Sie ein Verzeichnis `uebung-unix`
2. Wechseln Sie in dieses Verzeichnis
3. Erstellen Sie drei Unterverzeichnisse: `scripts`, `data`, `output`
4. Erstellen Sie in `scripts/` eine leere Datei `verarbeitung.py`
5. Kopieren Sie diese Datei nach `scripts/verarbeitung_backup.py`
6. Erstellen Sie in `data/` eine Datei `test.csv`
7. Listen Sie die gesamte Struktur mit `ls -R` auf
8. Verschieben Sie `scripts/verarbeitung_backup.py` nach `output/`
9. Löschen Sie das Verzeichnis `data/` komplett
10. Überprüfen Sie mit `ls`, was noch da ist
````

````{solution} unix-dateiverwaltung
:class: dropdown

```console
$ mkdir uebung-unix
$ cd uebung-unix
$ mkdir scripts data output
$ touch scripts/verarbeitung.py
$ cp scripts/verarbeitung.py scripts/verarbeitung_backup.py
$ touch data/test.csv
$ ls -R
.:
data  output  scripts

./data:
test.csv

./output:

./scripts:
verarbeitung.py  verarbeitung_backup.py
$ mv scripts/verarbeitung_backup.py output/
$ rm -r data
$ ls
output  scripts
$ ls -R
.:
output  scripts

./output:
verarbeitung_backup.py

./scripts:
verarbeitung.py
```
````

## Zusammenfassung der Befehle

| Befehl     | Bedeutung                    | Beispiel             |
| ---------- | ---------------------------- | -------------------- |
| `mkdir`    | Verzeichnis erstellen        | `mkdir projekte`     |
| `mkdir -p` | Verschachtelte Verzeichnisse | `mkdir -p a/b/c`     |
| `touch`    | Leere Datei erstellen        | `touch datei.txt`    |
| `cp`       | Datei kopieren               | `cp a.txt b.txt`     |
| `cp -r`    | Verzeichnis kopieren         | `cp -r dir1 dir2`    |
| `mv`       | Verschieben/Umbenennen       | `mv alt.txt neu.txt` |
| `rm`       | Datei löschen                | `rm datei.txt`       |
| `rm -r`    | Verzeichnis löschen          | `rm -r verzeichnis`  |
| `rmdir`    | Leeres Verzeichnis löschen   | `rmdir leer`         |
| `cat`      | Datei anzeigen               | `cat datei.txt`      |
| `less`     | Seitenweise anzeigen         | `less datei.txt`     |
| `head`     | Anfang anzeigen              | `head datei.txt`     |
| `tail`     | Ende anzeigen                | `tail datei.txt`     |
