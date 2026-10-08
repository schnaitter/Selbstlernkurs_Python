---
short_title: Rückgängig machen
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Änderungen rückgängig machen

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

Fehler passieren. Git ist gerade deshalb so wertvoll, weil Sie fast jede
Änderung rückgängig machen können. Dieses Kapitel zeigt die wichtigsten
Möglichkeiten – von einzelnen Dateien bis zu ganzen Commits.

## Zu früheren Versionen zurückkehren

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

### 3. Einen früheren Zustand ansehen: git checkout

Sie können sich einen früheren Zustand des Projekts ansehen:

```bash
git checkout a1b2c3d
```

:::::{margin}
**Detached HEAD**: Wenn Sie zu einem alten Commit wechseln, befinden Sie sich
im "detached HEAD"-Zustand. Das bedeutet, Sie sehen den alten Zustand, arbeiten
aber nicht mehr auf einem {term}`Branch`. Mit `git checkout main` (oder dem Namen Ihres
Branches) kommen Sie zurück.
:::::

**Was passiert?** Alle Dateien werden auf den Zustand von Commit `a1b2c3d`
zurückgesetzt.

### 4. Eine Datei auf einen alten Stand zurücksetzen

**Szenario**: Sie möchten eine Datei auf einen früheren Stand zurücksetzen,
aber als neuen Commit speichern.

```bash
# Datei auf Stand von Commit a1b2c3d zurücksetzen
git checkout a1b2c3d -- hallo.py

# Als neuen Commit speichern
git commit -m "Datei auf früheren Stand zurückgesetzt"
```

Das `--` trennt Commit-Hashes von Dateinamen.

## Einen {term}`Commit` rückgängig machen: git revert

**Szenario**: Ein Commit hat einen Fehler eingeführt. Sie möchten ihn
rückgängig machen, aber die Historie nicht verändern.

```bash
git revert e4f5g6h
```

{term}`Git` erstellt einen **neuen Commit**, der die Änderungen von `e4f5g6h`
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
Der Befehl `git reset` wird in diesem Kurs bewusst nicht im Detail behandelt.
Er kann die Historie verändern und ist fehleranfällig. Für den Einstieg reichen
`restore` und `revert` vollkommen aus.
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

:::::{admonition} Faustregel
:class: tip
- **Noch nicht committed?** → `git restore`
- **Bereits committed, aber nicht gepusht?** → `git revert` (sicher) oder im
  Ausnahmefall `git commit --amend` für die letzte Commit-Message
- **Bereits gepusht?** → ausschließlich `git revert`, damit die Historie für
  alle Beteiligten konsistent bleibt
:::::

## Zusammenfassung

| Befehl                         | Beschreibung                            |
| ------------------------------ | --------------------------------------- |
| `git restore <datei>`          | Änderungen verwerfen                    |
| `git restore --staged <datei>` | Aus Staging Area entfernen              |
| `git checkout <commit>`        | Zu altem Commit wechseln (nur ansehen)  |
| `git revert <commit>`          | Commit rückgängig machen (neuer Commit) |

Im nächsten Kapitel geht es um Best Practices und darum, wie Sie typische
Fehler von vornherein vermeiden.
