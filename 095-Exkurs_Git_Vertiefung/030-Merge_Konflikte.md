---
short_title: Merge-Konflikte
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Merge-Konflikte auflösen

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

:::{admonition} Fortgeschrittenes Thema
:class: warning
Merge-Konflikte treten meist erst auf, wenn mehrere Personen am selben Projekt
arbeiten oder wenn Sie längere Zeit parallel in verschiedenen Branches
entwickeln. Wenn Sie alleine arbeiten und regelmäßig committen, begegnen Ihnen
Konflikte selten. Dieses Kapitel zeigt, wie Sie ruhig und systematisch
vorgehen, falls es doch passiert.
:::

## Was ist ein Merge-Konflikt?

Git kann die meisten Änderungen automatisch zusammenführen. Ein
**Merge-Konflikt** entsteht, wenn {term}`Git` nicht entscheiden kann, welche Version
behalten werden soll. Das passiert typischerweise, wenn:

- zwei {term}`Branch`es **dieselbe Zeile in derselben Datei** unterschiedlich ändern
- eine Person eine Datei löscht, die eine andere Person bearbeitet
- beide Seiten dieselbe Datei an derselben Stelle umbenennen

:::::{note} Grundregel für Alleinarbeit
Wenn Sie alleine arbeiten und Git meldet einen Konflikt, haben Sie
wahrscheinlich vergessen, vor dem Arbeiten `git pull` auszuführen. Die Regel
lautet: **erst `git pull`, dann arbeiten, dann `git push`.**
:::::

## Ein konkretes Beispiel

Ausgangspunkt ist die Datei `statistik.py` mit dieser Funktion:

```python
def durchschnitt(werte):
    return sum(werte) / len(werte)
```

**Person A** ändert im Branch `feature-statistik` die Rückgabe:

```python
def durchschnitt(werte):
    return round(sum(werte) / len(werte), 2)
```

**Person B** ändert auf `main` dieselbe Zeile anders:

```python
def durchschnitt(werte):
    return sum(werte) / max(len(werte), 1)
```

Führt Person A nun `git merge main` aus (oder umgekehrt), kann Git nicht
entscheiden, welche der beiden Zeilen korrekt ist. Der Merge wird angehalten
und die betroffene Datei mit **Konfliktmarkern** versehen.

## Konfliktmarker erkennen

Öffnen Sie die betroffene Datei nach der Meldung. Sie sieht dann so aus:

```python
def durchschnitt(werte):
<<<<<<< HEAD
    return round(sum(werte) / len(werte), 2)
=======
    return sum(werte) / max(len(werte), 1)
>>>>>>> main
```

Die Marker bedeuten:

- `<<<<<<< HEAD`: Beginn Ihrer eigenen Version (der Branch, auf dem Sie stehen)
- `=======`: Trennlinie zwischen den beiden Versionen
- `>>>>>>> main`: Ende der Version, die aus dem anderen Branch kommt

## Einen Konflikt auflösen

1. **Ruhig bleiben**: Nichts ist kaputt – Git wartet auf Ihre Entscheidung.
2. **Betroffene Dateien finden**: `git status` zeigt sie unter
   "Unmerged paths" an.
3. **Datei öffnen und Marker bearbeiten**: Entscheiden Sie, welche Version
   (oder eine Mischung) richtig ist, und entfernen Sie die Marker-Zeilen
   (`<<<<<<<`, `=======`, `>>>>>>>`).

Für das Beispiel könnte das Ergebnis so aussehen:

```python
def durchschnitt(werte):
    return round(sum(werte) / max(len(werte), 1), 2)
```

4. **Als aufgelöst markieren und committen**:

```bash
git add statistik.py
git commit -m "Merge-Konflikt in durchschnitt() aufgelöst"
```

Git erstellt damit den Merge-{term}`Commit` und schließt den Merge ab.

## Einen Merge abbrechen

Wenn Ihnen die Situation zu unübersichtlich wird, können Sie den Merge
vollständig abbrechen und zum Zustand vor dem Merge zurückkehren:

```bash
git merge --abort
```

## Tipps zur Konfliktauflösung

- **Hilfe aus der IDE**: VS Code, PyCharm und andere Editoren zeigen Konflikte
  farbig an und bieten Buttons wie "Accept Current", "Accept Incoming" oder
  "Accept Both".
- **Kleine Commits**: Wer häufig und in kleinen Schritten committet, bekommt
  kleinere und leichter zu lesende Konflikte.
- **Vor dem Mergen aktualisieren**: Bringen Sie Ihren Branch zuerst mit
  `git pull` auf den neuesten Stand – so sehen Sie Konflikte früh.
- **Miteinander sprechen**: Bei Teamarbeit ist oft eine kurze Absprache die
  schnellste Lösung.
- **`git log --merge` und `git diff`**: Helfen, die konkurrierenden Änderungen
  zu verstehen.

## Zusammenfassung

```bash
# Status zeigt die betroffenen Dateien
git status

# Datei bearbeiten, Marker entfernen, dann:
git add <datei>
git commit -m "Merge-Konflikt aufgelöst"

# Oder den Merge komplett abbrechen:
git merge --abort
```

Merge-Konflikte sind kein Fehler, sondern ein normaler Teil der Zusammenarbeit.
Mit etwas Übung werden sie zur Routine.
