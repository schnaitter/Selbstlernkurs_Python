---
short_title: Remote Repositories
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Remote Repositories und Zusammenarbeit

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

Bisher haben Sie mit {term}`Git` nur lokal auf Ihrem Computer gearbeitet. In diesem
Kapitel lernen Sie, wie Sie Ihre Repositories mit einem Server (z.B. GitHub
oder GitLab) synchronisieren und gemeinsam mit anderen nutzen.

## Was ist ein Remote Repository?

Ein **Remote {term}`Repository`** (oft einfach "Remote" genannt) ist eine Kopie Ihres
Git-Projekts auf einem Server im Internet. Die wichtigsten Vorteile:

- **Backup**: Ihre Arbeit ist gesichert, falls Ihr Computer ausfällt
- **Zusammenarbeit**: Mehrere Personen können am selben Projekt arbeiten
- **Teilen**: Sie können Ihr Projekt öffentlich zugänglich machen
- **Von überall arbeiten**: Zugriff von verschiedenen Computern

## Hosting-Plattformen

Die bekanntesten Plattformen:

- **GitHub**: Größte Plattform, kostenlose öffentliche und private
  Repositories → [github.com](https://github.com)
- **GitLab**: Open-Source-Alternative, auch selbst hostbar
  → [gitlab.com](https://gitlab.com), für die HU Berlin:
  [scm.cms.hu-berlin.de](https://scm.cms.hu-berlin.de)
- **Gitea/Forgejo**: Leichtgewichtig, selbst hostbar, oft von Institutionen
  verwendet

In diesem Kurs verwenden wir **GitHub** als Beispiel – die Konzepte gelten
aber für alle Plattformen.

## Ein Repository klonen: git clone

Der häufigste Weg, mit einem Remote-Repository zu arbeiten, ist es zu
**klonen** – eine vollständige Kopie herunterzuladen. So haben Sie
wahrscheinlich auch diesen Kurs geklont:

```bash
git clone https://github.com/schnaitter/Selbstlernkurs_Python.git
```

**Was passiert?**

1. Git lädt das Repository herunter
2. Erstellt einen Ordner mit dem Repository-Namen
3. Richtet automatisch eine Verbindung zum Remote-Repository ein
4. Checkt den Standard-{term}`Branch` (meist `main`) aus

Die eingerichtete Verbindung heißt standardmäßig `origin`:

```bash
git remote -v
# origin  https://github.com/schnaitter/Selbstlernkurs_Python.git (fetch)
# origin  https://github.com/schnaitter/Selbstlernkurs_Python.git (push)
```

## Änderungen herunterladen: git pull

Wenn das Remote-Repository aktualisiert wurde (z.B. durch andere Personen oder
von einem anderen Computer), laden Sie die Änderungen mit:

```bash
git pull
```

Git fragt das Remote nach neuen Commits, lädt sie herunter und führt sie mit
Ihrem lokalen Stand zusammen (merge).

:::::{tip} Kurs-Updates abrufen
Wenn neue Kapitel oder Übungen zu diesem Kurs hinzugefügt werden, können Sie
sie mit `git pull` herunterladen!
:::::

## Änderungen hochladen: git push

Haben Sie lokal Commits erstellt und möchten diese auf den Server laden:

```bash
git push
```

**Voraussetzungen:** Sie brauchen Schreibrechte, und Ihr lokaler Branch muss
mit einem Remote-Branch verknüpft sein.

## Ein neues Remote-Repository erstellen

Szenario: Sie haben ein lokales Projekt und möchten es auf GitHub
veröffentlichen.

### Schritt 1: Repository auf GitHub erstellen

1. Auf [github.com](https://github.com) einloggen und "New repository" wählen
2. Namen vergeben (z.B. "mein-python-projekt")
3. Öffentlich (public) oder privat (private) wählen
4. **Wichtig**: KEIN README, keine `.gitignore`, keine Lizenz anlegen
   (das machen wir lokal)
5. "Create repository" klicken

### Schritt 2: Lokales Repository mit Remote verbinden

```bash
# Remote-Verbindung hinzufügen (URL von GitHub kopieren!)
git remote add origin https://github.com/ihr-username/mein-python-projekt.git

# Branch umbenennen (falls noch "master" statt "main")
git branch -M main

# Zum ersten Mal hochladen
git push -u origin main
```

:::::{margin}
**Das `-u` Flag** (oder `--set-upstream`) verknüpft Ihren lokalen
`main`-Branch mit dem Remote-Branch. Ab jetzt reicht `git push` ohne weitere
Angaben.
:::::

### Schritt 3: Weitere Commits hochladen

```bash
git add programm.py
git commit -m "Neue Funktion hinzugefügt"
git push
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
```

## Authentifizierung: SSH vs. HTTPS

### HTTPS (einfacher für Anfänger\*innen)

```bash
git clone https://github.com/username/repo.git
```

Einfach einzurichten und funktioniert überall – dafür müssen Sie sich bei jedem
`push` mit einem Token authentifizieren. Auf GitHub erstellen Sie ein Token
unter *Settings → Developer settings → Personal access tokens*.

### SSH (für Fortgeschrittene)

```bash
git clone git@github.com:username/repo.git
```

Keine wiederholte Authentifizierung, dafür ist die Einrichtung eines
SSH-Schlüssels etwas aufwendiger.

:::::{tip} SSH-Setup
Anleitungen finden Sie in der GitHub-Dokumentation:
[docs.github.com/…/connecting-to-github-with-ssh](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
:::::

## Häufige Situationen

### Push wird abgelehnt

Wenn jemand anderes Änderungen hochgeladen hat, lehnt Git Ihren `push` ab:

```
! [rejected]  main -> main (fetch first)
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. ...
```

**Lösung:**

```bash
git pull    # erst herunterladen und zusammenführen
git push    # dann erneut hochladen
```

### Remote-URL ändern

```bash
git remote -v
git remote set-url origin https://github.com/neue-url/neues-repo.git
git remote -v
```

## Zusammenfassung

| Befehl                        | Beschreibung                        |
| ----------------------------- | ----------------------------------- |
| `git clone <url>`             | Repository herunterladen            |
| `git remote -v`               | Remote-Verbindungen anzeigen        |
| `git pull`                    | Änderungen vom Server herunterladen |
| `git push`                    | Änderungen zum Server hochladen     |
| `git remote add origin <url>` | Remote-Verbindung hinzufügen        |

### Typischer Workflow

```bash
git clone https://github.com/username/projekt.git
cd projekt

git pull                                # vor dem Arbeiten aktualisieren
git add .
git commit -m "Änderungen beschrieben"
git push                                # am Ende hochladen
```

```{exercise} Übung: Erstes Remote-Repository
:label: git-remote-repository

Erstellen Sie Ihr erstes Remote-Repository:

1. Erstellen Sie auf GitHub ein neues Repository (öffentlich oder privat)
2. Erstellen Sie lokal ein Projekt mit mindestens 2 Commits
3. Verbinden Sie das lokale Repository mit GitHub und pushen Sie
4. Machen Sie eine kleine Änderung auf GitHub (im Web-Editor)
5. Pullen Sie die Änderung zu Ihrem lokalen Computer
```

Im nächsten Kapitel lernen Sie **Branches** kennen – ein mächtiges Feature zum
parallelen Arbeiten an verschiedenen Features.
