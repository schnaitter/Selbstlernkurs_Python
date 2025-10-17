# Vorschläge zur Kursverbesserung – GitHub Issues

## Überblick

Dieses Dokument konsolidiert Verbesserungsvorschläge aus Kurs-Reviews und
Curriculums-Planungsdokumenten. Jeder Abschnitt kann als Grundlage für ein
GitHub Issue dienen.

---

## 1. Exkurs: Unix – Detaillierte Ausgestaltung

**Kategorie**: Content Development <br>
**Priorität**: Mittel <br>
**Betroffenes Modul**: `030-Exkurs_Unix`<br>

### Beschreibung

Entwicklung eines umfassenden Unix/Linux-Exkurses mit strukturierten
Unterkapiteln, die praktische Relevanz für Python-Entwicklung haben.

### Vorgeschlagene Unterkapitel

- **010-Was_ist_Unix.md**: Geschichte, Unix-Philosophie, Relevanz für Python
- **020-Terminal_und_Shell.md**: Terminal vs. Shell, Shells (bash, zsh), Öffnen
  auf verschiedenen OS
- **030-Dateisystem_Navigation.md**: Verzeichnisstruktur, `pwd`, `ls`, `cd`,
  absolute vs. relative Pfade
- **040-Dateiverwaltung.md**: `mkdir`, `touch`, `cp`, `mv`, `rm`, `rmdir`,
  `cat`, `less`, `head`, `tail`
- **050-Berechtigungen.md**: Lese-, Schreib-, Ausführungsrechte, `chmod` für
  Python-Skripte, Shebang-Zeilen
- **060-Nuetzliche_Befehle.md** _(optional)_: Pipes, Umleitung, `grep`,
  Wildcards, Tab-Completion
- **070-Uebungen.md**: Praxisnahe Szenarien (z.B. Ordnerstruktur für Projekte)

### Implementierungsrichtlinien

- Fokus auf praktische Relevanz für Python-Entwicklung
- Unterkapitel kompakt halten (müssen nicht lang sein)
- Kurzer Hinweis auf Windows-Alternativen (Git Bash, WSL) - Hauptfokus:
  JupyterHub
- Viele Praxisbeispiele mit Bezug zu Kursinhalten
- Lernziel-Boxen am Anfang jedes Kapitels
- Übungsaufgaben mit Musterlösungen
- **Wichtig**: Exkurs ist optional, aber einzelne Inhalte werden in
  Folgekapi­teln vorausgesetzt → Cross-References zu spezifischen
  Unix-Abschnitten einbauen

### Deliverables

- [ ] Vollständige Struktur mit mindestens 5 Hauptkapiteln
- [ ] Jedem Kapitel ein Learning-Outcome zugeordnet
- [ ] Mindestens 2-3 Übungsaufgaben pro Kapitel

---

## 2. Exkurs: Git – Detaillierte Ausgestaltung

**Kategorie**: Content Development <br>
**Priorität**: Mittel <br>
**Betroffenes Modul**: `050-Exkurs_Git`<br>

### Beschreibung

Entwicklung eines praxisorientierten Git-Exkurses mit progressiver Komplexität
(lokal → remote) und bewusster Vereinfachung für Anfänger.

### Vorgeschlagene Unterkapitel

- **010-Was_ist_Versionskontrolle.md**: Problem
  ("finalversion_v3_wirklich_final.py"), Lösung, Git vs. GitHub/GitLab
- **020-Installation_Konfiguration.md**: Installation überprüfen,
  Grundkonfiguration, Verweis auf Installationskapitel
- **030-Grundkonzepte.md**: Repository, Working Directory, Staging Area, Commit
  (mit Visualisierung)
- **040-Erste_Schritte.md**: `git init`, `git status`, `git add`, `git commit`,
  gute Commit-Messages
- **050-Historie.md**: `git log`, `git diff`, Zu früheren Versionen
  zurückkehren
- **060-Remote_Repositories.md**: `git clone`, `git pull`, `git push`,
  GitHub/GitLab als Hosting-Plattformen
- **070-Branches.md**: Konzept, `git branch`, `git checkout`, wann Branches
  sinnvoll sind _(Merging nur konzeptionell!)_
- **080-Git_im_Kurs.md**: Eigene Lösungen versionieren, `.gitignore` für
  Python-Projekte, Kurs-Updates mit `git pull`
