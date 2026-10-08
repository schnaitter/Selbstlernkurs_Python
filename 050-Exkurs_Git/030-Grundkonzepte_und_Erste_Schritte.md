---
short_title: Grundkonzepte und erste Schritte
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Grundkonzepte und erste Schritte

Bevor wir mit Git arbeiten, ist es wichtig, die grundlegenden Konzepte zu
verstehen. Anschließend setzen wir sie in die Praxis um und erstellen unser
erstes Repository.

## Repository (Projektarchiv)

Ein {term}`Repository` (oft abgekürzt als "Repo") ist ein Projektordner, den {term}`Git`
überwacht. Es enthält:

- Alle Ihre Dateien (Python-Skripte, Daten, Dokumentation)
- Die gesamte Versionsgeschichte (wer hat wann was geändert)
- Git-Konfiguration (im versteckten Ordner `.git`)

Ein Repository kann lokal auf Ihrem Computer oder remote auf einem Server
(GitHub, GitLab) liegen.

:::::{margin}
**Wichtig**: Der `.git`-Ordner enthält alle Versionsinformationen. Löschen Sie
diesen Ordner nie, sonst verlieren Sie die gesamte Versionsgeschichte!
:::::

## Die drei Bereiche in Git

Git arbeitet mit drei wichtigen Bereichen. Das Verständnis dieser Bereiche ist
zentral für die Arbeit mit Git:

```{mermaid}
graph LR
    A[Working Directory<br/>Arbeitsverzeichnis] -->|git add| B[Staging Area<br/>Bereitstellung]
    B -->|git commit| C[Repository<br/>Versionsgeschichte]
    C -->|git checkout| A

    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#e1ffe1
```

### 1. Working Directory (Arbeitsverzeichnis)

Das **Working Directory** ist Ihr normaler Projektordner – so wie Sie ihn im
Dateimanager sehen. Hier bearbeiten Sie Ihre Dateien mit Ihrem Texteditor oder
Ihrer IDE.

**Beispiel**: Sie öffnen `taschenrechner.py` in VS Code und fügen eine neue
Funktion hinzu. Diese Änderung befindet sich zunächst nur im Working Directory.

### 2. Staging Area (Bereitstellungsbereich)

Die **Staging Area** ist ein Zwischenbereich. Hier sammeln Sie alle Änderungen,
die Sie in den nächsten Commit aufnehmen möchten.

**Warum braucht man das?** Stellen Sie sich vor, Sie haben an mehreren Dateien
gearbeitet:

- `taschenrechner.py`: Neue Funktion für Division
- `statistik.py`: Bugfix
- `dokumentation.md`: Rechtschreibfehler korrigiert

Mit der Staging Area können Sie entscheiden: "Ich möchte nur die Änderungen an
`taschenrechner.py` und `statistik.py` committen, aber `dokumentation.md` erst
später." So können Sie thematisch zusammengehörige Änderungen bündeln.

**Befehl**: `git add dateiname` fügt eine Datei zur Staging Area hinzu.

### 3. Repository / Versionsgeschichte

Wenn Sie einen **{term}`Commit`** erstellen, werden alle Änderungen aus der Staging
Area dauerhaft in der Versionsgeschichte gespeichert. Ein Commit ist wie ein
Schnappschuss Ihres Projekts zu einem bestimmten Zeitpunkt.

**Befehl**: `git commit -m "Beschreibung"` erstellt einen Commit.

## Was ist ein Commit?

Ein **Commit** ist eine gespeicherte Version Ihres Projekts. Jeder Commit
enthält:

