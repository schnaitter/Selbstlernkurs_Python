---
numbering:
    heading_1: false
    heading_2: true
    title: false
---

# Branches (Zweige)

**Branches** (deutsch: Zweige) gehören zu den mächtigsten Features von Git. Sie erlauben es, parallel an verschiedenen Versionen eines Projekts zu arbeiten.

## Was ist ein Branch?

Ein **Branch** ist ein unabhängiger Entwicklungszweig. Stellen Sie sich einen Branch wie eine alternative Timeline vor, in der Sie experimentieren können, ohne die Hauptversion zu beeinflussen.

**Metapher**: Ein Baum (Tree) mit mehreren Ästen (Branches):
- Der Hauptstamm ist der `main`-Branch
- Von diesem Stamm können Äste abzweigen (Feature-Branches)
- Diese Äste können später wieder zusammengeführt werden (Merge)

```{mermaid}
gitGraph
    commit id: "Initial commit"
    commit id: "Add function"
    branch feature-x
    commit id: "Start feature X"
    commit id: "Implement feature X"
    checkout main
    commit id: "Bugfix"
    checkout feature-x
    commit id: "Finish feature X"
    checkout main
    merge feature-x
    commit id: "Continue development"
```

## Warum Branches?

### Szenario 1: Neue Funktion entwickeln

Sie arbeiten an einem Projekt und möchten eine neue Funktion ausprobieren, sind aber nicht sicher, ob sie funktioniert. Mit Branches können Sie:

1. Einen neuen Branch erstellen (z.B. `feature-statistik`)
2. In diesem Branch experimentieren
3. Falls es funktioniert: Zurück zu `main` und den Branch mergen
4. Falls nicht: Branch einfach löschen, `main` bleibt unberührt

### Szenario 2: Zusammenarbeit

Mehrere Personen arbeiten am selben Projekt:
- Person A arbeitet am Branch `feature-export`
- Person B arbeitet am Branch `bugfix-import`
- Der `main`-Branch bleibt stabil
- Fertige Features werden einzeln in `main` integriert

### Szenario 3: Verschiedene Versionen

Sie entwickeln ein Tool und möchten:
- Eine stabile Version (`main`)
- Eine Entwicklungsversion mit neuen Features (`develop`)
- Verschiedene Experimente (`experiment-xyz`)

## Branches anzeigen

Alle lokalen Branches anzeigen:

```bash
git branch
```

**Ausgabe:**
```
* main
  feature-statistik
  bugfix-datum
```

Der `*` zeigt den aktuellen Branch an.

Auch Remote-Branches anzeigen:

```bash
git branch -a
```

## Einen neuen Branch erstellen

```bash
git branch feature-export
```

Dieser Befehl erstellt einen neuen Branch namens `feature-export`, wechselt aber noch nicht zu ihm.

## Zu einem Branch wechseln

```bash
git checkout feature-export
```

Jetzt arbeiten Sie im Branch `feature-export`. Alle Commits, die Sie jetzt erstellen, werden nur in diesem Branch gespeichert.

### Branch erstellen und direkt wechseln

Häufig möchte man beides auf einmal:

```bash
git checkout -b feature-export
```

Das `-b` steht für "branch" und bedeutet: "Erstelle einen neuen Branch und wechsle direkt zu ihm."

:::::{margin}
**Neuere Syntax**: In neueren Git-Versionen gibt es auch `git switch`:
```bash
git switch feature-export        # Wechseln
git switch -c feature-export     # Erstellen + wechseln
```
:::::

## In einem Branch arbeiten

Angenommen, Sie sind im Branch `feature-export`:

```bash
# Branch anzeigen
git branch
# * feature-export
#   main

# Datei erstellen und ändern
echo "def exportiere_daten():\n    pass" > export.py

# Committen
git add export.py
git commit -m "Export-Funktion angelegt"
```

Dieser Commit existiert jetzt nur im Branch `feature-export`, nicht in `main`!

## Zwischen Branches wechseln

Wechseln Sie zurück zu `main`:

```bash
git checkout main
```

**Was passiert?**
- Alle Dateien werden auf den Stand von `main` zurückgesetzt
- `export.py` ist verschwunden (existiert nur in `feature-export`)

Wechseln Sie wieder zu `feature-export`:

```bash
git checkout feature-export
```

**Was passiert?**
- `export.py` ist wieder da!

## Branches zusammenführen (Merge)

Wenn Sie mit Ihrer Arbeit im Feature-Branch zufrieden sind, möchten Sie ihn mit `main` zusammenführen.

### Schritt 1: Zu main wechseln

```bash
git checkout main
```

### Schritt 2: Den Feature-Branch mergen

```bash
git merge feature-export
```

**Was passiert?**
Git fügt alle Commits aus `feature-export` in `main` ein.

**Beispiel-Ausgabe (Fast-Forward Merge):**
```
Updating a1b2c3d..e4f5g6h
Fast-forward
 export.py | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 export.py
```

Ein **Fast-Forward Merge** bedeutet: `main` hatte keine eigenen Änderungen, Git schiebt `main` einfach vorwärts zu den neuen Commits.

### Schritt 3: Branch löschen (optional)

Nach erfolgreichem Merge können Sie den Feature-Branch löschen:

```bash
git branch -d feature-export
```

