---
numbering:
    heading_1: false
    heading_2: true
    title: false
---

# Git im Kurs nutzen

In diesem Kapitel lernen Sie, wie Sie Git konkret im Selbstlernkurs Python einsetzen können – sowohl um Kurs-Updates zu erhalten als auch um Ihre eigenen Lösungen zu versionieren.

## Das Kurs-Repository

Sie haben diesen Kurs wahrscheinlich bereits als Git-Repository geklont:

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

Wenn neue Kapitel hinzugefügt oder Fehler korrigiert werden, können Sie diese Updates herunterladen:

```bash
cd Selbstlernkurs_Python
git pull
```

**Was passiert?**
- Git lädt die neuesten Commits vom GitHub-Repository herunter
- Ihre lokale Kopie wird auf den neuesten Stand gebracht
- Neue Kapitel, korrigierte Übungen oder verbesserte Erklärungen stehen zur Verfügung

:::::{admonition} Regelmäßig updaten
:class: tip
Führen Sie vor Beginn einer neuen Lerneinheit ein `git pull` aus, um sicherzustellen, dass Sie die aktuellste Version des Kurses verwenden!
:::::

## Ihre eigenen Lösungen versionieren

### Szenario: Übungsaufgaben mit Git verwalten

Sie bearbeiten die Übungsaufgaben aus dem Kurs und möchten Ihre Fortschritte dokumentieren.

#### Option 1: Im Kurs-Repository arbeiten (einfach, aber eingeschränkt)

Sie können Ihre Lösungen direkt im Kurs-Ordner speichern:

```bash
cd Selbstlernkurs_Python

# Eigenen Lösungsordner erstellen
mkdir meine-loesungen
cd meine-loesungen

# Erste Aufgabe bearbeiten
echo "# Lösung Kapitel 2" > taschenrechner.py

# Committen
git add taschenrechner.py
git commit -m "Lösung: Taschenrechner-Grundfunktionen"
```

**Vorteil**: Alles an einem Ort, einfacher Einstieg

**Nachteil**:
- Sie können Ihre Commits nicht zu GitHub pushen (keine Schreibrechte)
- Bei `git pull` können Konflikte mit Kurs-Updates entstehen

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

# Optional: Auf GitHub pushen (siehe Kapitel Remote Repositories)
```

**Vorteil**:
- Vollständige Kontrolle über Ihr Repository
- Können zu GitHub/GitLab pushen
- Keine Konflikte mit Kurs-Updates
- Eigene Branch-Struktur möglich

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
.ipynb_checkpoints

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

:::::{margin}
**Hinweis**: Dateien, die bereits committed wurden, werden durch `.gitignore` nicht automatisch entfernt. Verwenden Sie `git rm --cached dateiname`, um sie aus Git zu entfernen (aber lokal zu behalten).
:::::

### Vorgefertigte .gitignore-Vorlagen

GitHub bietet Vorlagen für verschiedene Sprachen:
[https://github.com/github/gitignore](https://github.com/github/gitignore)

Für Python:
[https://github.com/github/gitignore/blob/main/Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)

## Praktischer Workflow: Eine Übungsaufgabe lösen

Ein typischer Workflow für eine Kurs-Übung:

```bash
# 1. Kurs-Updates holen
cd ~/Selbstlernkurs_Python
git pull

# 2. Neues Kapitel lesen, Aufgabe verstehen
# (z.B. Kapitel 040-Projekt_CSV_I)

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

# 7. Weiterarbeiten
# ... Code erweitern ...
git add csv_einlesen.py
git commit -m "CSV-Projekt: Fehlerbehandlung hinzugefügt"

# 8. Fertige Lösung
git add csv_einlesen.py
git commit -m "CSV-Projekt: Lösung abgeschlossen"

# 9. Optional: Zu GitHub pushen
git push
```

## Mit Musterlösungen vergleichen

Das Kurs-Repository enthält Musterlösungen im `solutions/`-Ordner.

```bash
cd ~/Selbstlernkurs_Python
ls solutions/
```

**Workflow:**

1. Versuchen Sie zunächst, die Aufgabe selbstständig zu lösen
2. Committen Sie Ihre eigene Lösung
3. Schauen Sie sich dann die Musterlösung an
4. Vergleichen Sie die Ansätze

**Unterschiede anzeigen:**

```bash
# Vergleichen Sie Ihre Lösung mit der Musterlösung
diff ~/Python-Kurs-Loesungen/020-Taschenrechner/taschenrechner.py \
     ~/Selbstlernkurs_Python/solutions/020/taschenrechner.py
