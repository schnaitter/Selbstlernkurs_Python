---
short_title: Git im Kurs
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Git im Kurs nutzen

In diesem Kapitel lernen Sie, wie Sie Git konkret im Selbstlernkurs Python
einsetzen – sowohl um Kurs-Updates zu erhalten als auch um Ihre eigenen
Lösungen zu versionieren. Außerdem erfahren Sie, welche Dateien **nicht** in
ein Repository gehören und wie Sie typische Fehler vermeiden.

## Das Kurs-Repository

Sie haben diesen Kurs wahrscheinlich bereits als {term}`Git`-{term}`Repository` geklont:

```bash
git clone https://github.com/schnaitter/Selbstlernkurs_Python.git
cd Selbstlernkurs_Python
```

Das Repository enthält:

- Alle Kapitel und Übungen
- Jupyter Notebooks für interaktive Beispiele
- Musterlösungen (im Ordner `solutions/`)
- Konfigurationsdateien für das Jupyter Book

## Kurs-Updates abrufen

Wenn neue Kapitel hinzugefügt oder Fehler korrigiert werden, können Sie diese
Updates herunterladen:

```bash
cd Selbstlernkurs_Python
git pull
```

**Was passiert?**

- Git lädt die neuesten Commits vom GitHub-Repository herunter
- Ihre lokale Kopie wird auf den neuesten Stand gebracht
- Neue Kapitel, korrigierte Übungen oder verbesserte Erklärungen stehen zur
  Verfügung

:::::{admonition} Regelmäßig updaten
:class: tip
Führen Sie vor Beginn einer neuen Lerneinheit ein `git pull` aus, um
sicherzustellen, dass Sie die aktuellste Version des Kurses verwenden!
:::::

## Ihre eigenen Lösungen versionieren

### Szenario: Übungsaufgaben mit Git verwalten

#### Option 1: Im Kurs-Repository arbeiten (einfach, aber eingeschränkt)

Sie können einen eigenen Unterordner `meine-loesungen/` anlegen und Ihre
Lösungen darin committen.

**Vorteil**: Alles an einem Ort, einfacher Einstieg.

**Nachteil**: Sie können nicht zu GitHub pushen (keine Schreibrechte), und bei
`git pull` können Konflikte mit Kurs-Updates entstehen.

#### Option 2: Eigenes Repository für Lösungen (empfohlen)

Erstellen Sie ein separates Repository für Ihre Lösungen:

```bash
# Neuen Ordner erstellen
mkdir ~/Python-Kurs-Loesungen
cd ~/Python-Kurs-Loesungen

# Git initialisieren
git init

# README erstellen
echo "# Meine Lösungen zum Selbstlernkurs Python" > README.md
git add README.md
git commit -m "Initial commit"
```

**Vorteil**: Vollständige Kontrolle, keine Konflikte mit Kurs-Updates, eigene
Branch-Struktur möglich.

**Empfohlene Ordnerstruktur:**

```
Python-Kurs-Loesungen/
├── 020-Taschenrechner/
│   ├── taschenrechner_v1.py
│   └── taschenrechner_v2.py
├── 040-CSV/
│   ├── csv_einlesen.py
│   └── testdaten.csv
├── 070-MARC-XML/
│   └── marc_parser.py
└── README.md
```

## .gitignore: Dateien von Git ausschließen

Nicht alle Dateien sollten versioniert werden. Typische Beispiele:

- **Temporäre Dateien**: `__pycache__/`, `.ipynb_checkpoints/`
- **Große Datenmengen**: `daten/bibliotheksdaten_10gb.csv`
- **Sensible Informationen**: Passwörter, API-Keys
- **Virtuelle Umgebungen**: `.venv/`, `venv/`
- **Build-Ausgaben**: `_build/`, `dist/`

### .gitignore erstellen

Erstellen Sie im Projektroot eine Datei namens `.gitignore`:

```bash
cd Python-Kurs-Loesungen
nano .gitignore
```

**Typischer Inhalt für Python-Projekte:**

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

# Jupyter Notebook
.ipynb_checkpoints/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Betriebssystem
.DS_Store
Thumbs.db