Das `-d` steht für "delete". Git fragt sicherheitshalber nach, wenn der Branch noch nicht gemerged wurde.

## Visualisierung: Branch-Workflow

```{mermaid}
gitGraph
    commit id: "A"
    commit id: "B"
    branch feature
    checkout feature
    commit id: "C (feature)"
    commit id: "D (feature)"
    checkout main
    commit id: "E (main)"
    checkout feature
    commit id: "F (feature)"
    checkout main
    merge feature tag: "Merge!"
    commit id: "G"
```

## Wann sind Branches sinnvoll?

### ✅ Gute Anwendungsfälle

- **Neue Features entwickeln**: Jedes neue Feature bekommt einen eigenen Branch
- **Bugfixes**: Kritische Bugs in einem separaten Branch beheben
- **Experimente**: Ausprobieren ohne Angst vor Schäden am Hauptcode
- **Zusammenarbeit**: Jede\*r arbeitet in eigenem Branch

### ❌ Weniger sinnvoll

- **Für jeden Commit einen Branch**: Zu viele Branches führen zu Unübersichtlichkeit
- **Niemals mergen**: Branches sollten irgendwann wieder zusammengeführt werden
- **Bei sehr kleinen Solo-Projekten**: Wenn Sie alleine an einem kleinen Skript arbeiten, reicht oft der `main`-Branch

## Branch-Strategien

Es gibt verschiedene Konventionen, wie man Branches benennt und organisiert:

### Einfaches Modell (für Anfänger)

```
main            → Stabiler Haupt-Branch
feature-xyz     → Neue Features
bugfix-abc      → Fehlerbehebungen
experiment-*    → Experimente
```

### Git Flow (für größere Projekte)

```
main            → Produktionsversion
develop         → Entwicklungsversion
feature/xyz     → Feature-Branches
hotfix/abc      → Dringende Bugfixes
release/v1.0    → Release-Vorbereitung
```

Für Ihren Einstieg reicht das einfache Modell!

## Merge-Konflikte (Überblick)

Ein **Merge-Konflikt** entsteht, wenn:
- Zwei Branches dieselbe Zeile in derselben Datei ändern
- Git nicht automatisch entscheiden kann, welche Änderung behalten werden soll

:::::{admonition} Konflikte in diesem Kurs
:class: note
Die Auflösung von Merge-Konflikten ist ein fortgeschrittenes Thema und wird in diesem Einsteigerkurs bewusst **nicht praktisch behandelt**.

**Warum?** Wenn Sie alleine an Ihren Projekten arbeiten, entstehen Konflikte sehr selten. Falls doch:
1. Bleiben Sie ruhig – nichts ist kaputt
2. Git zeigt an, in welchen Dateien Konflikte sind
3. Öffnen Sie die Datei – Git markiert die Konfliktstellen
4. Entscheiden Sie, welche Version Sie behalten möchten
5. Committen Sie die Auflösung

**Tipp**: Viele IDEs (wie VS Code) haben eingebaute Tools zur Konfliktauflösung.
:::::

## Praktisches Beispiel

Ein vollständiges Beispiel: Feature entwickeln, mergen, Branch löschen.

```bash
# 1. Neuen Branch erstellen und wechseln
git checkout -b feature-statistik

# 2. Im Feature-Branch arbeiten
echo "def statistik():\n    pass" > statistik.py
git add statistik.py
git commit -m "Statistik-Funktion angelegt"

# 3. Weiterarbeiten
echo "    print('Statistik')" >> statistik.py
git add statistik.py
git commit -m "Statistik-Ausgabe implementiert"

# 4. Zurück zu main
git checkout main

# 5. Feature-Branch mergen
git merge feature-statistik

# 6. Branch löschen (da fertig)
git branch -d feature-statistik

# 7. Prüfen, dass nur noch main existiert
git branch
```

## Zusammenfassung

Die wichtigsten Branch-Befehle:

| Befehl | Beschreibung |
|--------|--------------|
| `git branch` | Branches anzeigen |
| `git branch <name>` | Neuen Branch erstellen |
| `git checkout <name>` | Zu Branch wechseln |
| `git checkout -b <name>` | Branch erstellen und wechseln |
| `git merge <name>` | Branch in aktuellen Branch mergen |
| `git branch -d <name>` | Branch löschen |

### Typischer Feature-Workflow

```bash
git checkout -b feature-xyz      # Branch erstellen
# ... arbeiten und committen ...
git checkout main                # Zurück zu main
git merge feature-xyz            # Feature mergen
git branch -d feature-xyz        # Branch löschen
```

:::::{admonition} Übung
:class: warning
Experimentieren Sie mit Branches:

1. Erstellen Sie einen Branch `experiment-test`
2. Erstellen Sie darin eine Datei und committen Sie sie
3. Wechseln Sie zurück zu `main` – die Datei ist weg
4. Wechseln Sie wieder zu `experiment-test` – die Datei ist wieder da
5. Mergen Sie `experiment-test` in `main`
6. Löschen Sie den Branch `experiment-test`

Verwenden Sie `git log --oneline --graph --all`, um die Branch-Struktur zu visualisieren!
:::::

Im nächsten Kapitel lernen Sie, wie Sie Git konkret **in diesem Kurs** einsetzen können.
