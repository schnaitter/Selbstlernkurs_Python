---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Abschlussübung: Git-Projekt von Anfang bis Ende

In dieser Übung wenden Sie alle gelernten Git-Konzepte an, indem Sie ein
kleines Python-Projekt von Grund auf mit Git verwalten.

## Aufgabenstellung

Erstellen Sie ein **Bibliotheks-Statistik-Tool**, das CSV-Dateien mit
Ausleihstatistiken einliest und analysiert. Versionieren Sie das gesamte
Projekt mit Git und dokumentieren Sie Ihre Schritte mit mindestens **5
sinnvollen Commits**.

## Anforderungen

Das fertige Projekt soll:

1. CSV-Dateien mit Bibliotheksdaten einlesen
2. Grundlegende Statistiken berechnen (z.B. Gesamtanzahl, Durchschnitt)
3. Fehlerbehandlung für ungültige Dateien enthalten
4. Eine README-Datei haben
5. Eine sinnvolle `.gitignore` haben
6. Optional: Auf GitHub/GitLab veröffentlicht werden

## Schritt-für-Schritt-Anleitung

### Schritt 1: Projektstruktur aufsetzen

Erstellen Sie die Basis-Projektstruktur:

```bash
# Projektordner erstellen
$ mkdir bibliotheks-statistik
$ cd bibliotheks-statistik

# Git initialisieren
$ git init

# Status prüfen
$ git status
```

### Schritt 2: README erstellen (1. Commit)

Erstellen Sie eine `README.md`:

````markdown
# Bibliotheks-Statistik-Tool

Ein einfaches Python-Tool zur Analyse von Bibliotheks-Ausleihstatistiken.

## Funktionen

- CSV-Dateien einlesen
- Grundlegende Statistiken berechnen
- Fehlerbehandlung

## Verwendung

\```bash
python statistik.py daten.csv
\```

## Autor\*in

[Ihr Name]
````

Committen Sie die README:

```bash
$ git add README.md
$ git commit -m "Initial commit: README erstellt"
```

### Schritt 3: .gitignore erstellen (2. Commit)

Erstellen Sie eine `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyc

# Virtual Environment
.venv/
venv/

# IDEs
.vscode/
.idea/

# OS
.DS_Store

# Testdaten (große Dateien)
testdaten_gross.csv
```

Committen Sie:

```bash
$ git add .gitignore
$ git commit -m "Gitignore für Python-Projekt hinzugefügt"
```

### Schritt 4: Grundgerüst erstellen (3. Commit)

Erstellen Sie `statistik.py`:

```python
#!/usr/bin/env python3
"""
Bibliotheks-Statistik-Tool
Liest CSV-Dateien mit Ausleihstatistiken ein und berechnet Kennzahlen.
"""

import csv
import sys


def lies_csv(dateiname):
    """Liest eine CSV-Datei ein und gibt die Zeilen zurück."""
    pass  # TODO: Implementierung


def berechne_statistik(daten):
    """Berechnet Statistiken aus den eingelesenen Daten."""
    pass  # TODO: Implementierung


def main():
    """Hauptprogramm."""
    if len(sys.argv) < 2:
        print("Verwendung: python statistik.py <dateiname.csv>")
        sys.exit(1)

    dateiname = sys.argv[1]
    print(f"Lese Datei: {dateiname}")
    # TODO: Daten einlesen und analysieren


if __name__ == "__main__":
    main()
```

Committen Sie:

```bash
$ git add statistik.py
$ git commit -m "Grundgerüst mit Funktionsdefinitionen erstellt"
```

### Schritt 5: CSV-Einlesefunktion implementieren (4. Commit)

Erweitern Sie die `lies_csv`-Funktion:

```python
def lies_csv(dateiname):
    """Liest eine CSV-Datei ein und gibt die Zeilen zurück."""
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            reader = csv.DictReader(datei)
            daten = list(reader)
            return daten
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
        sys.exit(1)
    except Exception as e:
        print(f"Fehler beim Einlesen: {e}")
        sys.exit(1)