```

## Branch-Strategie für Übungen

Für größere Projekte können Sie Branches verwenden:

```bash
# Hauptbranch: Fertige, funktionierende Lösungen
git checkout main

# Neuer Branch für Experiment
git checkout -b experiment-alternative-loesung

# Experimentieren
# ... Code schreiben ...
git add .
git commit -m "Alternative Implementierung ausprobiert"

# Falls erfolgreich: Mergen
git checkout main
git merge experiment-alternative-loesung

# Falls nicht erfolgreich: Branch einfach löschen
git checkout main
git branch -d experiment-alternative-loesung
```

## Zusammenarbeit mit Kommiliton\*innen

Falls Sie mit anderen Kursteilnehmer\*innen zusammenarbeiten möchten:

### 1. Gemeinsames Repository auf GitHub erstellen

Eine Person erstellt ein Repository und lädt die anderen als Collaborators ein.

### 2. Alle klonen das Repository

```bash
git clone https://github.com/username/kurs-loesungen-gemeinsam.git
cd kurs-loesungen-gemeinsam
```

### 3. Feature-Branches nutzen

Jede Person arbeitet in einem eigenen Branch:

```bash
# Person A
git checkout -b person-a/csv-aufgabe
# ... arbeiten ...
git push -u origin person-a/csv-aufgabe

# Person B
git checkout -b person-b/marc-aufgabe
# ... arbeiten ...
git push -u origin person-b/marc-aufgabe
```

### 4. Regelmäßig synchronisieren

```bash
git pull
```

:::::{admonition} Kommunikation ist wichtig
:class: tip
Wenn Sie gemeinsam arbeiten:
- Sprechen Sie ab, wer an welchen Dateien arbeitet
- Ziehen Sie regelmäßig Updates mit `git pull`
- Pushen Sie fertige Commits zeitnah
- Nutzen Sie aussagekräftige Commit-Messages
:::::

## Typische Fehler vermeiden

### ❌ Fehler 1: Sensible Daten committen

```bash
# NIEMALS tun:
git add passwort.txt
git add config_mit_api_key.ini
```

**Lösung**: `.gitignore` verwenden!

### ❌ Fehler 2: Riesige Dateien committen

```bash
# Vermeiden:
git add bibliotheksdaten_5GB.csv
```

Git ist für Code optimiert, nicht für große Binärdateien.

**Lösung**: Große Dateien in `.gitignore` eintragen oder externe Speicherlösungen nutzen.

### ❌ Fehler 3: Kurs-Repository modifizieren und dann nicht updaten können

Wenn Sie direkt im Kurs-Repository Änderungen vornehmen, kann `git pull` zu Konflikten führen.

**Lösung**: Arbeiten Sie in einem separaten Lösungs-Repository (siehe oben).

## Zusammenfassung

### Kurs-Repository aktualisieren

```bash
cd Selbstlernkurs_Python
git pull
```

### Eigene Lösungen versionieren

```bash
# Separates Repository erstellen (empfohlen)
mkdir Python-Kurs-Loesungen
cd Python-Kurs-Loesungen
git init

# .gitignore erstellen
echo "__pycache__/" > .gitignore
echo ".venv/" >> .gitignore
git add .gitignore
git commit -m "Gitignore hinzugefügt"

# Lösungen committen
git add loesung.py
git commit -m "Beschreibung der Lösung"
```

### Wichtige Dateien ausschließen

```gitignore
# .gitignore
__pycache__/
.venv/
.ipynb_checkpoints/
*.pyc
.DS_Store
```

:::::{admonition} Übung
:class: warning
Richten Sie Ihr eigenes Lösungs-Repository ein:

1. Erstellen Sie einen neuen Ordner für Ihre Kurs-Lösungen
2. Initialisieren Sie Git mit `git init`
3. Erstellen Sie eine `.gitignore` für Python-Projekte
4. Kopieren Sie eine Ihrer bisherigen Lösungen in dieses Repository
5. Erstellen Sie mindestens 3 sinnvolle Commits
6. Optional: Pushen Sie das Repository zu GitHub

Dokumentieren Sie Ihre Schritte!
:::::

Im nächsten Kapitel lernen Sie Best Practices und Sicherheitshinweise für die Arbeit mit Git.
