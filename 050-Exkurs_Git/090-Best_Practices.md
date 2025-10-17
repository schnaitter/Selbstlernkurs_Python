---
numbering:
    heading_1: false
    heading_2: true
    title: false
---

# Best Practices und Sicherheit

In diesem Kapitel lernen Sie bewährte Praktiken für die Arbeit mit Git kennen – von der Commit-Frequenz bis zur Sicherheit.

## Commit-Frequenz: Wie oft committen?

### Die goldene Regel

**Committen Sie oft, aber mit Bedacht.**

Ein guter Richtwert:
- **Mindestens**: Nach jeder funktionierenden Teilaufgabe
- **Höchstens**: Nicht hunderte Commits für triviale Änderungen

### ✅ Gute Commit-Punkte

- Nach Implementierung einer Funktion (auch wenn sie noch nicht perfekt ist)
- Nach jedem Bugfix
- Vor größeren Refactorings
- Am Ende einer Arbeitseinheit
- Bevor Sie einen neuen Ansatz ausprobieren

**Beispiel**: Sie schreiben einen CSV-Parser:

```bash
git commit -m "CSV-Datei einlesen implementiert"
git commit -m "Spalten filtern hinzugefügt"
git commit -m "Fehlerbehandlung für ungültige Dateien"
git commit -m "Tests für Edge-Cases ergänzt"
```

### ❌ Zu große Commits vermeiden

```bash
# Schlecht:
git add .
git commit -m "Alles fertig"
# (Enthält 500 Zeilen über 10 Dateien mit 5 verschiedenen Features)
```

**Problem**: Wenn ein Fehler auftritt, ist schwer nachzuvollziehen, welche Änderung ihn verursacht hat.

### ❌ Zu kleine Commits vermeiden

```bash
# Übertrieben:
git commit -m "Zeile 1 hinzugefügt"
git commit -m "Zeile 2 hinzugefügt"
git commit -m "Leerzeichen entfernt"
git commit -m "Kommentar angepasst"
```

**Problem**: Die Historie wird unübersichtlich.

### Die "logische Einheit"-Regel

Ein Commit sollte **eine logische Änderung** darstellen:

- Eine Funktion hinzufügen
- Einen Bug beheben
- Eine Datei umstrukturieren
- Dokumentation erweitern

:::::{admonition} Faustregel
:class: tip
Können Sie die Änderung in einem Satz beschreiben? Dann ist es ein guter Commit.

- ✅ "Divisionsfunktion mit Fehlerbehandlung hinzugefügt"
- ✅ "Bug bei leeren Eingaben behoben"
- ❌ "Verschiedene Änderungen gemacht"
:::::

## Commit-Messages: Dos and Don'ts

### ✅ Gute Commit-Messages

```
Begrüßungsfunktion mit Parameterisierung hinzugefügt

CSV-Import für Umleitungsdaten implementiert

Bugfix: Division durch Null abgefangen

Dokumentation für Installationsprozess erweitert

Tests für Datums-Parsing ergänzt
```

**Merkmale:**
- Kurz und prägnant (erste Zeile unter 50 Zeichen)
- Beschreibt **was** geändert wurde
- Imperativ ("füge hinzu", nicht "hinzugefügt")
- Gibt Kontext (z.B. "für Umleitungsdaten")

### ❌ Schlechte Commit-Messages

```
Update
WIP
Änderungen
fix
asdf
Endlich fertig!!!!
noch mehr Zeug
```

**Probleme:**
- Zu vage
- Keine Information über den Inhalt
- Nicht professionell
- Hilft in 3 Monaten nicht beim Verständnis

### Ausführliche Commit-Messages

Für komplexere Commits können Sie eine längere Beschreibung hinzufügen:

```bash
git commit
```

Im Editor:

```
CSV-Import mit Fehlerbehandlung implementiert

- Unterstützung für verschiedene Trennzeichen (Komma, Semikolon, Tab)
- Fehlerbehandlung für nicht existierende Dateien
- Automatische Erkennung von Encoding (UTF-8, Latin-1)
- Rückgabe als Liste von Dictionaries für einfache Weiterverarbeitung

Closes #42
```

**Format:**
1. Erste Zeile: Kurze Zusammenfassung (max. 50 Zeichen)
2. Leerzeile
3. Ausführliche Beschreibung (optional)
4. Verweis auf Issues (optional)