- **090-Best_Practices.md**: Commit-Frequenz, Sicherheit (Passwörter, große
  Dateien), Ressourcen
- **100-Uebung.md**: Kleines Python-Projekt mit mindestens 5 sinnvollen Commits

### Implementierungsrichtlinien

- Schrittweise Progression von lokal zu remote
- Fokus auf Einzelarbeit (eine Person, ein Computer)
- **Komplexe Themen bewusst vereinfacht**:
    - Merge-Konflikte, Rebase: **nicht praktisch behandeln**
    - Kurzer konzeptioneller Hinweis: Bei mehreren Computern/Nutzer\*innen
      können Konflikte entstehen
- Verweis auf bestehende Git-Nutzung im Kurs (Repository-Clone)
- Visualisierungen und Diagramme (z.B. Git-Workflow)
- Klare Kennzeichnung als optional (aber: spätere Übungen setzen Git voraus)

### Deliverables

- [ ] Mindestens 8 Unterkapitel mit strukturiertem Aufbau
- [ ] Visualisierungen für Git-Konzepte (Working Directory, Staging Area,
      Commits)
- [ ] Praktische Übungsaufgaben mit Musterlösungen
- [ ] Checkliste für sichere Git-Nutzung

---

## 3. Curriculum-Neustrukturierung

**Kategorie**: Course Design <br>
**Priorität**: Hoch <br>
**Betroffene Module**: Alle<br>

### Beschreibung

Umordnung der Kursmodule für bessere Progression und logischere Gruppierung
verwandter Inhalte.

### Vorgeschlagene neue Reihenfolge

```
000 Einleitung
010 Installation & Technik
020 Projekt: Taschenrechner I (Grundlagen)
030 Exkurs: Unix (optional)
040 Projekt: CSV I (Bestseller)
050 Exkurs: Git (optional)
060 Projekt: Taschenrechner II (Interaktiv)
070 Projekt: CSV II [Inhalt spezifizieren]
080 Projekt: MARC-XML [Inhalt ergänzen]
090 Projekt: Excel [Inhalt ergänzen]
900 Cheatsheet & Referenzen
999 Epilog
```

### Rationale

- **Logische Progression**: Grundlagen (Taschenrechner I) → Unix/Dateisystem →
  Datenverarbeitung (CSV I) → Versionskontrolle (Git)
- **Git vor komplexeren Projekten**: Ab Taschenrechner II können Lernende ihre
  Arbeit versionieren
- **Taschenrechner II nach CSV I**: Baut auf erweiterten Konzepten auf,
  profitiert von Git-Kenntnissen
- **Progressive Datenkomplexität**: CSV I → CSV II → MARC-XML → Excel

### Implementierungsschritte

- [ ] Ordner umbenennen:
    - `045-Projekt_Taschenrechner_II` → `060-Projekt_Taschenrechner_II`
    - `060-Projekt_CSV_II` → `070-Projekt_CSV_II`
    - `070-Projekt_MARC-XML` → `080-Projekt_MARC-XML`
    - `080-Projekt_Excel` → `090-Projekt_Excel`
- [ ] `toc.yml` mit neuer Reihenfolge aktualisieren
- [ ] Cross-References in allen Dokumenten überprüfen und aktualisieren
- [ ] Build-System testen (Jupyter Book)
- [ ] Git-History: Commit mit klarer Message für Nachvollziehbarkeit

---

## 4. Verbesserungen in Kursstruktur und Navigation

**Kategorie**: Course Design <br>
**Priorität**: Mittel <br>
**Betroffene Module**: Alle<br>

### Issue 4a: Explizite Vorwissen-Referenzen in Einleitungen

**Beschreibung**: Hinzufügen von expliziten Verweisen auf erforderliches
Vorwissen in Kapiteleinleitungen mittels `seealso`-Admonition.

**Beispiel**:

```markdown
:::{seealso}
Dieses Kapitel baut auf folgenden Konzepten auf:

- [Kapitel 020: Variablen und Datentypen](020-Projekt_Taschenrechner_I)
- [Kapitel 040: Listen und CSV-Verarbeitung](040-Projekt_CSV_I)
  :::
```