- **Änderungen**: Was wurde geändert (z.B. "Zeile 42 in `taschenrechner.py`
  hinzugefügt")
- **Commit-Message**: Kurze Beschreibung der Änderung
- **Metadaten**: Autor\*in, Zeitstempel, eindeutige ID (Hash)
- **Verweis auf vorherigen Commit**: Commits bilden eine Kette

Commits bilden eine **Kette**: Jeder Commit zeigt über seinen **Parent** auf
den Vorgänger. So entsteht eine Timeline der Projektentwicklung, in der jeder
Commit über seinen **Hash** (eine eindeutige ID) angesprochen werden kann.

## Der Status-Befehl

Der wichtigste Befehl, um zu verstehen, was gerade wo ist:

```bash
git status
```

Dieser Befehl zeigt:

- Welche Dateien verändert wurden (im Working Directory)
- Welche Dateien für den Commit bereitstehen (in der Staging Area)
- Welche Dateien noch nicht von Git überwacht werden (untracked)

**Beispiel-Ausgabe:**

```
On branch main

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   taschenrechner.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   dokumentation.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        testdaten.csv
```

**Interpretation:**

- `taschenrechner.py` ist in der Staging Area → wird beim nächsten Commit
  gespeichert
- `dokumentation.md` wurde geändert, aber noch nicht zur Staging Area
  hinzugefügt
- `testdaten.csv` ist eine neue Datei, die Git noch nicht kennt

## Ein neues Repository erstellen

Jetzt wird es praktisch! Wir erstellen ein kleines Übungsprojekt.

### Schritt 1: Projektordner vorbereiten

```bash
mkdir mein-erstes-repo
cd mein-erstes-repo
```

### Schritt 2: Git initialisieren

Um Git für diesen Ordner zu aktivieren, verwenden Sie:

```bash
git init
```

**Ausgabe:**

```
Initialized empty Git repository in /Users/erika/mein-erstes-repo/.git/
```

:::::{margin}
**Was passiert hier?** Git erstellt einen versteckten `.git`-Ordner, der alle
Versionsinformationen enthält. Dieser Ordner macht aus einem normalen Ordner
ein Git-Repository.
:::::

Sie können den `.git`-Ordner mit `ls -la` sichtbar machen (das `-a` zeigt
versteckte Dateien).

## Die erste Datei hinzufügen

### Eine Datei erstellen

```bash
echo "print('Hallo Git!')" > hallo.py
```

Oder erstellen Sie die Datei mit einem Texteditor Ihrer Wahl:

```python
print('Hallo Git!')
```

### Status überprüfen

```bash
git status
```

**Ausgabe:**

```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hallo.py

nothing added to commit but untracked files present (use "git add" to track)
```

**Interpretation**: Git hat die neue Datei `hallo.py` bemerkt, überwacht sie
aber noch nicht ("untracked").

## Git add: Dateien zur Staging Area hinzufügen

Um Git mitzuteilen, dass Sie `hallo.py` versionieren möchten:

```bash
git add hallo.py
```

Prüfen Sie erneut den Status:

```bash
git status
```

**Ausgabe:**

```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   hallo.py
```

Die Datei ist jetzt in der **Staging Area** und bereit für den ersten Commit!

:::::{admonition} Mehrere Dateien hinzufügen
:class: tip
Sie können auch mehrere Dateien auf einmal hinzufügen:

```bash
git add datei1.py datei2.py datei3.py
```

Oder alle geänderten Dateien im aktuellen Ordner:

```bash
git add .
```

**Vorsicht**: `git add .` fügt _alle_ Änderungen hinzu – prüfen Sie vorher mit
`git status`, ob das wirklich gewünscht ist!
:::::

## Git commit: Den ersten Commit erstellen

Jetzt speichern wir die Änderung dauerhaft in der Versionsgeschichte:

```bash
git commit -m "Erste Version: Hallo-Welt-Skript hinzugefügt"
```

**Ausgabe:**

```
[main (root-commit) a1b2c3d] Erste Version: Hallo-Welt-Skript hinzugefügt
 1 file changed, 1 insertion(+)
 create mode 100644 hallo.py
```

:::::{margin}
**Commit-Hash**: Die Buchstaben-Zahlen-Kombination `a1b2c3d` ist die eindeutige
ID dieses Commits (ein verkürzter SHA-Hash).
:::::

**Was bedeutet das `-m`?** Das `-m` steht für "message" (Nachricht). Die
Nachricht sollte kurz beschreiben, was in diesem Commit geändert wurde.

### Status nach dem Commit

```bash
git status
```

**Ausgabe:**

```
On branch main
nothing to commit, working tree clean
```

**"Working tree clean"** bedeutet: Alle Änderungen sind committed, es gibt
keine offenen Änderungen.

## Weitere Änderungen committen

Lassen Sie uns das Skript erweitern und diese Änderung als zweiten Commit
speichern.

```python
# Mein erstes Git-Projekt

def begruessung(name):
    return f"Hallo {name}, willkommen bei Git!"

print(begruessung("Welt"))
```

Mit `git status` sehen Sie, dass `hallo.py` geändert wurde, die Änderung aber
noch nicht in der Staging Area liegt. Also:

```bash
git add hallo.py
git commit -m "Begrüßungsfunktion hinzugefügt"
```

**Ausgabe:**

```
[main e4f5g6h] Begrüßungsfunktion hinzugefügt
 1 file changed, 5 insertions(+), 1 deletion(-)
```

## Gute Commit-Messages schreiben

Commit-Messages sind wichtig für die Nachvollziehbarkeit. Hier einige
Richtlinien.

### Gute Commit-Messages

```
Divisionsfunktion hinzugefügt
Bugfix: Division durch Null abfangen
Dokumentation für CSV-Import erweitert
Konfigurationsdatei für Tests erstellt
```

**Merkmale guter Messages:**

- **Kurz und prägnant** (idealerweise unter 50 Zeichen)
- **Beschreiben, WAS geändert wurde**
- **Im Imperativ** ("füge hinzu", "behebe", nicht "hinzugefügt", "behoben")
- **Deutsch oder Englisch** – bleiben Sie konsistent!

### Schlechte Commit-Messages

```
Update
Änderungen
asdf
WIP
fertig gemacht
kleine Anpassungen
```

**Probleme:**

- Zu vage ("Änderungen" – was genau?)
- Nicht aussagekräftig ("fertig gemacht" – was ist fertig?)
- Unprofessionell ("asdf")

:::::{tip} Tipp: Commit-Message als Satzergänzung
Stellen Sie sich vor, Ihre Message vervollständigt den Satz:

**"Dieser Commit wird..."**

- ✅ "...Divisionsfunktion hinzufügen"
- ✅ "...Bugfix für Nullwerte anwenden"
- ❌ "...Änderungen gemacht haben"
:::::

### Längere Commit-Messages

Für komplexere Commits rufen Sie `git commit` ohne `-m` auf. Der Editor öffnet
sich, und Sie schreiben eine kurze Zusammenfassung (unter 50 Zeichen), eine
Leerzeile und anschließend eine ausführliche Beschreibung – so passen wichtige
Details in den Commit, ohne die erste Zeile zu überladen.

## Der typische Git-Workflow

Zusammengefasst sieht ein typischer Arbeitszyklus so aus:

```{mermaid}
graph TD
    A[1. Dateien bearbeiten] --> B[2. git status prüfen]
    B --> C[3. git add Dateien]
    C --> D[4. git commit -m 'Message']
    D --> E[5. Weiterarbeiten...]
    E --> A

    style A fill:#e1f5ff
    style C fill:#fff4e1
    style D fill:#e1ffe1
```

### Workflow in Befehlen

```bash
# 1. Status prüfen (was wurde geändert?)
git status

# 2. Dateien zur Staging Area hinzufügen
git add dateiname.py

# 3. Commit erstellen
git commit -m "Beschreibung der Änderung"

# 4. Status erneut prüfen (alles committed?)
git status
```

## Zusammenfassung

Die wichtigsten Konzepte und Befehle der ersten Schritte:

| Konzept / Befehl       | Beschreibung                                       |
| ---------------------- | -------------------------------------------------- |
| **Repository**         | Projektordner mit Versionsgeschichte               |
| **Working Directory**  | Ihr aktueller Arbeitsbereich                       |
| **Staging Area**       | Änderungen, die für den nächsten Commit vorgemerkt |
| **Commit**             | Gespeicherter Schnappschuss des Projekts           |
| `git init`             | Repository initialisieren                          |
| `git status`           | Status anzeigen (sehr wichtig!)                    |
| `git add <datei>`      | Datei zur Staging Area hinzufügen                  |
| `git add .`            | Alle Änderungen hinzufügen                         |
| `git commit -m "Text"` | Commit mit Message erstellen                       |

```{exercise} Übung: Erste Schritte mit Git
:label: git-erste-schritte

Erstellen Sie ein kleines Python-Projekt mit mindestens 3 Commits:

1. Erstellen Sie ein neues Repository mit `git init`
2. Fügen Sie eine Python-Datei hinzu und committen Sie sie
3. Ändern Sie die Datei und committen Sie die Änderung
4. Fügen Sie eine zweite Datei hinzu und committen Sie sie

Prüfen Sie nach jedem Schritt mit `git status`, was gerade passiert!
```

Im nächsten Kapitel lernen Sie, wie Sie die Versionsgeschichte anzeigen und
durch frühere Versionen navigieren können.
