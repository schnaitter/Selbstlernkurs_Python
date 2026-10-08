---
short_title: Best Practices
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Best Practices für die Arbeit mit Git

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

In diesem Kapitel lernen Sie bewährte Praktiken kennen – von der
{term}`Commit`-Frequenz über die {term}`Repository`-Organisation bis zur Zusammenarbeit.

## Commit-Frequenz: Wie oft committen?

### Die goldene Regel

**Committen Sie oft, aber mit Bedacht.** Ein guter Richtwert:

- **Mindestens**: Nach jeder funktionierenden Teilaufgabe
- **Höchstens**: Nicht hunderte Commits für triviale Änderungen

### ✅ Gute Commit-Punkte

- Nach Implementierung einer Funktion (auch wenn sie noch nicht perfekt ist)
- Nach jedem Bugfix
- Vor größeren Refactorings
- Am Ende einer Arbeitseinheit
- Bevor Sie einen neuen Ansatz ausprobieren

**Beispiel** – ein {term}`CSV`-Parser entsteht in mehreren Schritten:

```bash
git commit -m "CSV-Datei einlesen implementiert"
git commit -m "Spalten filtern hinzugefügt"
git commit -m "Fehlerbehandlung für ungültige Dateien"
git commit -m "Tests für Edge-Cases ergänzt"
```

### ❌ Zu große Commits vermeiden

```bash
git add .
git commit -m "Alles fertig"
# (500 Zeilen über 10 Dateien mit 5 verschiedenen Features)
```

**Problem**: Tritt ein Fehler auf, ist schwer nachzuvollziehen, welche Änderung
ihn verursacht hat.

### ❌ Zu kleine Commits vermeiden

```bash
git commit -m "Zeile 1 hinzugefügt"
git commit -m "Leerzeichen entfernt"
git commit -m "Kommentar angepasst"
```

**Problem**: Die Historie wird unübersichtlich.

### Die "logische Einheit"-Regel

Ein Commit sollte **eine logische Änderung** darstellen: eine Funktion
hinzufügen, einen Bug beheben, eine Datei umstrukturieren oder Dokumentation
erweitern.

:::::{admonition} Faustregel
:class: tip
Können Sie die Änderung in einem Satz beschreiben? Dann ist es ein guter
Commit.

- ✅ "Divisionsfunktion mit Fehlerbehandlung hinzugefügt"
- ❌ "Verschiedene Änderungen gemacht"
:::::

## Commit-Messages: Dos and Don'ts

Wie Sie gute Commit-Messages schreiben, haben Sie bereits im Kapitel
[Grundkonzepte und erste Schritte](../050-Exkurs_Git/030-Grundkonzepte_und_Erste_Schritte.md)
kennengelernt. Kurzüberblick:

**✅ Gut:**

- Kurz und prägnant (erste Zeile unter 50 Zeichen)
- Beschreibt **was** geändert wurde, im Imperativ
- Gibt Kontext (z.B. "für Umleitungsdaten")

**❌ Schlecht:**

- Zu vage ("Update", "WIP", "Änderungen")
- Unprofessionell ("asdf", "Endlich fertig!!!!")

Für komplexere Commits können Sie ohne `-m` eine längere Beschreibung im
Editor ergänzen (erste Zeile Zusammenfassung, Leerzeile, Details, optional
Issue-Verweis wie `Closes #42`).

## Repository-Organisation

### Gute Dateistruktur

```
mein-projekt/
├── README.md              # Projektbeschreibung
├── requirements.txt       # Python-Abhängigkeiten
├── .gitignore            # Ignorierte Dateien
├── src/                  # Quellcode
├── tests/                # Tests
├── docs/                 # Dokumentation
└── data/                 # Beispieldaten (klein!)
```

### README.md erstellen

Jedes Projekt sollte eine README haben:

```markdown
# Projekt-Name

Kurze Beschreibung, was das Projekt macht.

## Installation

\```bash
pip install -r requirements.txt
\```

## Verwendung

\```bash
python src/main.py
\```

## Lizenz

MIT
```

:::::{note} Hinweis
Die Überschriften innerhalb des Codeblocks (Installation, Verwendung, Lizenz)
sind Teil des README-Beispiels und keine Kapitel dieses Kurses.
:::::

## Zusammenarbeit: Kommunikation ist wichtig

1. **Regelmäßig pullen**: Vor Arbeitsbeginn `git pull` ausführen
2. **Regelmäßig pushen**: Fertige Commits zeitnah hochladen
3. **Aussagekräftige Messages**: Kolleg\*innen verstehen, was Sie getan haben
4. **Kleine Commits**: Einfacher zu reviewen
5. **Branches nutzen**: Feature-Branches für größere Änderungen

**Kommunikations-Checkliste:**

- [ ] Morgens: `git pull` ausführen
- [ ] Features in separaten Branches entwickeln
- [ ] Commits mit klaren Messages versehen
- [ ] Vor Feierabend: Änderungen pushen

## Weiterführende Ressourcen

**Online-Tutorials:**

- [Pro Git Buch (kostenlos)](https://git-scm.com/book/de/v2)
- [GitHub Learning Lab](https://github.com/apps/github-learning-lab)
- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials)

**Visualisierungen:**

- [Visualizing Git](https://git-school.github.io/visualizing-git/)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=de_DE)

**Git-GUIs** (falls Sie lieber grafisch arbeiten):

- [GitKraken](https://www.gitkraken.com/)
- [SourceTree](https://www.sourcetreeapp.com/)
- VS Code: Eingebaute Git-Integration

## Zusammenfassung

- ✅ Häufig committen (nach jeder logischen Einheit)
- ✅ Aussagekräftige Messages schreiben, kleine Commits
- ✅ Regelmäßig pullen und pushen, Feature-{term}`Branch`es nutzen
- ❌ Keine riesigen "Alles-auf-einmal"-Commits
- ❌ Nicht direkt auf `main` arbeiten bei Team-Projekten

:::::{admonition} Ihr Weg zu Git-Kompetenz
:class: success
{term}`Git`-Expertise entsteht durch Übung. Die wichtigsten Tipps:

1. **Keine Angst vor Fehlern**: Solange Sie committen, können Sie (fast) nichts
   kaputt machen
2. **`git status` ist Ihr Freund**: Bei Unsicherheit immer zuerst Status prüfen
3. **Klein anfangen**: Nutzen Sie zunächst nur die Basics und erweitern Sie
   schrittweise
:::::