**Betroffene Module**: Mindestens 070-Projekt_CSV_II, 080-Projekt_MARC-XML,
090-Projekt_Excel

**Deliverables**:

- [ ] Alle Kapiteleinleitungen überprüft
- [ ] Mindestens 3 Kapitel erhalten explizite Vorwissen-Referenzen in
      `seealso`-Admonitions
- [ ] Hyperlinks zu relevanten vorherigen Kapiteln hinzugefügt

### Issue 4b: Cheatsheet-Platzierung und Referenzierung

**Beschreibung**: Das Cheatsheet (Kapitel 900) kommt zu spät. Für
Selbstlernende sollte es früher als Ressource referenziert werden.

**Vorgeschlagene Maßnahmen**:

- Erwähnung in Kurseinleitung (000) als ständig verfügbare Referenz-Ressource
- Hyperlinks zu relevanten Cheatsheet-Einträgen in frühen Kapiteln
- Optional: Kurzes "Quick Reference" am Ende jedes Hauptkapitels

**Technische Voraussetzung**: Cheatsheet benötigt ggf. Anker-Links für gezielte
Referenzierung (separate Prüfung nötig)

**Deliverables**:

- [ ] Kurseinleitung erwähnt Cheatsheet als Referenz
- [ ] Mindestens 3 Kapitel verlinken zu relevanten Cheatsheet-Abschnitten
- [ ] Anker-Struktur im Cheatsheet überprüft und ggf. ergänzt
- [ ] Navigierbarkeit des Cheatsheets getestet (Anker-Links funktionieren)

---

## 5. Inhalts-Vervollständigung

**Kategorie**: Content Development <br>
**Priorität**: Mittel<br>

### Issue 5a: CSV II – Inhalts-Spezifizierung

**Betroffenes Modul**: `070-Projekt_CSV_II`

**Beschreibung**: Das Modul "Projekt: CSV II" ist im aktuellen Kurs nicht
ausgearbeitet. Definieren Sie Inhalte und Lernziele.

**Fokus**: Analysen "von Hand" durchführen (ohne pandas)

**Vorgeschlagene Themen**:

- Fortgeschrittene CSV-Verarbeitung (Encoding-Probleme, komplexe Datentypen)
- Datenmigration oder -transformation
- Fehlerbehandlung bei großen Dateien
- Performance-Optimierung
- Manuelle Datenanalyse mit Python-Basismitteln (Listen, Dictionaries, etc.)

**Deliverables**:

- [ ] Lernziele definieren
- [ ] Unterkapitel-Struktur planen
- [ ] Mindestens 2 Übungen/Projekte

### Issue 5b: MARC-XML – Inhalts-Ergänzung

**Betroffenes Modul**: `080-Projekt_MARC-XML`

**Beschreibung**: Modul-Inhalte ausarbeiten mit Fokus auf Datentransformation.

**Fokus**: Datentransformation für Bibliothekssysteme

- JSON-Daten in MARC-XML überführen
- Import-Vorbereitung für Bibliothekssysteme
- XML-Verarbeitung in Python

**Deliverables**:

- [ ] Lernziele definieren
- [ ] Unterkapitel-Struktur planen
- [ ] Beispiel-Datensätze (JSON → MARC-XML)
- [ ] Mindestens 2 Übungen/Projekte

### Issue 5c: Excel – Inhalts-Ergänzung

**Betroffenes Modul**: `090-Projekt_Excel`

**Beschreibung**: Modul-Inhalte ausarbeiten mit Fokus auf moderne Datenanalyse.

**Fokus**: State-of-the-art Analyse mit pandas und Visualisierung

- Excel-Dateien in Python einlesen
- Datenanalyse mit pandas
- Visualisierung der Ergebnisse
- Optional: Visualisierung könnte eigenes Kapitel werden

**Deliverables**:

- [ ] Lernziele definieren
- [ ] Unterkapitel-Struktur planen
- [ ] Entscheidung: Visualisierung integriert oder separates Kapitel?
- [ ] Mindestens 2 Übungen/Projekte mit realen Library-Daten

---

## 6. Dokumentation und Referenzmaterialien

**Kategorie**: Documentation <br>
**Priorität**: Niedrig<br>

### Beschreibung

- Hilfreiche externe Ressourcen für jedes Kapitel verlinken
- Glossar mit Inhalt füllen und in-text Referenzen hinzufügen
- Best-Practice-Guides für häufige Fehler

