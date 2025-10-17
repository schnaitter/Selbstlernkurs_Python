---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Was ist Versionskontrolle?

```{seealso} 🎓 Lernziele
:icon: false

Nach diesem Exkurs können Sie:

- Git lokal auf Ihrem Computer nutzen
- Versionen Ihrer Python-Projekte verwalten
- Änderungen nachvollziehen und rückgängig machen
- Mit Remote-Repositories (GitHub/GitLab) arbeiten
- Ihre Lösungen zu den Kursaufgaben versionieren

```

## Das Problem

Wer kennt das nicht? Man arbeitet an einem Python-Skript, speichert
verschiedene Versionen und am Ende sieht der Dateiordner so aus:

```
taschenrechner.py
taschenrechner_v2.py
taschenrechner_v2_neu.py
taschenrechner_v3.py
taschenrechner_final.py
taschenrechner_wirklich_final.py
taschenrechner_wirklich_final_v2.py
```

Bei dieser Arbeitsweise verliert man schnell den Überblick:

- Welche Datei enthält welche Änderungen?
- Warum wurde etwas geändert?
- Wie komme ich zu einer älteren Version zurück?
- Wie kann ich mit anderen zusammenarbeiten, ohne die Arbeit der anderen zu
  überschreiben?

## Die Lösung: Versionskontrollsysteme

**Versionskontrollsysteme** (auch Version Control Systems oder VCS) lösen diese
Probleme, indem sie:

- **Alle Änderungen protokollieren**: Jede Änderung wird mit Zeitstempel,
  Autor\*in und Beschreibung gespeichert
- **Versionen verwalten**: Man kann zu jeder beliebigen früheren Version
  zurückkehren
- **Zusammenarbeit ermöglichen**: Mehrere Personen können gleichzeitig am
  selben Projekt arbeiten
- **Änderungen nachvollziehbar machen**: Man sieht genau, wer was wann und
  warum geändert hat

## Git: Das Standard-Versionskontrollsystem

**Git** ist das heute meistgenutzte Versionskontrollsystem. Es wurde 2005 von
Linus Torvalds (dem Erfinder von Linux) entwickelt und ist:

- **Dezentral**: Jede\*r hat eine vollständige Kopie der gesamten
  Versionsgeschichte
- **Schnell**: Die meisten Operationen funktionieren lokal ohne
  Internetverbindung
- **Flexibel**: Unterstützt verschiedene Arbeitsweisen und Workflows
- **Open Source**: Kostenlos und frei verfügbar

## Git vs. GitHub/GitLab

Ein häufiges Missverständnis: **Git und GitHub sind nicht dasselbe!**

::::{grid} 2
:gutter: 2

:::{card}
:header: Git

Das Versionskontrollsystem, das lokal auf Ihrem Computer läuft. Git speichert
und verwaltet Versionen Ihrer Dateien.
:::

:::{card}
:header: GitHub / GitLab / Gitea
Online-Plattformen, die Git-Repositories im Internet hosten. Sie bieten
zusätzliche Funktionen wie:

- Zentrale Ablage für gemeinsame Projekte
- Web-Oberfläche zur Verwaltung
- Kollaborations-Tools (Issues, Pull Requests)
- Backup Ihrer Arbeit in der Cloud
  :::

::::

Man kann Git auch **ohne** GitHub/GitLab nutzen – rein lokal auf dem eigenen
Computer. In diesem Kurs werden wir zunächst die lokale Nutzung kennenlernen,
bevor wir uns mit Remote-Plattformen beschäftigen.

## Warum ist Git wichtig für Bibliotheks- und Informationswissenschaftler\*innen?

:::::{margin}
:::{hint} Hinweis

Viele Open-Source-Bibliothekssysteme und -Tools werden mit Git versioniert und
auf GitHub/GitLab kollaborativ entwickelt. Wenn Sie diese Tools nutzen oder
anpassen möchten, sind Git-Kenntnisse sehr hilfreich!

:::
:::::

In der Bibliotheks- und Informationspraxis arbeiten Sie häufig mit:

- **Skripten zur Datenverarbeitung**: Katalogdaten konvertieren, Statistiken
  erstellen
- **Konfigurationsdateien**: Einstellungen für Bibliothekssysteme
- **Dokumentation**: Anleitungen, Workflows, Best Practices

Git hilft dabei:

- Änderungen an Skripten und Konfigurationen nachvollziehbar zu dokumentieren
- Mit Kolleg\*innen an gemeinsamen Projekten zu arbeiten
- Fehler rückgängig zu machen, ohne Panik zu bekommen
- Code und Dokumentation zu teilen und weiterzuentwickeln