# Eigene Testdaten (falls gewünscht)
testdaten/grosse_datei.csv

# Sensible Daten
config.ini
secrets.json
.env
```

Committen Sie die `.gitignore`:

```bash
git add .gitignore
git commit -m "Gitignore für Python-Projekt hinzugefügt"
```

### .gitignore testen

Prüfen Sie, ob eine Datei ignoriert wird:

```bash
git check-ignore -v dateiname.txt
```

:::::{margin}
**Hinweis**: Dateien, die bereits committed wurden, werden durch `.gitignore`
nicht automatisch entfernt. Verwenden Sie `git rm --cached dateiname`, um sie
aus Git zu entfernen (aber lokal zu behalten).
:::::

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
Achtung: Die Datei ist zwar aus dem neuesten Commit entfernt, aber noch in der
Historie vorhanden! Für wirklich sensible Daten (Passwörter) müssten Sie die
gesamte Historie bereinigen – das ist komplex und fehleranfällig.

**Besser**: Von Anfang an keine sensiblen Daten committen!
:::::

### Vorgefertigte .gitignore-Vorlagen

GitHub bietet Vorlagen für verschiedene Sprachen:
[github.com/github/gitignore](https://github.com/github/gitignore)

Für Python:
[Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)

## Sicherheit: Was gehört NICHT in Git?

### 🚨 Niemals committen:

#### 1. Passwörter und API-Keys

```python
# ❌ NIEMALS:
PASSWORD = "geheim123"
API_KEY = "sk_live_12345abcdef"
```

**Lösung**: Umgebungsvariablen verwenden:

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
- Videos, hochauflösende Bilder
- Binärdateien, kompilierte Programme
- Datenbank-Dumps

**Faustregel**: Dateien über 5–10 MB gehören nicht in Git.

### Sicherheits-Checkliste

- [ ] `.gitignore` **vor** dem ersten Commit anlegen
- [ ] Keine Passwörter, API-Keys oder Tokens im Code
- [ ] Keine privaten Schlüssel (`*.pem`, `id_rsa`, …) committen
- [ ] Keine personenbezogenen oder vertraulichen Daten committen
- [ ] Große Dateien (> 5–10 MB) vermeiden oder extern speichern
- [ ] Vor jedem Commit kurz `git status` prüfen
- [ ] Bei versehentlichem Commit: `git rm --cached` und `.gitignore` ergänzen
- [ ] Bei echten Geheimnissen: Schlüssel/Passwort sofort ändern (die Historie
  lässt sich nur aufwendig bereinigen)

## Praktischer Workflow: Eine Übungsaufgabe lösen

```bash
# 1. Kurs-Updates holen
cd ~/Selbstlernkurs_Python
git pull

# 2. Neues Kapitel lesen, Aufgabe verstehen

# 3. In Ihr Lösungs-Repository wechseln
cd ~/Python-Kurs-Loesungen

# 4. Ordner für die Aufgabe erstellen
mkdir 040-CSV-Projekt
cd 040-CSV-Projekt

# 5. Lösungsdatei erstellen
nano csv_einlesen.py
# ... Code schreiben ...

# 6. Ersten Commit erstellen
git add csv_einlesen.py
git commit -m "CSV-Projekt: Grundgerüst erstellt"

# 7. Weiterarbeiten und weitere Commits erstellen
# 8. Optional: Zu GitHub pushen
git push
```

## Mit Musterlösungen vergleichen

Das Kurs-Repository enthält Musterlösungen im `solutions/`-Ordner.

**Workflow:**

1. Versuchen Sie zunächst, die Aufgabe selbstständig zu lösen
2. Committen Sie Ihre eigene Lösung
3. Schauen Sie sich dann die Musterlösung an
4. Vergleichen Sie die Ansätze

**Unterschiede anzeigen:**

```bash
diff ~/Python-Kurs-Loesungen/020-Taschenrechner/taschenrechner.py \
     ~/Selbstlernkurs_Python/solutions/020/taschenrechner.py