```

Committen Sie:

```bash
$ git add statistik.py
$ git commit -m "CSV-Einlesefunktion mit Fehlerbehandlung implementiert"
```

### Schritt 6: Testdaten erstellen

Erstellen Sie eine Beispiel-CSV-Datei `beispiel.csv`:

```csv
Datum,Ausleihen,Rueckgaben
2025-10-01,45,38
2025-10-02,52,41
2025-10-03,48,50
2025-10-04,61,55
2025-10-05,39,42
```

**Achtung**: Diese Datei **nicht** committen – verwenden Sie `.gitignore`!

Fügen Sie zur `.gitignore` hinzu:

```gitignore
# Testdaten
beispiel.csv
```

Committen Sie **nur** die `.gitignore`:

```bash
$ git add .gitignore
$ git commit -m "Testdaten in gitignore aufgenommen"
```

### Schritt 7: Statistik-Funktion implementieren (5. Commit)

Erweitern Sie die `berechne_statistik`-Funktion:

```python
def berechne_statistik(daten):
    """Berechnet Statistiken aus den eingelesenen Daten."""
    if not daten:
        print("Keine Daten vorhanden.")
        return

    gesamt_ausleihen = sum(int(row['Ausleihen']) for row in daten)
    gesamt_rueckgaben = sum(int(row['Rueckgaben']) for row in daten)
    durchschnitt_ausleihen = gesamt_ausleihen / len(daten)

    print("\n=== Statistik ===")
    print(f"Anzahl Datensätze: {len(daten)}")
    print(f"Gesamt-Ausleihen: {gesamt_ausleihen}")
    print(f"Gesamt-Rückgaben: {gesamt_rueckgaben}")
    print(f"Durchschnitt Ausleihen/Tag: {durchschnitt_ausleihen:.2f}")
```

Und aktualisieren Sie `main()`:

```python
def main():
    """Hauptprogramm."""
    if len(sys.argv) < 2:
        print("Verwendung: python statistik.py <dateiname.csv>")
        sys.exit(1)

    dateiname = sys.argv[1]
    print(f"Lese Datei: {dateiname}")

    daten = lies_csv(dateiname)
    berechne_statistik(daten)
```

Committen Sie:

```bash
$ git add statistik.py
$ git commit -m "Statistik-Berechnung implementiert"
```

### Schritt 8: Testen

Testen Sie Ihr Programm:

```bash
$ python statistik.py beispiel.csv
```

**Erwartete Ausgabe:**

```
Lese Datei: beispiel.csv

=== Statistik ===
Anzahl Datensätze: 5
Gesamt-Ausleihen: 245
Gesamt-Rückgaben: 226
Durchschnitt Ausleihen/Tag: 49.00
```

### Schritt 9: README aktualisieren (6. Commit)

Erweitern Sie die README mit einem Beispiel:

````markdown
# Bibliotheks-Statistik-Tool

Ein einfaches Python-Tool zur Analyse von Bibliotheks-Ausleihstatistiken.

## Funktionen

- CSV-Dateien mit Ausleihstatistiken einlesen
- Berechnung von Gesamt-Ausleihen und -Rückgaben
- Durchschnittliche Ausleihen pro Tag
- Fehlerbehandlung für fehlende oder ungültige Dateien

## Verwendung

\```bash
python statistik.py beispiel.csv
\```

## CSV-Format

Die CSV-Datei sollte folgendes Format haben:

\```csv
Datum,Ausleihen,Rueckgaben
2025-10-01,45,38
2025-10-02,52,41
\```

## Autor\*in

[Ihr Name] - Selbstlernkurs Python, HU Berlin
````

Committen Sie:

```bash
$ git add README.md
$ git commit -m "README mit Verwendungsbeispiel aktualisiert"
```

### Schritt 10: Historie überprüfen

Schauen Sie sich Ihre Arbeit an:

```bash
# Alle Commits anzeigen
$ git log --oneline

# Mit Graph
$ git log --oneline --graph --all

# Detaillierte Ansicht
$ git log
```

## Optionale Erweiterungen

### Option A: Feature-Branch für Erweiterung

Erstellen Sie einen Branch für eine neue Funktion:

```bash
# Branch erstellen
$ git checkout -b feature-visualisierung

# Neue Funktion hinzufügen (z.B. Balkendiagramm mit ASCII-Art)
# ... Code schreiben ...

# Committen
$ git add statistik.py
$ git commit -m "ASCII-Visualisierung hinzugefügt"

# Zurück zu main und mergen
$ git checkout main
$ git merge feature-visualisierung

# Branch löschen
$ git branch -d feature-visualisierung
```

### Option B: Auf GitHub veröffentlichen

1. Erstellen Sie ein Repository auf GitHub
2. Verbinden Sie Ihr lokales Repository:

```bash
$ git remote add origin https://github.com/ihr-username/bibliotheks-statistik.git
$ git branch -M main
$ git push -u origin main
```

3. Überprüfen Sie auf GitHub, dass alle Commits sichtbar sind

### Option C: Zusammenarbeit simulieren

Erstellen Sie eine zweite Änderung:

```bash
# Simulieren Sie einen anderen Computer
$ cd ..
$ git clone bibliotheks-statistik bibliotheks-statistik-klon
$ cd bibliotheks-statistik-klon

