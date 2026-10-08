---
short_title: Historie
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

- **{term}`Commit`-Hash**: Eindeutige ID (lange Hexadezimalzahl)
- **Author**: Name und E-Mail der Person, die den Commit erstellt hat
- **Date**: Zeitstempel
- **Commit-Message**: Beschreibung der Änderung
- **(HEAD -> main)**: Zeigt an, wo Sie sich gerade befinden

:::::{margin}
**HEAD** ist ein Zeiger auf den aktuell ausgecheckten Commit (normalerweise der
neueste {term}`Commit` auf Ihrem aktuellen {term}`Branch`).
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

```bash
# Zwei Commits vergleichen
git diff a1b2c3d e4f5g6h

# Aktuellen Zustand mit einem früheren Commit vergleichen
git diff a1b2c3d
```

## Einen Commit rückgängig machen: git revert

**Szenario**: Ein Commit hat einen Fehler eingeführt. Sie möchten ihn
rückgängig machen, aber die Historie nicht verändern.

```bash
git revert e4f5g6h
```

{term}`Git` erstellt einen **neuen Commit**, der die Änderungen von `e4f5g6h`
rückgängig macht. Die Historie bleibt erhalten – das ist wichtig, wenn Sie
bereits mit anderen Personen zusammenarbeiten.

:::::{note} Weitere Möglichkeiten
Wie Sie einzelne Dateien wiederherstellen, zu alten Ständen wechseln oder
`restore`, `revert` und `reset` unterscheiden, lesen Sie im Vertiefungskapitel
[Änderungen rückgängig machen](../095-Exkurs_Git_Vertiefung/040-Rueckgaengig_machen.md).
:::::

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

| Befehl              | Beschreibung                            |
| ------------------- | --------------------------------------- |
| `git log`           | Commit-Historie anzeigen                |
| `git log --oneline` | Kompakte Historie                       |
| `git diff`          | Änderungen anzeigen (Working Directory) |
| `git diff --staged` | Änderungen in Staging Area anzeigen     |
| `git revert <commit>` | Commit rückgängig machen (neuer Commit) |

```{exercise}
:label: git-historie-navigation

**Versionsgeschichte erkunden**

Experimentieren Sie mit Ihrem Übungs-Repository:

1. Erstellen Sie 3–5 Commits mit verschiedenen Änderungen
2. Betrachten Sie die Historie mit `git log` und `git log --oneline`
3. Verwenden Sie `git diff`, um Änderungen zwischen Commits zu vergleichen
4. Machen Sie eine Änderung und verwenden Sie `git revert`, um einen Commit
   rückgängig zu machen

**Tipp**: Haben Sie keine Angst, zu experimentieren! Solange Sie regelmäßig
committen, können Sie immer zurück zu einem funktionierenden Stand.
```

Im nächsten Kapitel lernen Sie, wie Sie Git konkret **in diesem Kurs**
einsetzen.
