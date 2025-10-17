# Zukünftige Verbesserungsvorschläge (Optional)

Dieses Dokument sammelt Verbesserungsideen, die aktuell zu umfangreich oder
nicht prioritär sind, aber langfristig interessant sein könnten.

---

## Assessment-Redesign: Three-Track Curriculum

**Kategorie**: Assessment & Pedagogy<br>
**Priorität**: Optional / Langfristig<br>
**Betroffene Module**: Gesamter Kurs<br>

### Beschreibung Entwicklung eines gestuften Curriculums mit drei

Track-Optionen und verbessertem Assessment durch Auto-Grading, Peer Review und
Portfolio-Entwicklung.

### Curriculum-Struktur

#### 30-Hour Track (Foundation)

- Grundlagen Python (4-5 Projekte)
- Fokus: Fundamentale Konzepte, syntaktisches Verständnis
- Assessment: Auto-graded quizzes + Peer code review (strukturiert)

**Projekte**:

1. Taschenrechner I & II (Grundlagen)
2. CSV I (Bestseller-Analyse)
3. Einfacher Datenanalyseprozess (optional)

#### 60-Hour Track (Extended)

- Foundation + OOP, Exception Handling, Web Scraping, Advanced Pandas
- Progressive Komplexität über 12-15 Wochen
- Größere Projekte mit praktischer Anwendung

**Projekte** (zusätzlich zu Foundation):

1. Web Scraper für Library Vendors (200-250 Zeilen, 8-10h)
2. OAI-PMH Harvester (300-400 Zeilen, 10-12h)
3. Circulation Analysis Suite (250-300 Zeilen, 8-10h)

#### 90-Hour Track (Capstone)

- Extended + Capstone-Projekt mit individuellem Problemlösungsansatz
- Proposal, Design, Development, Testing, Documentation, Presentation
- Real-world Anwendung für eigene Organisation

### Assessment-Komponenten

#### 1. Auto-Graded Quizzes

- **Was**: Faktenwissen + syntaktisches Verständnis
- **Wann**: Nach jedem Konzept-Block
- **Feedback**: Nicht nur "incorrect", sondern "Your answer suggests you're
  thinking about variable scope in local rather than global terms—review this
  explanation"

#### 2. Weekly Challenge Problems

- **Was**: Automatisiertes Testing gegen mehrere Test-Cases
- **Output**: Pass/Fail + spezifische Test-Cases
- **Beispiel**: "Your function works correctly for single-digit numbers but
  fails for multi-digit—check your string indexing"

#### 3. Peer Code Review (Structured)

- **Rubrik**: 4-5 konkrete ja/nein Fragen pro Projekt
    - Läuft der Code ohne Fehler?
    - Erfüllt er das Ziel?
    - Ist er angemessen organisiert?
    - Sind Variablennamen aussagekräftig?
- **Protokoll**:
    - Jeder Lernende postet Code + Erklärung
    - Review von 2 zugewiesenen Peers
    - Strukturiertes Feedback: 1 Stärke + 1 Verbesserungsvorschlag
- **Kalibrierung**: Beispiele mit Scoring in Orientierungssession

#### 4. Selective Deep Instructor Feedback

- **Wann**: 3 Punkte pro Lernende
    - Opening session practice
    - Mid-program milestone project
    - Capstone/Final project
- **Format**:
    - 2 Stärken (mit Code-Beispielen)
    - 2 Wachstumsbereiche (mit konkreten Vorschlägen)
    - 1 reflektierende Frage
- **Medium**: Video-Feedback mit Screen-Annotation (effizienter als
  schriftlich)

#### 5. Portfolio Development

- **Was**: Lernende dokumentieren abgeschlossene Projekte
- **Inhalt pro Projekt**:
    - Problem-Beschreibung
    - Gewählter Ansatz
    - Konsultierte Ressourcen
    - Investierte Zeit
    - Reflexion über Lernergebnisse

### Implementierungsschritte

- [ ] Quizzes überprüfen und mit detailliertem Feedback ausstatten
- [ ] Challenge-Problem-Infrastruktur setup (Auto-Testing)
- [ ] Rubrik für Peer Code Review entwickeln + dokumentieren
- [ ] Portfolio-Vorlage erstellen
- [ ] Video-Feedback-Template erstellen
- [ ] Pilot mit einer kleinen Lerngruppe

### Offene Fragen

1. Ist dieses Three-Track-Modell für den weiterbildenden Masterstudiengang
   realistisch?
2. Gibt es bereits Assessment-Strukturen, die beibehalten werden sollten?
3. Automatisiertes Testing: Welche Tools? (`pytest`, `nbgrader`, andere?)
4. Peer Review: Organisatorisch im Fernstudium umsetzbar? (Moodle, GitHub
   Discussions?)

### Deliverables (wenn implementiert)

- [ ] Überarbeitete Quizzes mit spezifischem Feedback (alle 50+)
- [ ] 5-10 Challenge-Probleme mit Test-Suite
- [ ] Structured Peer Review Rubric (1 Dokument)
- [ ] Portfolio-Template (Google Doc / Markdown-Vorlage)
- [ ] Assessment-Übersichtsdokument (welches Assessment wann?)

---

**Dokument erstellt**: 17.10.2025<br>
**Status**: Optional / Für zukünftige
Überlegungen
