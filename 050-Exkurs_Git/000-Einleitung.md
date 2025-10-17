---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Exkurs: Git

```{seealso} 🎓 Lernziele
:icon: false

Nach diesem Exkurs können Sie:

- Git lokal auf Ihrem Computer nutzen
- Versionen Ihrer Python-Projekte verwalten
- Änderungen nachvollziehen und rückgängig machen
- Mit Remote-Repositories (GitHub/GitLab) arbeiten
- Ihre Lösungen zu den Kursaufgaben versionieren

```

:::::{tip} Optional, aber empfohlen

Dieser Exkurs ist optional, aber _empfohlen_. Einige weiterführende Übungen
im Kurs setzen voraus, dass Sie mit Git umgehen können. Es wird dort auf die
entsprechenden Abschnitte hier im Exkurs verwiesen.

Wenn Sie bereits Git-Erfahrung haben, können Sie diesen Exkurs überspringen
oder als Nachschlagewerk nutzen.

:::::

Dieser Exkurs führt Sie in Git ein, das Standard-Versionskontrollsystem für
Software-Entwicklung. Sie lernen zunächst, [warum Versionskontrolle wichtig
ist](010-Was_ist_Versionskontrolle.md) und welche Probleme Git löst.
Anschließend [installieren und
konfigurieren](020-Installation_Konfiguration.md) Sie Git auf Ihrem Computer.

Die Kapitel zu [Grundkonzepten](030-Grundkonzepte.md) und [ersten
Schritten](040-Erste_Schritte.md) erklären die zentrale Arbeitsweise von Git:
Working Directory, Staging Area und Repository. Sie lernen, wie Sie Änderungen
vorbereiten (git add) und als Commits speichern (git commit), und wie Sie [die
Historie](050-Historie.md) Ihres Projekts nachvollziehen können.

Im Abschnitt zu [Remote-Repositories](060-Remote_Repositories.md) arbeiten Sie
mit GitHub oder GitLab – Sie laden bestehende Projekte herunter (clone), holen
Updates (pull) und veröffentlichen eigene Änderungen (push). Das Kapitel zu
[Branches](070-Branches.md) zeigt, wie Sie parallel an verschiedenen Features
arbeiten können, ohne die Hauptversion zu beeinträchtigen.

Für die Kursarbeit besonders relevant ist das Kapitel [Git im
Kurs](080-Git_im_Kurs.md), das erklärt, wie Sie Kurs-Repositories nutzen,
eigene Lösungen versionieren und typische Fehler vermeiden. [Best
Practices](090-Best_Practices.md) zu Commit-Größen, aussagekräftigen
Commit-Messages und Sicherheit helfen Ihnen, Git professionell einzusetzen.

Der Exkurs schließt mit einer [praktischen Übung](100-Uebung.md) ab, in der Sie
ein kleines Python-Projekt von Grund auf mit Git verwalten – von der
Initialisierung über mehrere Commits bis zur optionalen Veröffentlichung auf
GitHub.