## Sicherheit: Was gehört NICHT in Git?

### 🚨 Niemals committen:

#### 1. Passwörter und API-Keys

```python
# ❌ NIEMALS:
PASSWORD = "geheim123"
API_KEY = "sk_live_12345abcdef"
DATABASE_URL = "postgresql://user:password@server/db"
```

**Lösung**: Umgebungsvariablen oder Konfigurationsdateien verwenden:

```python
# ✅ Stattdessen:
import os
PASSWORD = os.getenv("MY_PASSWORD")
API_KEY = os.getenv("API_KEY")
```

Und in `.gitignore`:
```gitignore
.env
secrets.json
config.ini
```

#### 2. Private Schlüssel

```gitignore
# In .gitignore:
*.pem
*.key
id_rsa
*.p12
```

#### 3. Persönliche Daten

- E-Mail-Listen
- Nutzerdaten aus Datenbanken
- Personenbezogene Testdaten

#### 4. Große Dateien

Git ist für Code optimiert, nicht für:
- Große CSV-Dateien (> 10 MB)
- Videos, Bilder in hoher Auflösung
- Binärdateien, kompilierte Programme
- Datenbank-Dumps

**Faustregel**: Dateien über 5-10 MB gehören nicht in Git.

#### 5. Generierte Dateien

```gitignore
# Automatisch generierte Dateien:
__pycache__/
*.pyc
*.pyo
.ipynb_checkpoints/
_build/
dist/
*.egg-info/
```

## Die .gitignore richtig einsetzen

### Standard .gitignore für Python-Projekte

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual Environment
.venv/
venv/
ENV/
env/

# Jupyter
.ipynb_checkpoints/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Tests
.pytest_cache/
.coverage
htmlcov/

# Eigene sensible Dateien
.env
secrets.json
config_local.ini
```

### .gitignore testen

Prüfen Sie, ob eine Datei ignoriert wird:

```bash
git check-ignore -v dateiname.txt
```

### Bereits committete Dateien entfernen

Falls Sie versehentlich eine Datei committed haben:

```bash
# Aus Git entfernen, aber lokal behalten
git rm --cached dateiname.txt

# Zur .gitignore hinzufügen
echo "dateiname.txt" >> .gitignore

# Committen
git add .gitignore
git commit -m "Sensible Datei aus Git entfernt"
```

:::::{warning}
Achtung: Die Datei ist zwar aus dem neuesten Commit entfernt, aber noch in der Historie vorhanden! Für wirklich sensible Daten (Passwörter) müssen Sie die gesamte Historie bereinigen – das ist komplex und fehleranfällig.

**Besser**: Von Anfang an keine sensiblen Daten committen!
:::::

## Repository-Organisation

### Gute Dateistruktur

```
mein-projekt/
├── README.md              # Projektbeschreibung
├── requirements.txt       # Python-Abhängigkeiten
├── .gitignore            # Ignorierte Dateien
├── src/                  # Quellcode
│   ├── main.py
│   └── utils.py
├── tests/                # Tests
│   └── test_main.py
├── docs/                 # Dokumentation
│   └── anleitung.md
└── data/                 # Beispieldaten (klein!)
    └── beispiel.csv
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

## Zusammenarbeit: Kommunikation ist wichtig

### Wenn mehrere Personen am Projekt arbeiten:

1. **Regelmäßig pullen**: Vor Arbeitsbeginn `git pull` ausführen
2. **Regelmäßig pushen**: Fertige Commits zeitnah hochladen
3. **Aussagekräftige Messages**: Kolleg\*innen verstehen, was Sie getan haben
4. **Kleine Commits**: Einfacher zu reviewen
5. **Branches nutzen**: Feature-Branches für größere Änderungen

### Kommunikations-Checkliste

- [ ] Morgens: `git pull` ausführen
- [ ] Features in separaten Branches entwickeln
- [ ] Commits mit klaren Messages versehen
- [ ] Vor Feierabend: Änderungen pushen
- [ ] Bei Problemen: Mit Team kommunizieren

## Häufige Fehler und Lösungen

### Problem 1: "I forgot to commit"

Sie haben den ganzen Tag gearbeitet und wollen jetzt alles auf einmal committen.

**Lösung**: Verwenden Sie `git add -p` (interactive staging):

```bash
git add -p
```