```

## Zusammenarbeit mit Kommiliton\*innen

Falls Sie mit anderen Kursteilnehmer\*innen zusammenarbeiten möchten:

1. **Gemeinsames Repository auf GitHub erstellen** und die anderen als
   Collaborators einladen
2. **Alle klonen das Repository**
3. **Feature-Branches nutzen**: Jede Person arbeitet in einem eigenen {term}`Branch`
4. **Regelmäßig synchronisieren**: `git pull` vor dem Arbeiten, `git push` nach
   fertigen Commits

:::::{admonition} Kommunikation ist wichtig
:class: tip
- Sprechen Sie ab, wer an welchen Dateien arbeitet
- Ziehen Sie regelmäßig Updates mit `git pull`
- Pushen Sie fertige Commits zeitnah
- Nutzen Sie aussagekräftige Commit-Messages
:::::

## Häufige Fehler und Lösungen

Alle typischen Anfängerfehler an einer Stelle gesammelt:

### Vergessen, `git add` zu verwenden

```bash
git commit -m "Änderungen"   # Datei war nie gestaged
```

**Lösung**: Immer erst `git add`, dann `git commit`. Vorher `git status`
prüfen.

### Commit ohne Message

`git commit` ohne `-m` öffnet einen Editor. Wird dieser ohne Eingabe
geschlossen, bricht der Commit ab.

**Lösung**: Message im Editor eingeben oder `-m "Message"` verwenden.

### Ungewollte Dateien committen

```bash
git add .
git commit -m "Alles"
```

Dabei werden auch temporäre Dateien, Caches oder vertrauliche Daten committed.

**Lösung**: Vorher `git status` prüfen, gezielt mit `git add` auswählen und
eine `.gitignore` verwenden.

### Falsche Commit-Message (letzter Commit, noch nicht gepusht)

```bash
git commit --amend -m "Korrigierte Commit-Message"
```

:::::{warning}
**Niemals** Commits ändern, die bereits gepusht wurden! Das führt zu Problemen
bei anderen Entwickler\*innen.
:::::

### Versehentlich im falschen Branch committed

```bash
# Commit-Hash merken
git log

# Zum richtigen Branch wechseln und Commit übernehmen
git checkout richtiger-branch
git cherry-pick a1b2c3d
```

### Alle Änderungen verwerfen

Mit `git restore .` verwerfen Sie alle nicht-committeten Änderungen, mit
`git restore --staged .` nehmen Sie sie zusätzlich aus der Staging Area.

### Kurs-Repository modifiziert und kann nicht mehr updaten

Wenn Sie direkt im Kurs-Repository Änderungen vornehmen, kann `git pull` zu
Konflikten führen.

**Lösung**: Arbeiten Sie in einem separaten Lösungs-Repository (siehe oben).

:::::{seealso} Weitere Hilfestellungen
Weitere Rückgängig-Techniken finden Sie im Vertiefungskapitel
[Änderungen rückgängig machen](../095-Exkurs_Git_Vertiefung/040-Rueckgaengig_machen.md).
:::::

## Zusammenfassung

```bash
# Kurs-Repository aktualisieren
cd Selbstlernkurs_Python
git pull

# Eigenes Lösungs-Repository anlegen (empfohlen)
mkdir Python-Kurs-Loesungen && cd Python-Kurs-Loesungen
git init
printf '__pycache__/\n.venv/\n.ipynb_checkpoints/\n*.pyc\n.DS_Store\n' > .gitignore
git add .gitignore
git commit -m "Gitignore hinzugefügt"
```

```{exercise} Übung: Lösungs-Repository einrichten
:label: git-loesungs-repository

Richten Sie Ihr eigenes Lösungs-Repository ein:

1. Erstellen Sie einen neuen Ordner für Ihre Kurs-Lösungen
2. Initialisieren Sie Git mit `git init`
3. Erstellen Sie eine `.gitignore` für Python-Projekte
4. Kopieren Sie eine Ihrer bisherigen Lösungen in dieses Repository
5. Erstellen Sie mindestens 3 sinnvolle Commits
6. Optional: Pushen Sie das Repository zu GitHub

Dokumentieren Sie Ihre Schritte!
```

Im nächsten Kapitel finden Sie eine zusammenfassende Übungsaufgabe zum
gesamten Git-Exkurs.
