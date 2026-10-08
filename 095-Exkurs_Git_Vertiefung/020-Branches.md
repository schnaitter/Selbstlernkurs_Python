---
short_title: Branches
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Branches (Zweige)

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

{term}`Branch`es (deutsch: Zweige) gehören zu den mächtigsten Features von {term}`Git`. Sie
erlauben es, parallel an verschiedenen Versionen eines Projekts zu arbeiten.

## Was ist ein Branch?

Ein **Branch** ist ein unabhängiger Entwicklungszweig – eine alternative
Timeline, in der Sie experimentieren können, ohne die Hauptversion zu
beeinflussen.

**Metapher**: Ein Baum (Tree) mit mehreren Ästen:

- Der Hauptstamm ist der `main`-Branch
- Von diesem Stamm zweigen Äste ab (Feature-Branches)
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

- **Neue Funktion entwickeln**: In einem eigenen Branch experimentieren; klappt
  es, wird gemergt, sonst wird der Branch gelöscht und `main` bleibt unberührt.
- **Zusammenarbeit**: Jede\*r arbeitet in einem eigenen Branch; `main` bleibt
  stabil.
- **Verschiedene Versionen**: Stabile Version (`main`), Entwicklungsversion
  (`develop`) und Experimente parallel pflegen.

## Branches anzeigen

```bash
git branch        # lokale Branches
git branch -a     # zusätzlich Remote-Branches
```

**Ausgabe:**

```
* main
  feature-statistik
  bugfix-datum
```

Der `*` zeigt den aktuellen Branch an.

## Branch erstellen und wechseln

```bash
git branch feature-export        # nur erstellen, nicht wechseln
git checkout feature-export      # zu einem Branch wechseln
git checkout -b feature-export   # erstellen + direkt wechseln
```

Das `-b` steht für "branch". Alle {term}`Commit`s, die Sie jetzt erstellen, werden nur
in diesem Branch gespeichert.

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
echo "def exportiere_daten():\n    pass" > export.py
git add export.py
git commit -m "Export-Funktion angelegt"
```

Dieser Commit existiert jetzt nur im Branch `feature-export`, nicht in `main`!

Wechseln Sie zurück zu `main`, verschwindet `export.py` aus dem
Arbeitsverzeichnis. Wechseln Sie wieder zu `feature-export`, ist sie wieder da –
Git tauscht die Dateien passend zum Branch aus.

## Branches zusammenführen (Merge)

Wenn Sie mit Ihrer Arbeit im Feature-Branch zufrieden sind, führen Sie ihn mit
`main` zusammen:

```bash
git checkout main           # 1. zu main wechseln
git merge feature-export    # 2. Feature mergen
git branch -d feature-export  # 3. Branch löschen (optional)
```

**Was passiert beim Merge?** Git fügt alle Commits aus `feature-export` in
`main` ein.

**Fast-Forward Merge**: `main` hatte keine eigenen Änderungen, Git schiebt
`main` einfach vorwärts zu den neuen Commits. Haben beide Branches eigene
Commits, erstellt Git einen **Merge-Commit** – dabei kann es zu Merge-Konflikten
kommen, siehe [Merge-Konflikte auflösen](030-Merge_Konflikte.md).

## Wann sind Branches sinnvoll?

**Gute Anwendungsfälle:**

- **Neue Features**: Jedes Feature bekommt einen eigenen Branch
- **Bugfixes**: Kritische Bugs in einem separaten Branch beheben
- **Experimente**: Ausprobieren ohne Angst vor Schäden am Hauptcode
- **Zusammenarbeit**: Jede\*r arbeitet in eigenem Branch

**Weniger sinnvoll:**

- Für jeden Commit einen Branch (zu viele Branches = unübersichtlich)
- Branches niemals mergen
- Bei sehr kleinen Solo-Projekten reicht oft `main`

## Branch-Strategien

Es gibt verschiedene Konventionen, wie man Branches benennt und organisiert:

**Einfaches Modell (für Anfänger\*innen):**

```
main            → Stabiler Haupt-Branch
feature-xyz     → Neue Features
bugfix-abc      → Fehlerbehebungen
experiment-*    → Experimente
```

**Git Flow (für größere Projekte):**

```
main            → Produktionsversion
develop         → Entwicklungsversion
feature/xyz     → Feature-Branches
hotfix/abc      → Dringende Bugfixes
release/v1.0    → Release-Vorbereitung
```

Für Ihren Einstieg reicht das einfache Modell!

## Zusammenfassung

| Befehl                   | Beschreibung                      |
| ------------------------ | --------------------------------- |
| `git branch`             | Branches anzeigen                 |
| `git branch <name>`      | Neuen Branch erstellen            |
| `git checkout <name>`    | Zu Branch wechseln                |
| `git checkout -b <name>` | Branch erstellen und wechseln     |
| `git merge <name>`       | Branch in aktuellen Branch mergen |
| `git branch -d <name>`   | Branch löschen                    |

```{exercise}
:label: git-branches-experimentieren
**Mit Branches experimentieren**

1. Erstellen Sie einen Branch `experiment-test`
2. Erstellen Sie darin eine Datei und committen Sie sie
3. Wechseln Sie zurück zu `main` – die Datei ist weg
4. Wechseln Sie wieder zu `experiment-test` – die Datei ist wieder da
5. Mergen Sie `experiment-test` in `main` und löschen Sie den Branch

Verwenden Sie `git log --oneline --graph --all`, um die Branch-Struktur zu
visualisieren!
```

Im nächsten Kapitel sehen Sie, wie Sie **Merge-Konflikte** Schritt für Schritt
auflösen.
