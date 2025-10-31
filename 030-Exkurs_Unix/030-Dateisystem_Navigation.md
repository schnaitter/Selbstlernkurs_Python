---
short_title: Navigation
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Dateisystem-Navigation

Die Navigation im Dateisystem über das Terminal ist eine grundlegende Fähigkeit
für Python-Entwicklung. In diesem Kapitel lernen Sie die wichtigsten Befehle
kennen.

## Die Verzeichnisstruktur

:::::{margin}
::::{note} Windows vs. Unix

Windows nutzt Laufwerksbuchstaben (`C:\`, `D:\`).

Unix-Systeme haben ein einheitliches Dateisystem, das bei `/` (root) beginnt. Alle Laufwerke und Geräte werden in diesen Baum eingehängt ("gemountet").

::::
:::::

Unix-Systeme organisieren Dateien in einer Baumstruktur:

```
/                          (root, die Wurzel)
├── home/                  (Nutzer*innen-Verzeichnisse)
│   ├── alice/
│   └── bob/
├── usr/                   (Programme und Bibliotheken)
│   ├── bin/               (Binärdateien/Programme)
│   └── lib/               (Bibliotheken)
├── etc/                   (Konfigurationsdateien)
├── tmp/                   (Temporäre Dateien)
└── var/                   (Variable Daten, Logs)
```

Wichtige Verzeichnisse:

- `/` – Das Wurzelverzeichnis (root)
- `/home/username/` – Ihr persönliches Verzeichnis (Home)
- `~` – Abkürzung für Ihr Home-Verzeichnis
- `.` – Das aktuelle Verzeichnis
- `..` – Das übergeordnete Verzeichnis

## Wo bin ich? (`pwd`)

:::::{margin}
::::{hint} `pwd` = Print Working Directory

Der Befehl `pwd` steht für "Print Working Directory" und zeigt das aktuelle
Arbeitsverzeichnis an.

::::
:::::

Um zu sehen, in welchem Verzeichnis Sie sich befinden:

```console
$ pwd
/home/alice
```

Jedes Terminal-Fenster hat ein **aktuelles Arbeitsverzeichnis**. Befehle, die
Sie ausführen, beziehen sich auf dieses Verzeichnis, wenn Sie keine absoluten
Pfade angeben.

## Was ist hier? (`ls`)

Der Befehl `ls` (list) zeigt den Inhalt eines Verzeichnisses:

```console
$ ls
Dokumente  Downloads  Bilder  projekte
```

Nützliche Optionen:

```console
$ ls -l
```

Zeigt detaillierte Informationen (Rechte, Größe, Datum):

```
drwxr-xr-x  5 alice users  4096 Okt 15 10:30 Dokumente
drwxr-xr-x  2 alice users  4096 Okt 16 08:15 Downloads
drwxr-xr-x  3 alice users  4096 Okt 10 14:20 Bilder
drwxr-xr-x  4 alice users  4096 Okt 17 09:00 projekte
```

```console
$ ls -lh
```

Mit `-h` (human-readable) werden Dateigrößen lesbarer angezeigt (KB, MB statt
Bytes).

```console
$ ls -a
```

Zeigt auch versteckte Dateien (die mit `.` beginnen):

```console
.  ..  .bashrc  .profile  Dokumente  Downloads
```

```console
$ ls -lha
```

Kombiniert alle drei Optionen: detailliert, lesbare Größen, versteckte Dateien.

## Verzeichnis wechseln (`cd`)

:::::{margin}
::::{hint} `cd` = Change Directory

Der Befehl `cd` steht für "Change Directory" und wechselt das aktuelle
Arbeitsverzeichnis.

::::
:::::

Mit `cd` (change directory) wechseln Sie in ein anderes Verzeichnis:

```console
$ pwd
/home/alice
$ cd Dokumente
$ pwd
/home/alice/Dokumente
```

### Wichtige cd-Varianten

```console
$ cd
```

Ohne Argument: Wechselt ins Home-Verzeichnis.

```console
$ cd ~
```

Explizit ins Home-Verzeichnis (äquivalent zu `cd` ohne Argument).

```console
$ cd ..
```

Wechselt ein Verzeichnis nach oben (ins übergeordnete Verzeichnis).

```console
$ cd ../..
```

Wechselt zwei Verzeichnisse nach oben.

```console
$ cd -
```

Wechselt zum vorherigen Verzeichnis zurück (wie "Zurück" in einem Browser).

## Absolute vs. relative Pfade

:::::{margin}
::::{seealso} Pfad-Notation

In Python nutzen Sie diese Pfad-Konzepte ebenfalls – z.B. beim Öffnen von
Dateien:

```python
open('/home/alice/data.csv')  # absolut
open('../data/data.csv')      # relativ
```

::::
:::::

Es gibt zwei Arten, Pfade anzugeben:

### Absolute Pfade

Beginnen mit `/` und geben den kompletten Pfad von der Wurzel an:

```console
$ cd /home/alice/projekte/python
```

Funktioniert immer, egal wo Sie gerade sind.

### Relative Pfade

Beginnen **nicht** mit `/` und sind relativ zum aktuellen Verzeichnis:

```console
$ pwd
/home/alice
$ cd projekte/python
$ pwd
/home/alice/projekte/python
```

Beispiele:

```console
$ cd ..                    # Ein Verzeichnis hoch
$ cd ../../Downloads       # Zwei hoch, dann in Downloads
$ cd ./unterordner         # In unterordner (. = aktuelles Verz.)
$ cd ~/Dokumente           # ~ wird zu /home/alice expandiert
```

## Praktisches Beispiel

Typische Navigationssitzung:

```console
$ pwd
/home/alice
$ ls
Dokumente  Downloads  projekte
$ cd projekte
$ ls
python-kurs  bibliotheks-scripts
$ cd python-kurs
$ pwd
/home/alice/projekte/python-kurs
$ ls
taschenrechner.py  data.csv  README.md
$ cd ..
$ pwd
/home/alice/projekte
$ cd ~
$ pwd
/home/alice
```

:::::{admonition} 💪 Übung
:icon: false

Führen Sie folgende Schritte aus:

1. Zeigen Sie Ihr aktuelles Verzeichnis mit `pwd` an
2. Listen Sie den Inhalt mit `ls` auf
3. Wechseln Sie in ein Unterverzeichnis (wenn vorhanden)
4. Zeigen Sie erneut mit `pwd`, wo Sie sind
5. Wechseln Sie mit `cd ..` wieder nach oben
6. Wechseln Sie mit `cd ~` in Ihr Home-Verzeichnis
7. Nutzen Sie `ls -la` um alle Dateien (inklusive versteckter) anzuzeigen

:::{dropdown} ✅ Beispiel-Lösung

```console
$ pwd
/home/alice
$ ls
Dokumente  Downloads  projekte
$ cd Dokumente
$ pwd
/home/alice/Dokumente
$ cd ..
$ pwd
/home/alice
$ cd ~
$ pwd
/home/alice
$ ls -la
total 48
drwxr-xr-x  6 alice users 4096 Okt 17 10:00 .
drwxr-xr-x  3 root  root  4096 Jan 15  2024 ..
-rw-------  1 alice users  220 Jan 15  2024 .bash_logout
-rw-------  1 alice users 3526 Jan 15  2024 .bashrc
drwxr-xr-x  5 alice users 4096 Okt 15 10:30 Dokumente
drwxr-xr-x  2 alice users 4096 Okt 16 08:15 Downloads
drwxr-xr-x  4 alice users 4096 Okt 17 09:00 projekte
```

Ihre Ausgabe wird anders aussehen, abhängig von Ihrem System und
Verzeichnisinhalt.

:::
:::::

## Tipps und Tricks

:::::{margin}
::::{hint} Tab-Vervollständigung

Nutzen Sie {kbd}`Tab` intensiv! Es spart Zeit und vermeidet Tippfehler.

```console
$ cd Dok[Tab]
$ cd Dokumente/
```

::::
:::::

**Tab-Vervollständigung:** Drücken Sie {kbd}`Tab` nach den ersten Buchstaben
eines Verzeichnisnamens:

```console
$ cd proj[Tab]
$ cd projekte/
```

**Pfade mit Leerzeichen:** Nutzen Sie Anführungszeichen oder Backslash:

```console
$ cd "Meine Dokumente"
$ cd Meine\ Dokumente
```

**Schnell navigieren:**

```console
$ cd ~/projekte/python-kurs    # Direkt in Unterverzeichnisse
$ cd -                         # Zurück zum vorherigen Ort
```
