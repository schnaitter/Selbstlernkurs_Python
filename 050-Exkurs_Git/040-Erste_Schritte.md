---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Erste Schritte mit Git

Jetzt wird es praktisch! In diesem Kapitel erstellen Sie Ihr erstes
Git-Repository und lernen die wichtigsten Grundbefehle kennen.

## Ein neues Repository erstellen

### Schritt 1: Projektordner vorbereiten

Erstellen Sie zunächst einen Ordner für ein kleines Übungsprojekt:

```bash
$ mkdir mein-erstes-repo
$ cd mein-erstes-repo
```

### Schritt 2: Git initialisieren

Um Git für diesen Ordner zu aktivieren, verwenden Sie:

```bash
$ git init
```

**Ausgabe:**

```
Initialized empty Git repository in /Users/erika/mein-erstes-repo/.git/
```

:::::{margin}
:::{hint} Was passiert hier?

Git erstellt einen versteckten `.git`-Ordner, der alle
Versionsinformationen enthält. Dieser Ordner macht aus einem normalen Ordner
ein Git-Repository.

:::
:::::

Sie können den `.git`-Ordner mit `ls -la` sichtbar machen (das `-a` zeigt
versteckte Dateien):

```bash
$ ls -la
```

## Die erste Datei hinzufügen

### Eine Datei erstellen

Erstellen Sie eine einfache Python-Datei:

```bash
$ echo "print('Hallo Git!')" > hallo.py
```

Oder erstellen Sie die Datei mit einem Texteditor Ihrer Wahl und fügen Sie
folgenden Inhalt ein:

```python
print('Hallo Git!')
```

### Status überprüfen

Prüfen Sie mit `git status`, was Git "sieht":

```bash
$ git status
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
$ git add hallo.py
```

Prüfen Sie erneut den Status:

```bash
$ git status
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

:::::{tip} Mehrere Dateien hinzufügen

Sie können auch mehrere Dateien auf einmal hinzufügen:

```bash
$ git add datei1.py datei2.py datei3.py
```

Oder alle geänderten Dateien im aktuellen Ordner:

```bash
$ git add .
```

:::{caution} Vorsicht

`git add .` fügt _alle_ Änderungen hinzu – prüfen Sie vorher mit `git status`,
ob das wirklich gewünscht ist!

:::
:::::

## Git commit: Den ersten Commit erstellen

:::::{margin}
:::{hint} Commit-Hash

Die Buchstaben-Zahlen-Kombination `a1b2c3d` ist die eindeutige ID dieses
Commits (ein verkürzter SHA-Hash).

Sie wird für den Commit inkl. der Commit-Message berechnet. Git nutzt an vielen
Stellen einen Hash als Bezeichner um Dateien, Commits, Notizen, … zu
identifizieren.

Befehle zeigen als Ausgabe oft den ganzen Hash an. Wollen Sie einen Hash
referenzieren, so reichen typischerweise 8-10 Zeichen vom Anfang, solange diese
Zeichenkette dann noch ein-eindeutig unter den Hash-Werte im Repositorium ist.

:::
:::::

Jetzt speichern wir die Änderung dauerhaft in der Versionsgeschichte:

```bash
$ git commit -m "Erste Version: Hallo-Welt-Skript hinzugefügt"
```

**Ausgabe:**

```
[main (root-commit) a1b2c3d] Erste Version: Hallo-Welt-Skript hinzugefügt
 1 file changed, 1 insertion(+)
 create mode 100644 hallo.py
```

**Was bedeutet das `-m`?** Das `-m` steht für "message" (Nachricht). Die
Nachricht sollte kurz beschreiben, was in diesem Commit geändert wurde.

### Status nach dem Commit

Prüfen Sie erneut mit `git status`:

```bash
$ git status
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

### Datei ändern

Öffnen Sie `hallo.py` und ändern Sie den Inhalt:

```python
# Mein erstes Git-Projekt

def begruessung(name):
    return f"Hallo {name}, willkommen bei Git!"

print(begruessung("Welt"))
```

### Änderungen anzeigen

Mit `git status` sehen Sie:

```bash
$ git status
```

