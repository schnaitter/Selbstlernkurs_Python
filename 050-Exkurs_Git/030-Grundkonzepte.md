---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Grundkonzepte von Git

Bevor wir mit Git arbeiten, ist es wichtig, die grundlegenden Konzepte zu verstehen. Git verwendet eine eigene Terminologie, die zunächst ungewohnt wirken kann – aber die Konzepte dahinter sind logisch und nachvollziehbar.

## Repository (Projektarchiv)

Ein **Repository** (oft abgekürzt als "Repo") ist ein Projektordner, den Git überwacht. Es enthält:
- Alle Ihre Dateien (Python-Skripte, Daten, Dokumentation)
- Die gesamte Versionsgeschichte (wer hat wann was geändert)
- Git-Konfiguration (im versteckten Ordner `.git`)

Ein Repository kann lokal auf Ihrem Computer oder remote auf einem Server (GitHub, GitLab) liegen.

:::::{margin}
**Wichtig**: Der `.git`-Ordner enthält alle Versionsinformationen. Löschen Sie diesen Ordner nie, sonst verlieren Sie die gesamte Versionsgeschichte!
:::::

## Die drei Bereiche in Git

Git arbeitet mit drei wichtigen Bereichen. Das Verständnis dieser Bereiche ist zentral für die Arbeit mit Git:

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

Das **Working Directory** ist Ihr normaler Projektordner – so wie Sie ihn im Dateimanager sehen. Hier bearbeiten Sie Ihre Dateien mit Ihrem Texteditor oder Ihrer IDE.

**Beispiel**: Sie öffnen `taschenrechner.py` in VS Code und fügen eine neue Funktion hinzu. Diese Änderung befindet sich zunächst nur im Working Directory.

### 2. Staging Area (Bereitstellungsbereich)

Die **Staging Area** ist ein Zwischenbereich. Hier sammeln Sie alle Änderungen, die Sie in den nächsten Commit aufnehmen möchten.

**Warum braucht man das?** Stellen Sie sich vor, Sie haben an mehreren Dateien gearbeitet:
- `taschenrechner.py`: Neue Funktion für Division
- `statistik.py`: Bugfix
- `dokumentation.md`: Rechtschreibfehler korrigiert

Mit der Staging Area können Sie entscheiden: "Ich möchte nur die Änderungen an `taschenrechner.py` und `statistik.py` committen, aber `dokumentation.md` erst später." So können Sie thematisch zusammengehörige Änderungen bündeln.

**Befehl**: `git add dateiname` fügt eine Datei zur Staging Area hinzu.

### 3. Repository / Versionsgeschichte

Wenn Sie einen **Commit** erstellen, werden alle Änderungen aus der Staging Area dauerhaft in der Versionsgeschichte gespeichert. Ein Commit ist wie ein Schnappschuss Ihres Projekts zu einem bestimmten Zeitpunkt.

**Befehl**: `git commit -m "Beschreibung"` erstellt einen Commit.

## Was ist ein Commit?

Ein **Commit** ist eine gespeicherte Version Ihres Projekts. Jeder Commit enthält:

- **Änderungen**: Was wurde geändert (z.B. "Zeile 42 in `taschenrechner.py` hinzugefügt")
- **Commit-Message**: Kurze Beschreibung der Änderung (z.B. "Divisionsfunktion hinzugefügt")
- **Metadaten**: Autor\*in, Zeitstempel, eindeutige ID (Hash)
- **Verweis auf vorherigen Commit**: Commits bilden eine Kette

::::{grid}
:gutter: 2

:::{grid-item-card} Commit 1
**Hash**: `a1b2c3d`
**Autor**: Erika Mustermann
**Datum**: 2025-10-15
**Message**: "Projekt initialisiert"
:::

:::{grid-item-card} Commit 2
**Hash**: `e4f5g6h`
**Autor**: Erika Mustermann
**Datum**: 2025-10-16
**Message**: "Addition implementiert"
**Parent**: `a1b2c3d`
:::

:::{grid-item-card} Commit 3
**Hash**: `i7j8k9l`
**Autor**: Erika Mustermann
**Datum**: 2025-10-17
**Message**: "Division hinzugefügt"
**Parent**: `e4f5g6h`
:::

::::

Commits bilden eine **Kette**: Jeder Commit zeigt auf seinen Vorgänger. So entsteht eine Timeline der Projektentwicklung.

## Visualisierung: Der Git-Workflow

Hier ein typischer Arbeitsablauf mit Git:

```{mermaid}
sequenceDiagram
    participant WD as Working Directory
    participant SA as Staging Area
    participant Repo as Repository

    Note over WD: Datei bearbeiten
    WD->>SA: git add datei.py
    Note over SA: Änderung bereitgestellt

    Note over WD: Weitere Datei bearbeiten
    WD->>SA: git add datei2.py
    Note over SA: Beide bereitgestellt

    SA->>Repo: git commit -m "Neue Funktionen"
    Note over Repo: Version gespeichert

    Note over WD: Weiter arbeiten...
```

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
- `taschenrechner.py` ist in der Staging Area → wird beim nächsten Commit gespeichert
- `dokumentation.md` wurde geändert, aber noch nicht zur Staging Area hinzugefügt
- `testdaten.csv` ist eine neue Datei, die Git noch nicht kennt

## Zusammenfassung der Konzepte

| Konzept | Beschreibung |
|---------|--------------|
| **Repository** | Projektordner mit Versionsgeschichte |
| **Working Directory** | Ihr aktueller Arbeitsbereich |
| **Staging Area** | Änderungen, die für den nächsten Commit vorgemerkt sind |
| **Commit** | Gespeicherter Schnappschuss des Projekts |
| **git status** | Zeigt den aktuellen Zustand aller drei Bereiche |

:::::{admonition} Verständnis-Check
:class: tip
Beantworten Sie für sich selbst:
1. Was ist der Unterschied zwischen Working Directory und Repository?
2. Warum gibt es eine Staging Area – könnte man nicht direkt committen?
3. Was enthält ein Commit?

Antworten:
1. Working Directory = aktuelle Dateien, die Sie bearbeiten; Repository = gespeicherte Versionsgeschichte
2. Die Staging Area ermöglicht selektives Committen: Sie können aus vielen Änderungen gezielt auswählen, was zusammen gespeichert werden soll
3. Ein Commit enthält Änderungen, eine Beschreibung (Message), Metadaten (Autor, Zeit) und einen Verweis auf den vorherigen Commit
:::::

Im nächsten Kapitel setzen wir diese Konzepte in die Praxis um und erstellen unser erstes Repository!