Git zeigt Ihnen jede Änderung einzeln und fragt, ob sie hinzugefügt werden soll. So können Sie selektiv committen.

### Problem 2: "Wrong commit message"

Sie haben eine fehlerhafte Commit-Message geschrieben.

**Lösung (nur letzter Commit, noch nicht gepusht):**

```bash
git commit --amend -m "Korrigierte Commit-Message"
```

:::::{warning}
**Niemals** Commits ändern, die bereits gepusht wurden! Das führt zu Problemen bei anderen Entwickler\*innen.
:::::

### Problem 3: "I committed to the wrong branch"

**Lösung:**

```bash
# Aktuellen Commit merken
git log  # Hash kopieren, z.B. a1b2c3d

# Zum richtigen Branch wechseln
git checkout richtiger-branch

# Commit hierher kopieren
git cherry-pick a1b2c3d

# Zurück zum falschen Branch
git checkout falscher-branch

# Letzten Commit rückgängig machen
git reset --hard HEAD~1
```

### Problem 4: "I want to undo everything"

Sie haben experimentiert und möchten alle Änderungen verwerfen.

**Lösung:**

```bash
# Alle nicht-committeten Änderungen verwerfen
git restore .

# Auch aus Staging Area entfernen
git restore --staged .
```

## Cheat Sheet: Die wichtigsten Befehle

### Tägliche Arbeit

```bash
git status              # Status prüfen
git add datei.py        # Datei hinzufügen
git commit -m "Text"    # Committen
git push                # Hochladen
git pull                # Herunterladen
```

### Historie

```bash
git log --oneline       # Commits anzeigen
git diff                # Änderungen anzeigen
```

### Branches

```bash
git branch              # Branches anzeigen
git checkout -b name    # Branch erstellen + wechseln
git merge name          # Branch mergen
```

### Troubleshooting

```bash
git restore datei.py    # Änderungen verwerfen
git restore --staged .  # Aus Staging entfernen
git status              # Orientierung finden
```

## Weiterführende Ressourcen

### Online-Tutorials

- [Pro Git Buch (kostenlos)](https://git-scm.com/book/de/v2): Umfassendes Handbuch
- [GitHub Learning Lab](https://github.com/apps/github-learning-lab): Interaktive Tutorials
- [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials): Gut strukturiert

### Visualisierungen

- [Visualizing Git](https://git-school.github.io/visualizing-git/): Interaktive Visualisierung
- [Learn Git Branching](https://learngitbranching.js.org/?locale=de_DE): Spielerisches Lernen

### Git-GUIs

Falls Sie lieber grafisch arbeiten:
- [GitKraken](https://www.gitkraken.com/): Umfangreich, kostenlos für öffentliche Repos
- [SourceTree](https://www.sourcetreeapp.com/): Kostenlos
- VS Code: Eingebaute Git-Integration

## Zusammenfassung

### Commit-Best-Practices

- ✅ Häufig committen (nach jeder logischen Einheit)
- ✅ Aussagekräftige Messages schreiben
- ✅ Kleine, fokussierte Commits
- ❌ Keine riesigen "Alles-auf-einmal"-Commits

### Sicherheit

- ✅ `.gitignore` von Anfang an einrichten
- ✅ Keine Passwörter, Keys, sensiblen Daten committen
- ✅ Große Dateien vermeiden
- ❌ Nie sensible Daten in öffentliche Repos pushen

### Zusammenarbeit

- ✅ Regelmäßig pullen und pushen
- ✅ Feature-Branches nutzen
- ✅ Kommunikation im Team
- ❌ Nicht direkt auf `main` arbeiten bei Team-Projekten

:::::{admonition} Ihr Weg zu Git-Kompetenz
:class: success
Git-Expertise entsteht durch Übung. Die wichtigsten Tipps:

1. **Keine Angst vor Fehlern**: Solange Sie committen, können Sie (fast) nichts kaputt machen
2. **git status ist Ihr Freund**: Bei Unsicherheit immer zuerst Status prüfen
3. **Klein anfangen**: Nutzen Sie zunächst nur die Basics, erweitern Sie schrittweise
4. **Dokumentieren Sie**: Schreiben Sie auf, was funktioniert hat

Mit der Zeit werden Git-Befehle zur Routine – wie das Speichern einer Datei!
:::::

Im letzten Kapitel des Git-Exkurses finden Sie eine zusammenfassende Übungsaufgabe.