**Ausgabe:**

```
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
        modified:   hallo.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Git hat die Änderung bemerkt, aber sie ist noch nicht in der Staging Area.

### Änderung zur Staging Area hinzufügen und committen

```bash
$ git add hallo.py
$ git commit -m "Begrüßungsfunktion hinzugefügt"
```

**Ausgabe:**

```
[main e4f5g6h] Begrüßungsfunktion hinzugefügt
 1 file changed, 5 insertions(+), 1 deletion(-)
```

## Gute Commit-Messages schreiben

Commit-Messages sind wichtig für die Nachvollziehbarkeit. Hier einige
Richtlinien:

### Gute Commit-Messages

```
Divisionsfunktion hinzugefügt
Bugfix: Division durch Null abfangen
Dokumentation für CSV-Import erweitert
Konfigurationsdatei für Tests erstellt
```

**Merkmale guter Messages:**

- **Kurz und prägnant** (idealerweise unter 50 Zeichen)
- **Beschreiben, WAS geändert wurde** (nicht wie oder warum – das steht im
  Code)
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

Für komplexere Commits können Sie eine ausführlichere Beschreibung hinzufügen:

```bash
$ git commit
```

(ohne `-m`) öffnet Ihren konfigurierten Texteditor. Schreiben Sie:

```
Divisionsfunktion mit Fehlerbehandlung hinzugefügt

- Division durch Null wird abgefangen
- Rückgabe von None bei ungültigen Eingaben
- Tests für Edge-Cases ergänzt
```

**Format:**

- Erste Zeile: Kurze Zusammenfassung (unter 50 Zeichen)
- Leerzeile
- Ausführlichere Beschreibung (optional)

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
$ git status

# 2. Dateien zur Staging Area hinzufügen
$ git add dateiname.py

# 3. Commit erstellen
$ git commit -m "Beschreibung der Änderung"

# 4. Status erneut prüfen (alles committed?)
$ git status
```

## Häufige Anfängerfehler

### Fehler 1: Vergessen, `git add` zu verwenden

```bash
# Datei geändert, aber vergessen, sie hinzuzufügen
$ git commit -m "Änderungen"
```

**Ergebnis**: Fehlermeldung oder leerer Commit

**Lösung**: Immer erst `git add`, dann `git commit`

### Fehler 2: Commit ohne Message

```bash
$ git commit
```

Ohne `-m` öffnet sich ein Editor. Anfänger\*innen schließen diesen oft, ohne
eine Message einzugeben.

**Lösung**: Entweder Message im Editor eingeben oder `-m "Message"` verwenden

### Fehler 3: Ungewollte Dateien committen

```bash
$ git add .
$ git commit -m "Alles"
```

Dabei werden auch temporäre Dateien, Caches oder vertrauliche Daten committed.

**Lösung**: Immer erst `git status` prüfen, dann gezielt Dateien mit `git add`
auswählen. Im nächsten Kapitel lernen Sie `.gitignore` kennen.

## Zusammenfassung

Die wichtigsten Befehle für die ersten Schritte:

| Befehl                 | Beschreibung                      |
| ---------------------- | --------------------------------- |
| `git init`             | Repository initialisieren         |
| `git status`           | Status anzeigen (sehr wichtig!)   |
| `git add <datei>`      | Datei zur Staging Area hinzufügen |
| `git add .`            | Alle Änderungen hinzufügen        |
| `git commit -m "Text"` | Commit mit Message erstellen      |

:::::{admonition} 💪 Übung
:icon: false

Erstellen Sie ein kleines Python-Projekt mit mindestens 3 Commits:

1. Erstellen Sie ein neues Repository mit `git init`
2. Fügen Sie eine Python-Datei hinzu und committen Sie sie
3. Ändern Sie die Datei und committen Sie die Änderung
4. Fügen Sie eine zweite Datei hinzu und committen Sie sie

Prüfen Sie nach jedem Schritt mit `git status`, was gerade passiert!

:::::

Im nächsten Kapitel lernen Sie, wie Sie die Versionsgeschichte anzeigen und
durch frühere Versionen navigieren können.
