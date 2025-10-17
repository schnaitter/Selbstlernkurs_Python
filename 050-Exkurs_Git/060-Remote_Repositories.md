---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Remote Repositories und Zusammenarbeit

Bisher haben Sie mit Git nur lokal auf Ihrem Computer gearbeitet. In diesem
Kapitel lernen Sie, wie Sie Ihre Repositories mit einem Server (z.B. GitHub
oder GitLab) synchronisieren können. Bietet der Server mehr Funktionalitäten
als reines Git (Issue-Verwaltung, Pull-/Merge-Requests, …) so wird dieser auch
manchmal Git Forge genannt.

## Was ist ein Remote Repository?

Ein **Remote Repository** (oft einfach "Remote" genannt) ist eine Kopie Ihres
Git-Projekts auf einem Server im Internet. Die wichtigsten Vorteile:

- **Backup**: Ihre Arbeit ist gesichert, falls Ihr Computer ausfällt
- **Zusammenarbeit**: Mehrere Personen können am selben Projekt arbeiten
- **Teilen**: Sie können Ihr Projekt öffentlich zugänglich machen
- **Von überall arbeiten**: Zugriff von verschiedenen Computern

## Hosting-Plattformen

Die bekanntesten Plattformen für Git-Repositories:

::::{grid}
:gutter: 2

:::{grid-item-card} GitHub