**Externe Ressourcen (Priorität)**:

1. Offizielle Dokumentation (Python, Bibliotheken)
2. (E-)Bücher zu relevanten Themen
3. Bibliotheksspezifische OER-Materialien

**Wichtig**: Möglichst alle drei Kategorien pro Kapitel abdecken

### Deliverables

- [ ] Mindestens 3 externe Ressourcen pro Exkurs (alle drei Kategorien wenn
      möglich)
- [ ] Glossar mit 10+ neuen Einträgen füllen (insbesondere für Unix/Git)
- [ ] In-text Glossar-Referenzen in allen Kapiteln hinzufügen
- [ ] "Häufige Fehler & Lösungen" Dokument erstellen

---

## Kontinuierliche Aufgaben (keine separaten Issues)

Diese Aufgaben sind keine einmaligen Issues, sondern sollten regelmäßig während
der Kursentwicklung durchgeführt werden:

### Build-System regelmäßig testen

**System**: Jupyter Book v2 (Beta) basierend auf MyST

**Wann prüfen**:

- Nach jeder größeren Änderung (z.B. Curriculum-Neustrukturierung)
- Nach Hinzufügen neuer Kapitel
- Bei gemeldeten Problemen

**Prüfpunkte**:

- [ ] `toc.yml` validiert und fehlerfrei
- [ ] Alle Cross-References funktionieren
- [ ] Build-Prozess läuft ohne Fehler durch
- [ ] Navigation zwischen Kapiteln funktioniert
- [ ] Alle Assets (Bilder, etc.) werden korrekt geladen

### Dependencies aktuell halten

**Wann prüfen**:

- Zu Beginn eines neuen Semesters
- Bei Sicherheitswarnungen
- Alle 3-6 Monate

**Prüfpunkte**:

- [ ] `requirements.txt` auf veraltete Pakete prüfen
- [ ] Kompatibilität zwischen Paketen sicherstellen
- [ ] Nach Updates: Alle Notebooks/Code-Beispiele testen
- [ ] Breaking Changes dokumentieren

---

## Prioritäts-Matrix

| Issue                              | Impact  | Effort  | Priorität   |
| ---------------------------------- | ------- | ------- | ----------- |
| Git Exkurs (#2)                    | Hoch    | Mittel  | **Hoch**    |
| Unix Exkurs (#1)                   | Mittel  | Mittel  | **Mittel**  |
| Curriculum-Neustrukturierung (#3)  | Hoch    | Hoch    | **Hoch**    |
| Vorwissen-Referenzen (#4a)         | Mittel  | Niedrig | **Mittel**  |
| Cheatsheet-Referenzierung (#4b)    | Mittel  | Niedrig | **Mittel**  |
| CSV II/MARC-XML/Excel Inhalte (#5) | Mittel  | Mittel  | **Mittel**  |
| Dokumentation (#6)                 | Niedrig | Mittel  | **Niedrig** |

**Hinweise**:

- Assessment-Redesign wurde in `FUTURE_IMPROVEMENTS.md` verschoben (zu
  umfangreich für aktuelle Planung)
- Build-Testing und Dependency-Updates sind kontinuierliche Aufgaben (siehe
  oben)

---

## Nächste Schritte

1. **Kurzzeitig** (nächste 2-4 Wochen):
    - Curriculum-Neustrukturierung (Issue #3) umsetzen
    - Git Exkurs (Issue #2) beginnen
    - Build-System nach Neustrukturierung testen (kontinuierliche Aufgabe)

2. **Mittelfristig** (4-8 Wochen):
    - Unix Exkurs (Issue #1) ausarbeiten
    - Vorwissen-Referenzen (Issue #4a) hinzufügen
    - Cheatsheet-Referenzierung (Issue #4b) implementieren
    - Inhalts-Lücken füllen (Issue #5)

3. **Langfristig** (nach 8+ Wochen):
    - Dokumentation erweitern (Issue #6)
    - Optional: Assessment-Redesign aus `FUTURE_IMPROVEMENTS.md` evaluieren

---

**Dokument erstellt**: 17.10.2025
**Quelle**: Konsolidiert aus Projekt-Reviews und Curriculums-Planungsdokumenten
