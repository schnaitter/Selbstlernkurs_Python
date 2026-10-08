---
short_title: Abschlussübung
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
Projekt mit {term}`Git` und dokumentieren Sie Ihre Schritte mit mindestens **5
sinnvollen Commits**.

## Anforderungen

Das fertige Projekt soll:

1. {term}`CSV`-Dateien mit Bibliotheksdaten einlesen
1. Grundlegende Statistiken berechnen (z.B. Gesamtanzahl, Durchschnitt)
1. Fehlerbehandlung für ungültige Dateien enthalten
1. Eine README-Datei haben
1. Eine sinnvolle `.gitignore` haben
1. Optional: auf GitHub/GitLab veröffentlicht werden

## Schritt-für-Schritt-Anleitung

### Schritt 1: Projektstruktur aufsetzen

```bash
mkdir bibliotheks-statistik
cd bibliotheks-statistik
git init
git status
```

**✅ Checkpoint**: Sie haben ein leeres {term}`Git`-{term}`Repository` erstellt.

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
git add README.md
git commit -m "Initial commit: README erstellt"
```

### Schritt 3: .gitignore erstellen (2. Commit)

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

```bash
git add .gitignore
git commit -m "Gitignore für Python-Projekt hinzugefügt"
```

### Schritt 4: Grundgerüst erstellen (3. Commit)

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


if __name__ == "__main__":
    main()
```

```bash
git add statistik.py
git commit -m "Grundgerüst mit Funktionsdefinitionen erstellt"
```

### Schritt 5: CSV-Einlesefunktion implementieren (4. Commit)

```python
def lies_csv(dateiname):
    """Liest eine CSV-Datei ein und gibt die Zeilen zurück."""
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            reader = csv.DictReader(datei)
            return list(reader)
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
        sys.exit(1)
    except Exception as e:
        print(f"Fehler beim Einlesen: {e}")
        sys.exit(1)
```

```bash
git add statistik.py
git commit -m "CSV-Einlesefunktion mit Fehlerbehandlung implementiert"
```

### Schritt 6: Testdaten erstellen und ignorieren

Erstellen Sie eine Beispiel-CSV-Datei `beispiel.csv`:

```csv
Datum,Ausleihen,Rueckgaben
2025-10-01,45,38
2025-10-02,52,41
2025-10-03,48,50
2025-10-04,61,55
2025-10-05,39,42
```

**Achtung**: Diese Datei **nicht** committen – ergänzen Sie sie in der
`.gitignore`:

```gitignore
# Testdaten
beispiel.csv
```

```bash
git add .gitignore
git commit -m "Testdaten in gitignore aufgenommen"
```

**✅ Checkpoint**: Sie haben gelernt, Dateien zu ignorieren!

### Schritt 7: Statistik-Funktion implementieren (5. Commit)

```python
def berechne_statistik(daten):
    """Berechnet Statistiken aus den eingelesenen Daten."""
    if not daten:
        print("Keine Daten vorhanden.")
        return

    gesamt_ausleihen = sum(int(row['Ausleihen']) for row in daten)
    gesamt_rueckgaben = sum(int(row['Rueckgaben']) for row in daten)
    durchschnitt = gesamt_ausleihen / len(daten)

    print("\n=== Statistik ===")
    print(f"Anzahl Datensätze: {len(daten)}")
    print(f"Gesamt-Ausleihen: {gesamt_ausleihen}")
    print(f"Gesamt-Rückgaben: {gesamt_rueckgaben}")
    print(f"Durchschnitt Ausleihen/Tag: {durchschnitt:.2f}")
```

Und rufen Sie die Funktion in `main()` auf:

```python
    daten = lies_csv(dateiname)
    berechne_statistik(daten)
```

```bash
git add statistik.py
git commit -m "Statistik-Berechnung implementiert"
```

### Schritt 8: Testen

```bash
python statistik.py beispiel.csv
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

### Schritt 9: Historie überprüfen

```bash
git log --oneline
git log --oneline --graph --all
```

**✅ Checkpoint**: Sie haben mindestens 5 sinnvolle Commits erstellt!

## Bewertungskriterien

- [ ] Git-Repository initialisiert (`git init`)
- [ ] Mindestens 5 sinnvolle Commits mit aussagekräftigen Messages
- [ ] `.gitignore` vorhanden und sinnvoll konfiguriert
- [ ] README.md mit Projektbeschreibung vorhanden
- [ ] Python-Skript funktioniert und liest CSV ein
- [ ] Fehlerbehandlung implementiert
- [ ] Testdaten **nicht** committed
- [ ] Historie mit `git log` überprüft

**Bonuspunkte**: Feature-{term}`Branch` verwendet, auf GitHub veröffentlicht,
erweiterte Funktionen implementiert, verschiedene Ansätze reflektiert.

## Musterlösung (Commit-Historie)

Ihre Commit-Historie sollte in etwa so aussehen:

```
* e7f8g9h (HEAD -> main) Statistik-Berechnung implementiert
* c5d6e7f Testdaten in gitignore aufgenommen
* b4c5d6e CSV-Einlesefunktion mit Fehlerbehandlung implementiert
* a3b4c5d Grundgerüst mit Funktionsdefinitionen erstellt
* 92a3b4c Gitignore für Python-Projekt hinzugefügt
* 81829a3 Initial commit: README erstellt
```

## Kleine Aufgabe (für den Kurs)

Diese Übung kann als **Kleine Aufgabe** für den Selbstlernkurs Python
eingereicht werden, wenn Sie noch zwei weitere Änderungen mit zugehörigen
Commits einfügen. Dokumentieren Sie:

1. Ihre Commit-Historie (`git log --oneline`)
1. Screenshots des funktionierenden Programms
1. Den Link zu Ihrem GitHub-Repository (falls veröffentlicht)
1. Eine kurze Reflexion (3–5 Sätze): Was haben Sie gelernt? Was war
   herausfordernd?

**Abgabeformat**: PDF mit Dokumentation oder Link zum GitHub-Repository

:::::{admonition} Glückwunsch!
:class: success

Sie haben den Git-Exkurs erfolgreich abgeschlossen! Sie können jetzt lokale
Repositories erstellen und verwalten, Commits mit aussagekräftigen Messages
erstellen und durch die Historie navigieren. Für Remote-Repositories, Branches
und Merge-Konflikte steht Ihnen das optionale Vertiefungsmodul [Exkurs: Git –
Vertiefung](../095-Exkurs_Git_Vertiefung/000-Einleitung.md) zur Verfügung.
:::::

---

**Viel Erfolg und viel Spaß mit Git!** 🎉