- Größte Plattform, sehr verbreitet
- Kostenlose öffentliche und private Repositories
- [https://github.com](https://github.com)

:::

:::{grid-item-card} GitLab

- Open-Source-Alternative zu GitHub
- Kann auch selbst gehostet werden
- [https://gitlab.com](https://gitlab.com)

:::

:::{grid-item-card} Gitea/Forgejo

- Leichtgewichtige, selbst-hostbare Lösung
- Open Source
- Oft von Institutionen verwendet

:::

::::

TODO: Zusätzliche Erklärungen mit dem GitLab der HU

In diesem Kurs verwenden wir **GitHub** als Beispiel, aber die Konzepte gelten
für alle Plattformen.

## Ein Repository klonen: git clone

Der häufigste Weg, mit einem Remote-Repository zu arbeiten, ist es zu
**klonen** – das heißt, eine vollständige Kopie herunterzuladen.

### Beispiel: Diesen Kurs klonen

Sie haben diesen Kurs wahrscheinlich bereits geklont, als Sie ihn eingerichtet
haben:

```bash
$ git clone https://github.com/schnaitter/Selbstlernkurs_Python.git
```

**Was passiert?**

1. Git lädt das Repository herunter
2. Erstellt einen Ordner mit dem Repository-Namen
3. Richtet automatisch eine Verbindung zum Remote-Repository ein
4. Checkt den Standard-Branch (meist `main`) aus

### Die Remote-Verbindung anzeigen

Wenn Sie ein Repository geklont haben, ist automatisch eine Remote-Verbindung
eingerichtet:

```bash
$ git remote -v
```

**Ausgabe:**

```
origin  https://github.com/schnaitter/Selbstlernkurs_Python.git (fetch)
origin  https://github.com/schnaitter/Selbstlernkurs_Python.git (push)
```

:::::{margin}
:::{hint} Typische Remote-Namen

**origin** ist der Standard-Name für die Remote-Verbindung. Sie können mehrere
Remotes haben, aber `origin` ist die wichtigste.

**upstream** wird normalerweise genutzt, wenn man mit dem Fork eines
Repositoriums arbeitet. Ein Fork ist eine Kopie eines Repos, wobei oft eine
Verbindung beibehalten wird über die Änderungen wieder an das original Repo
zurückgespielt werden können.

Das Repositorium `schnaitter/Selbstlernkurs_Python` ist in meinem lokalen Klon
als `origin` bezeichnet. Wenn Sie es sich klonen, dann ist es bei Ihnen
ebenfalls `origin`. Sie haben dann aber keine Rechte um Änderungen zum Server
zu übertragen (`push`, s.u.).

Wollen Sie Ihre eigene Version anlegen und selbst Änderungen vornehmen und
diese auf einem Git-Server speichern, dann müssen Sie zuerst einen Fork
anlegen. Dieser könnte `musterfrau/Selbstlernkurs_Python` heißen. Wenn Sie
diesen dann klonen wäre `musterfrau/Selbstlernkurs_Python` Ihre `origin` und
`schnaitter/Selbstlernkurs_Python` Ihr `upstream`.

Andere Namen sind möglich treten aber selten auf.

:::
:::::

## Änderungen herunterladen: git pull

Wenn das Remote-Repository aktualisiert wurde (z.B. durch andere Personen oder
von einem anderen Computer), laden Sie die Änderungen mit:

```bash
$ git pull
```

**Was passiert?**

1. Git fragt das Remote-Repository: "Gibt es neue Commits?"
2. Lädt neue Commits herunter
3. Führt sie mit Ihrem lokalen Stand zusammen (merge)

**Beispiel-Ausgabe:**

```
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 5 (delta 2), reused 5 (delta 2)
Unpacking objects: 100% (5/5), done.
From https://github.com/schnaitter/Selbstlernkurs_Python
   a1b2c3d..e4f5g6h  main -> origin/main
Updating a1b2c3d..e4f5g6h
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

:::::{tip} Kurs-Updates abrufen

Wenn neue Kapitel oder Übungen zu diesem Kurs hinzugefügt werden, können Sie
sie mit `git pull` herunterladen!

:::::

## Änderungen hochladen: git push

Wenn Sie lokal Commits erstellt haben und diese auf den Server hochladen
möchten:

```bash
$ git push
```

**Voraussetzungen:**

- Sie müssen Schreibrechte für das Repository haben
- Ihr lokaler Branch muss mit einem Remote-Branch verknüpft sein

**Beispiel-Ausgabe:**

```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 280 bytes | 280.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/ihre-username/ihr-projekt.git
   a1b2c3d..e4f5g6h  main -> main
```

## Ein neues Remote-Repository erstellen

Szenario: Sie haben ein lokales Projekt und möchten es auf GitHub
veröffentlichen.

### Schritt 1: Repository auf GitHub erstellen

1. Gehen Sie zu [https://github.com](https://github.com) und loggen Sie sich
   ein
2. Klicken Sie auf "New repository" (grüner Button)
3. Geben Sie einen Namen ein (z.B. "mein-python-projekt")
4. Wählen Sie öffentlich (public) oder privat (private)
5. **Wichtig**: Erstellen Sie KEIN README, keine .gitignore, keine Lizenz (das
   machen wir lokal)
6. Klicken Sie auf "Create repository"

GitHub zeigt Ihnen jetzt Anweisungen. Wir folgen denen für ein "existing
repository":

### Schritt 2: Lokales Repository mit Remote verbinden

In Ihrem lokalen Projektordner:

```bash
# Remote-Verbindung hinzufügen (URL von GitHub kopieren!)
$ git remote add origin https://github.com/ihr-username/mein-python-projekt.git

# Branch umbenennen (falls noch "master" statt "main")
$ git branch -M main

# Zum ersten Mal hochladen
$ git push -u origin main
```

:::::{margin}
:::{hint} Verknüpfung von Branches

**Das `-u` Flag** (oder `--set-upstream`) verknüpft Ihren lokalen `main`-Branch
mit dem Remote-Branch. Ab jetzt reicht `git push` ohne weitere Angaben.

:::
:::::

### Schritt 3: Weitere Commits hochladen

Ab jetzt können Sie normal arbeiten:

```bash
# Datei ändern
$ echo "print('Neue Funktion')" >> programm.py

# Committen
$ git add programm.py
$ git commit -m "Neue Funktion hinzugefügt"

# Hochladen
$ git push
```

## Der komplette Workflow: lokal und remote

```{mermaid}
graph TB
    subgraph "Lokaler Computer"
        WD[Working Directory]
        SA[Staging Area]
        LR[Local Repository]
    end

    subgraph "GitHub / GitLab"
        RR[Remote Repository]
    end

    WD -->|git add| SA
    SA -->|git commit| LR
    LR -->|git push| RR
    RR -->|git pull| LR
    LR -->|git checkout| WD

    style WD fill:#e1f5ff
    style SA fill:#fff4e1
    style LR fill:#e1ffe1
    style RR fill:#ffe1e1
```

## Authentifizierung: SSH vs. HTTPS

Wenn Sie auf ein Remote-Repository zugreifen, müssen Sie sich authentifizieren.
Es gibt zwei Methoden:

### HTTPS (einfacher für Anfänger)

```bash
$ git clone https://github.com/username/repo.git
```

**Vorteile:**

- Einfach einzurichten
- Funktioniert überall (auch hinter Firewalls)

**Nachteile:**

- Sie müssen bei jedem `push` Ihren Benutzernamen und ein Token eingeben

**Token erstellen (GitHub):**

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens
   (classic)
2. "Generate new token" → Berechtigungen auswählen (mindestens `repo`)
3. Token kopieren (wird nur einmal angezeigt!)
4. Beim `git push` Token als Passwort eingeben

### SSH (für Fortgeschrittene)

```bash
$ git clone git@github.com:username/repo.git
```

**Vorteile:**

- Keine wiederholte Authentifizierung nötig
- Sicherer

**Nachteile:**

- Einrichtung etwas komplexer (SSH-Keys erstellen)

:::::{tip} SSH-Setup

Falls Sie SSH verwenden möchten, finden Sie Anleitungen in der
GitHub-Dokumentation:
[https://docs.github.com/en/authentication/connecting-to-github-with-ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
:::::

## Häufige Situationen

### Szenario 1: Lokale und remote Änderungen

Sie haben lokal gearbeitet, aber jemand anderes hat auch Änderungen
hochgeladen.

```bash
$ git push
```

**Fehlermeldung:**

```
! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/...'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
```

**Lösung:**

```bash
# Erst remote Änderungen herunterladen
$ git pull

# Dann hochladen
$ git push
```

### Szenario 2: Ein geklontes Repository aktualisieren

Sie haben ein Repository vor Wochen geklont. Jetzt möchten Sie die neuesten
Änderungen:

```bash
$ cd pfad/zum/repository
$ git pull
```

### Szenario 3: Remote-URL ändern

Sie haben Ihr Repository umbenannt oder die URL geändert:

```bash
# Aktuelle URL anzeigen
$ git remote -v

# URL ändern
$ git remote set-url origin https://github.com/neue-url/neues-repo.git

# Überprüfen
$ git remote -v
```

## Zusammenarbeit: Ein einfaches Beispiel

Angenommen, Sie arbeiten mit einer Kollegin zusammen:

**Sie (Computer A):**

```bash
# Datei ändern
$ echo "# Neue Notiz" >> notizen.md
$ git add notizen.md
$ git commit -m "Notiz hinzugefügt"
$ git push
```

**Ihre Kollegin (Computer B):**

```bash
# Änderungen herunterladen
$ git pull

# Jetzt hat sie Ihre Änderung!
$ cat notizen.md
```

**Ihre Kollegin macht auch Änderungen:**

```bash
$ echo "# Weitere Notiz" >> notizen.md
$ git add notizen.md
$ git commit -m "Weitere Notiz ergänzt"
$ git push
```

**Sie holen die Änderungen:**

```bash
$ git pull
```

## Was sind Merge-Konflikte?

Wenn zwei Personen **dieselbe Zeile in derselben Datei** ändern, entsteht ein
**Merge-Konflikt**. Git kann nicht automatisch entscheiden, welche Änderung
korrekt ist.

:::::{tip} Vereinfachte Behandlung

Merge-Konflikte und deren Auflösung sind ein fortgeschrittenes Thema. In diesem
Kurs arbeiten Sie zunächst alleine an Ihren Projekten, sodass Konflikte selten
auftreten.

**Grundregel**: Wenn Sie alleine arbeiten und Git sagt "Konflikt", haben Sie
wahrscheinlich vergessen, `git pull` vor dem Arbeiten auszuführen.

**Tipp**: Immer erst `git pull`, dann arbeiten, dann `git push`.

:::::

## Zusammenfassung

Die wichtigsten Befehle für Remote-Repositories:

| Befehl                        | Beschreibung                        |
| ----------------------------- | ----------------------------------- |
| `git clone <url>`             | Repository herunterladen            |
| `git remote -v`               | Remote-Verbindungen anzeigen        |
| `git pull`                    | Änderungen vom Server herunterladen |
| `git push`                    | Änderungen zum Server hochladen     |
| `git remote add origin <url>` | Remote-Verbindung hinzufügen        |

### Typischer Workflow

```bash
# Am Anfang: Repository klonen
$ git clone https://github.com/username/projekt.git
$ cd projekt

# Regelmäßig: Vor Arbeitsbeginn aktualisieren
$ git pull

# Arbeiten: Änderungen machen und committen
$ git add .
$ git commit -m "Änderungen beschrieben"

# Am Ende: Hochladen
$ git push
```

:::::{admonition} 💪 Übung

Erstellen Sie Ihr erstes Remote-Repository:

1. Erstellen Sie auf GitHub ein neues Repository (öffentlich oder privat)
2. Erstellen Sie lokal ein Projekt mit mindestens 2 Commits
3. Verbinden Sie das lokale Repository mit GitHub
4. Pushen Sie Ihre Commits zu GitHub
5. Machen Sie eine kleine Änderung auf GitHub (im Web-Editor)
6. Pullen Sie die Änderung zu Ihrem lokalen Computer

Dokumentieren Sie jeden Schritt mit `git status` und `git log`!

:::::

Im nächsten Kapitel lernen Sie **Branches** kennen – ein mächtiges Feature zum
parallelen Arbeiten an verschiedenen Features.