# Änderung machen
$ echo "# Todo: Tests schreiben" >> README.md
$ git add README.md
$ git commit -m "Todo-Liste zur README hinzugefügt"

# Zurück zum Original
$ cd ../bibliotheks-statistik

# Updates holen
$ git pull ../bibliotheks-statistik-klon main
```

## Bewertungskriterien

Überprüfen Sie selbst, ob Sie alle Anforderungen erfüllt haben:

- [ ] Git-Repository initialisiert (`git init`)
- [ ] Mindestens 5 sinnvolle Commits erstellt
- [ ] Jeder Commit hat eine aussagekräftige Message
- [ ] `.gitignore` vorhanden und sinnvoll konfiguriert
- [ ] README.md mit Projektbeschreibung vorhanden
- [ ] Python-Skript funktioniert und liest CSV ein
- [ ] Fehlerbehandlung implementiert
- [ ] Testdaten **nicht** committed (in `.gitignore`)
- [ ] Historie mit `git log` überprüft

### Bonuspunkte

- [ ] Mehr als 6 Commits mit logischer Aufteilung
- [ ] Feature-Branch verwendet
- [ ] Auf GitHub/GitLab veröffentlicht
- [ ] Erweiterte Funktionen implementiert (z.B. verschiedene Statistiken)

## Reflexion

Beantworten Sie für sich selbst:

1. **Commit-Frequenz**: Haben Sie oft genug committed? Waren die Commits zu
   groß oder zu klein?
2. **Commit-Messages**: Sind Ihre Messages aussagekräftig? Könnten Sie in 3
   Monaten nachvollziehen, was Sie getan haben?
3. **Git-Workflow**: Welche Git-Befehle haben Sie am häufigsten verwendet?
4. **Herausforderungen**: Was war schwierig? Was würden Sie beim nächsten Mal
   anders machen?
5. **Nutzen**: Wie hat Git Ihnen bei der Entwicklung geholfen?

## Musterlösung (Commit-Historie)

Ihre Commit-Historie sollte in etwa so aussehen:

```
* e7f8g9h (HEAD -> main) README mit Verwendungsbeispiel aktualisiert
* d6e7f8g Statistik-Berechnung implementiert
* c5d6e7f Testdaten in gitignore aufgenommen
* b4c5d6e CSV-Einlesefunktion mit Fehlerbehandlung implementiert
* a3b4c5d Grundgerüst mit Funktionsdefinitionen erstellt
* 92a3b4c Gitignore für Python-Projekt hinzugefügt
* 81829a3 Initial commit: README erstellt
```

## Zusammenfassung

In dieser Übung haben Sie:

✅ Ein Repository von Grund auf erstellt<br>
✅ Mehrere sinnvolle Commits mit guten Messages erstellt<br>
✅ `.gitignore` für Python-Projekte konfiguriert<br>
✅ Eine README für Ihr Projekt geschrieben<br>
✅ Den gesamten Git-Workflow durchlaufen<br>
✅ Optional: Branches verwendet oder auf GitHub veröffentlicht<br>

Sie haben den Git-Exkurs abgeschlossen und können nun:

- Lokale Repositories erstellen und verwalten
- Commits mit aussagekräftigen Messages erstellen
- Durch die Historie navigieren
- Mit Remote-Repositories (GitHub/GitLab) arbeiten
- Branches für parallele Entwicklung nutzen
- Best Practices für Sicherheit und Zusammenarbeit anwenden

**Nächste Schritte:**

- Wenden Sie Git bei allen Kurs-Projekten an
- Erstellen Sie ein Portfolio-Repository auf GitHub
- Experimentieren Sie mit Branches für verschiedene Lösungsansätze
- Teilen Sie Ihre Projekte mit Kommiliton\*innen

<!--
## Kleine Aufgabe (für den Kurs)

Diese Übung kann als **Kleine Aufgabe** für den Selbstlernkurs Python eingereicht werden. Dokumentieren Sie:

1. Ihre Commit-Historie (`git log --oneline`)
2. Screenshots des funktionierenden Programms
3. Den Link zu Ihrem GitHub-Repository (falls veröffentlicht)
4. Eine kurze Reflexion (3-5 Sätze): Was haben Sie gelernt? Was war herausfordernd?

**Abgabeformat**: PDF mit Dokumentation oder Link zum GitHub-Repository
-->
