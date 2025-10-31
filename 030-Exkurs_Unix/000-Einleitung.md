---
short_title: "Exkurs: Unix"
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Exkurs: Unix

```{seealso} 🎓 Lernziele
:icon: false

In diesem Kapitel erlernen Sie, …

- … was Unix ist und warum es für Python-Entwicklung wichtig ist.
- … wie Sie das Terminal öffnen und grundlegende Befehle nutzen.
- … wie Sie im Dateisystem navigieren und Pfade verstehen.
- … wie Sie Dateien und Verzeichnisse verwalten.
- … wie Sie Python-Skripte ausführbar machen.
- … wie Sie effizient mit Pipes, Wildcards und weiteren Unix-Tools arbeiten.

```

:::::{tip} Optional, aber teilw. in nachfolgenden Inhalten genutzt
:class: dropdown

Dieser Exkurs ist optional – Sie müssen ihn nicht komplett durcharbeiten, um
mit dem Kurs fortzufahren.

**Aber:** Einzelne Inhalte aus diesem Exkurs werden in späteren Kapiteln
vorausgesetzt. Dort wird dann auf die entsprechenden Abschnitte verwiesen (z.B.
für Dateirechte bei [ausführbaren
Skripten](../020-Projekt_Taschenrechner_I/050-Ausführbare_Skripte.md)).

Wenn Sie bereits mit Unix/Linux vertraut sind, können Sie diesen Exkurs
überspringen oder als Nachschlagewerk nutzen.

**Auf JupyterHub:** Alle Inhalte dieses Exkurses funktionieren direkt auf
JupyterHub. Sie können das Terminal dort über "File → New → Terminal" öffnen.

:::::

Dieser Exkurs führt Sie in die Unix-Kommandozeile ein, die für Python-Entwicklung
unverzichtbar ist. Sie lernen zunächst, [was Unix ist](010-Was_ist_Unix.md) und
warum diese Kenntnisse auch für Windows-Nutzer\*innen wichtig sind. Anschließend
verstehen Sie den Unterschied zwischen [Terminal und Shell](020-Terminal_und_Shell.md)
und öffnen Ihre erste Kommandozeile.

In den Kapiteln zur [Navigation im Dateisystem](030-Dateisystem_Navigation.md)
und [Dateiverwaltung](040-Dateiverwaltung.md) lernen Sie, wie Sie sich im
Verzeichnisbaum bewegen (`cd`, `ls`, `pwd`), absolute und relative Pfade verstehen
und Dateien sowie Verzeichnisse erstellen, kopieren, verschieben und löschen –
alles über das Terminal.

Das Kapitel zu [Berechtigungen](050-Berechtigungen.md) ist besonders relevant
für Python-Entwicklung: Sie lernen das Unix-Berechtigungssystem kennen und machen
Ihre Python-Skripte ausführbar (`chmod +x`). Die [nützlichen Befehle](060-Nützliche_Befehle.md)
zeigen Ihnen fortgeschrittene Techniken wie Pipes, Wildcards und Text-Verarbeitung,
die Ihre Arbeit im Terminal deutlich effizienter machen.

Der Exkurs schließt mit [praktischen Übungen](070-Übungen.md) ab, in denen Sie
alle gelernten Befehle in Szenarien aus der Bibliotheks- und Informationspraxis
anwenden – vom Erstellen einer Projektstruktur bis zur Verarbeitung von Metadaten.
