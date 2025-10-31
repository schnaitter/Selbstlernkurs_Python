---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Versionsgeschichte und Historie

Einer der großen Vorteile von Git ist die Möglichkeit, die gesamte
Entwicklungsgeschichte eines Projekts nachzuvollziehen. In diesem Kapitel
lernen Sie, wie Sie durch die Historie navigieren und Änderungen betrachten
können.

## Die Historie anzeigen: git log

Der Befehl `git log` zeigt alle bisherigen Commits:

```bash
git log
```

**Beispiel-Ausgabe:**

```
commit e4f5g6h1i2j3k4l5m6n7o8p9q0r1s2t3u4v5w6x7 (HEAD -> main)
Author: Erika Mustermann <erika.mustermann@example.com>
Date:   Tue Oct 17 14:23:45 2025 +0200

    Begrüßungsfunktion hinzugefügt

commit a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
Author: Erika Mustermann <erika.mustermann@example.com>
Date:   Tue Oct 17 13:15:20 2025 +0200

    Erste Version: Hallo-Welt-Skript hinzugefügt
```

**Bestandteile eines Log-Eintrags:**

- **Commit-Hash**: Eindeutige ID (lange Hexadezimalzahl)
- **Author**: Name und E-Mail der Person, die den Commit erstellt hat
- **Date**: Zeitstempel
- **Commit-Message**: Beschreibung der Änderung
- **(HEAD -> main)**: Zeigt an, wo Sie sich gerade befinden

:::::{margin}
**HEAD** ist ein Zeiger auf den aktuell ausgecheckten Commit (normalerweise der
neueste Commit auf Ihrem aktuellen Branch).
:::::

### Kompakte Log-Ansicht

Die Standard-Ausgabe ist manchmal zu ausführlich. Eine kompaktere Darstellung:

```bash
git log --oneline
```

**Ausgabe:**

```
e4f5g6h (HEAD -> main) Begrüßungsfunktion hinzugefügt
a1b2c3d Erste Version: Hallo-Welt-Skript hinzugefügt
```

Jetzt sehen Sie nur die kurzen Hashes und die Commit-Messages.

### Weitere nützliche Log-Optionen

```bash
# Letzte 5 Commits anzeigen
git log -5

# Graphische Darstellung von Branches
git log --oneline --graph --all

# Mit Statistik (welche Dateien geändert wurden)
git log --stat

# Änderungen in kompakter Form
git log --oneline --decorate --graph
```

:::::{admonition} Tipp: Log-Ausgabe beenden
:class: tip

Falls die Log-Ausgabe sehr lang ist, öffnet Git einen "Pager" (meistens
`less`). Navigieren Sie mit:

- Pfeiltasten oder `j`/`k`: auf/ab scrollen
- Leertaste: eine Seite weiter
- `q`: Beenden

:::::

## Unterschiede anzeigen: git diff

Der Befehl `git diff` zeigt Unterschiede zwischen verschiedenen Versionen.

### Änderungen im Working Directory

Um zu sehen, **welche Änderungen** Sie seit dem letzten Commit gemacht haben:

```bash
git diff
```

**Beispiel**: Sie ändern `hallo.py`:

```python
# Vorher:
print('Hallo Git!')

# Nachher:
print('Hallo Git!')
print('Versionskontrolle ist super!')
```

`git diff` zeigt:

```diff
diff --git a/hallo.py b/hallo.py
index a1b2c3d..e4f5g6h 100644
--- a/hallo.py
+++ b/hallo.py
@@ -1 +1,2 @@
 print('Hallo Git!')
+print('Versionskontrolle ist super!')
```

**Interpretation:**

- **Grün/+**: Hinzugefügte Zeilen
- **Rot/-**: Gelöschte Zeilen
- Die Zeile mit `@@` zeigt, wo im File die Änderung ist

### Unterschiede in der Staging Area

Um Änderungen zu sehen, die bereits mit `git add` zur Staging Area hinzugefügt
wurden:

```bash
git diff --staged
```

oder

```bash
git diff --cached
```

### Unterschiede zwischen Commits

Vergleichen Sie zwei Commits miteinander:

```bash
git diff a1b2c3d e4f5g6h
```

Oder vergleichen Sie den aktuellen Zustand mit einem früheren Commit:

```bash
git diff a1b2c3d
```

### Unterschiede für eine bestimmte Datei

```bash
git diff hallo.py
```

Zeigt nur Änderungen in `hallo.py`.

## Zu früheren Versionen zurückkehren

Git erlaubt es Ihnen, jederzeit zu einer früheren Version zurückzukehren. Es
gibt verschiedene Möglichkeiten:

### 1. Eine Datei wiederherstellen: git restore

**Szenario**: Sie haben `hallo.py` geändert, aber die Änderungen gefallen Ihnen
nicht. Sie möchten zur letzten committed Version zurück.

```bash
git restore hallo.py
```

:::::{warning} Vorsicht
Dieser Befehl verwirft alle nicht-committeten Änderungen in der Datei! Die
Änderungen sind unwiederbringlich verloren.
:::::

### 2. Eine Datei aus der Staging Area entfernen

**Szenario**: Sie haben eine Datei mit `git add` hinzugefügt, möchten sie aber
doch nicht committen.

```bash
git restore --staged hallo.py
```

Die Datei bleibt geändert, wird aber aus der Staging Area entfernt.

### 3. Zu einem früheren Commit wechseln: git checkout

Sie können sich einen früheren Zustand des Projekts ansehen:

```bash
git checkout a1b2c3d
```

:::::{margin}
**Detached HEAD**: Wenn Sie zu einem alten Commit wechseln, befinden Sie sich
im "detached HEAD"-Zustand. Das bedeutet, Sie sehen den alten Zustand, arbeiten
aber nicht mehr auf einem Branch.
:::::

**Was passiert?** Alle Dateien werden auf den Zustand von Commit `a1b2c3d` zurückgesetzt.

**Zurück zum neuesten Stand:**

```bash
git checkout main
```

(oder der Name Ihres Branches)

### 4. Einen alten Zustand wiederherstellen (neuer Commit)

**Szenario**: Sie möchten eine Datei auf einen früheren Stand zurücksetzen,
aber als neuen Commit speichern.

```bash
# Datei auf Stand von Commit a1b2c3d zurücksetzen
git checkout a1b2c3d -- hallo.py

# Als neuen Commit speichern
git commit -m "Datei auf früheren Stand zurückgesetzt"
```

Das `--` trennt Commit-Hashes von Dateinamen.

## Einen Commit rückgängig machen: git revert

**Szenario**: Ein Commit hat einen Fehler eingeführt. Sie möchten ihn
rückgängig machen, aber die Historie nicht verändern.

```bash
git revert e4f5g6h
```

Git erstellt einen **neuen Commit**, der die Änderungen von `e4f5g6h`
rückgängig macht. Die Historie bleibt erhalten – das ist wichtig, wenn Sie
bereits mit anderen Personen zusammenarbeiten.

## Vergleich: restore vs. revert vs. reset

| Befehl                         | Zweck                                     | Wirkung                                                 |
| ------------------------------ | ----------------------------------------- | ------------------------------------------------------- |
| `git restore <datei>`          | Änderungen im Working Directory verwerfen | Datei auf letzten Commit-Stand zurücksetzen             |
| `git restore --staged <datei>` | Datei aus Staging Area entfernen          | Bleibt geändert, aber nicht mehr staged                 |
| `git revert <commit>`          | Commit rückgängig machen                  | Erstellt neuen Commit, der Änderungen zurücknimmt       |
| `git reset`                    | Historie zurücksetzen                     | **Vorsicht! Verändert Historie** (für Fortgeschrittene) |

:::::{admonition} reset ist für Fortgeschrittene
:class: warning
Der Befehl `git reset` wird in diesem Kurs bewusst nicht behandelt. Er kann die
Historie verändern und ist fehleranfällig. Für den Einstieg reichen `restore`
und `revert` vollkommen aus.
:::::

## Praktisches Beispiel: Fehler korrigieren

Angenommen, Sie haben einen Fehler gemacht:

```python
# Commit 1: Funktion hinzugefügt
def addiere(a, b):
    return a + b

# Commit 2: Fehler! Falsche Funktion implementiert
def subtrahiere(a, b):
    return a + b  # Bug: sollte a - b sein!

# Commit 3: Weitere Funktionen
def multipliziere(a, b):
    return a * b
```

**Option 1: Neuer Commit mit Bugfix**

```bash
# Fehler in datei.py korrigieren
# Dann:
git add datei.py
git commit -m "Bugfix: Subtraktion korrigiert"
```

**Option 2: Den fehlerhaften Commit reverten**

```bash
git revert <commit-hash-von-commit-2>
# Editor öffnet sich, Commit-Message anpassen
```

## Visualisierung der Versionsgeschichte

Mit grafischen Tools können Sie die Historie besser visualisieren:

```bash
# Terminal-basiert
git log --oneline --graph --all --decorate

# Beispiel-Ausgabe:
* e4f5g6h (HEAD -> main) Begrüßungsfunktion hinzugefügt
* a1b2c3d Erste Version: Hallo-Welt-Skript hinzugefügt
```

Viele IDEs und Git-GUIs (z.B. GitKraken, SourceTree, VS Code) bieten grafische
Darstellungen der Historie.

## Zusammenfassung

Die wichtigsten Befehle zur Arbeit mit der Historie:

| Befehl                         | Beschreibung                            |
| ------------------------------ | --------------------------------------- |
| `git log`                      | Commit-Historie anzeigen                |
| `git log --oneline`            | Kompakte Historie                       |
| `git diff`                     | Änderungen anzeigen (Working Directory) |
| `git diff --staged`            | Änderungen in Staging Area anzeigen     |
| `git restore <datei>`          | Änderungen verwerfen                    |
| `git restore --staged <datei>` | Aus Staging Area entfernen              |
| `git checkout <commit>`        | Zu altem Commit wechseln (nur ansehen)  |
| `git revert <commit>`          | Commit rückgängig machen (neuer Commit) |

```{exercise}
:label: git-historie-navigation

**Versionsgeschichte erkunden**

Experimentieren Sie mit Ihrem Übungs-Repository:

1. Erstellen Sie 3-5 Commits mit verschiedenen Änderungen
2. Betrachten Sie die Historie mit `git log` und `git log --oneline`
3. Verwenden Sie `git diff`, um Änderungen zwischen Commits zu vergleichen
4. Machen Sie eine Änderung und verwenden Sie `git restore`, um sie rückgängig zu machen
5. Versuchen Sie, mit `git checkout` zu einem älteren Commit zu wechseln und wieder zurück

**Tipp**: Haben Sie keine Angst, zu experimentieren! Solange Sie regelmäßig
committen, können Sie immer zurück zu einem funktionierenden Stand.
```

Im nächsten Kapitel lernen Sie, wie Sie mit **Remote-Repositories** (GitHub,
GitLab) arbeiten können.
