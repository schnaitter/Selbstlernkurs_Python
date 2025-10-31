---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Lokale Installation

## Installation von Python

Für die lokale Nutzung dieses Kurses benötigen Sie eine
{term}`Python`-Installation. Es gibt zwei empfohlene Wege: die
Standard-Python-Installation von [Python.org](https://www.python.org/) oder die
[Anaconda](https://www.anaconda.com/)-Distribution.

### Option A: Python.org (Standard-Installation)

Die offizielle Python-Installation eignet sich für die meisten Anwendungsfälle
und bietet maximale Flexibilität.

```{dropdown} **Windows**

1. Besuchen Sie die [offizielle
   Python-Download-Seite](https://www.python.org/downloads/windows/)
2. Laden Sie die neueste Python 3.x Version herunter (empfohlen: Python 3.13
   oder 3.14)
3. Folgen Sie der [detaillierten
   Windows-Installationsanleitung](https://docs.python.org/3/using/windows.html)
   von Python.org
4. **Wichtig:** Aktivieren Sie "Add Python to PATH" während der Installation

```

```{dropdown} **macOS**

1. Besuchen Sie die [offizielle
   Python-Download-Seite](https://www.python.org/downloads/macos/)
2. Laden Sie die neueste Python 3.x Version herunter
3. Folgen Sie der
   [macOS-Installationsanleitung](https://docs.python.org/3/using/mac.html) von
Python.org
4. Alternativ: Installation über [Homebrew](https://brew.sh/): `brew install
   python`

```

````{dropdown} **Linux**

- **Ubuntu/Debian:** Folgen Sie der [offiziellen
  Linux-Anleitung](https://docs.python.org/3/using/unix.html)
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip python3-venv
    ```
- **Fedora/CentOS:** `sudo dnf install python3 python3-pip`
- **Arch Linux:** `sudo pacman -S python python-pip`

````

**Installation überprüfen:**

```bash
$ python3 --version
Python 3.13.7
# oder auf manchen Systemen:
$ python --version
```

Die bei Ihnen installierte Python-Version kann von der hier gezeigten
abweichen. Solange Sie eine relativ moderne Python-Version haben (>= 3.11)
können Sie die Inhalte des Kurses problemlos durcharbeiten.

### Option B: Anaconda Distribution

````{margin}

```{caution} Lizenz von Anaconda

Für die private Nutzung und die Nutzung als Student\*in ist Anaconda für Sie
kostenlos. Wollen Sie die Python-Distribution in einem Arbeitskontext nutzen
sollten Sie abklären ob Sie eine Lizenz kaufen müssen.

```
````

Anaconda ist besonders für Data Science und wissenschaftliche Anwendungen
geeignet und bringt viele nützliche Pakete mit.

**Alle Betriebssysteme:**

1. Besuchen Sie die [offizielle
   Anaconda-Download-Seite](https://www.anaconda.com/download)
2. Laden Sie die Anaconda-Distribution für Ihr Betriebssystem herunter
3. Folgen Sie der [detaillierten
   Installationsanleitung](https://docs.anaconda.com/anaconda/install/) von
   Anaconda
4. Nach der Installation steht Ihnen der [Anaconda
   Navigator](https://docs.anaconda.com/navigator/) zur Verfügung

**Vorteile von Anaconda:**

- Integrierte wissenschaftliche Pakete ({term}`NumPy`, {term}`Pandas`,
  {term}`Matplotlib`, etc.)
- Anaconda Navigator für grafische Verwaltung
- Conda Package Manager für einfache Paketverwaltung
- Jupyter Notebook bereits vorinstalliert

**Installation überprüfen:**

```bash
$ conda --version
$ python3 --version
```

## Download der Inhalte

Um die Kursinhalte lokal zu nutzen, benötigen Sie Git und müssen das Repository
klonen.

### Git installieren

Git ist ein Versionskontrollsystem, das für das Herunterladen der Kursinhalte
benötigt wird.

```{dropdown} **Windows**

1. Besuchen Sie die [offizielle
   Git-Download-Seite](https://git-scm.com/download/win)
2. Laden Sie Git für Windows herunter
3. Folgen Sie der [detaillierten
   Windows-Installationsanleitung](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#_installing_on_windows)
4. Git Bash wird mitinstalliert und bietet eine Unix-ähnliche Kommandozeile

```

```{dropdown} **macOS**

1. Git ist oft bereits vorinstalliert. Überprüfen Sie mit: `git --version`
2. Falls nicht installiert:
    - Installieren Sie Git über die Installation der Entwicklerwerkzeuge mit
      dem Befehl `xcode-select --install`.
    - Besuchen Sie die [Git-Download-Seite](https://git-scm.com/download/mac)
    - Alternativ über [Homebrew](https://brew.sh/): `brew install git`
3. Folgen Sie der
   [macOS-Installationsanleitung](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#_installing_on_macos)

```

```{dropdown} **Linux**

- **Ubuntu/Debian:** `sudo apt install git`
- **Fedora:** `sudo dnf install git`
- **Arch Linux:** `sudo pacman -S git`
- Detaillierte Anweisungen in der [offiziellen Linux-Anleitung](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#_installing_on_linux)

```

**Git konfigurieren:**

Nach der Installation konfigurieren Sie Git mit Ihren Daten:

```bash
$ git config --global user.name "Ihr Name"
$ git config --global user.email "ihre.email@example.com"
```

### Repository klonen

1. Öffnen Sie ein Terminal (Linux/macOS) oder Git Bash (Windows)
2. Navigieren Sie zu dem Verzeichnis, in dem Sie den Kurs speichern möchten
3. Klonen Sie das Repository:

    ```bash
    # Klonen (Herunterladen) der Kursinhalte
    $ git clone https://github.com/schnaitter/Selbstlernkurs_Python.git
    # Wechsel in den neu erstellten Ordner mit den Kursinhalten
    $ cd Selbstlernkurs_Python
    # Ausgabe der Unterordner und Dateien im heruntergeladenen Ordner
    $ ls
    ```

**Verzeichnisstruktur:**

Nach dem Klonen erhalten Sie folgende Struktur:

- `000-Einleitung/` - Allgemeine Informationen zum Kurs
- `010-Installation_Technik/` - Diese Installationsanleitung
- `020-Python_Grundlagen/` - Grundlagen der Python-Programmierung
- Weitere Kapitel entsprechend dem Kursaufbau

## Einrichten eines Virtuellen Environments

Virtuelle Umgebungen (Virtual Environments) isolieren Python-Projekte
voneinander und verhindern Konflikte zwischen verschiedenen Paketen und
Versionen.

### Option A: Nutzung des Python Moduls `venv`

`venv` ist das standardmäßige Tool für virtuelle Umgebungen in Python und
funktioniert mit jeder Python-Installation.

**Virtuelles Environment erstellen:**

```bash
# Im Kurs-Verzeichnis
$ python3 -m venv venv
```

Dieser Befehl führt das Python-Modul `venv` aus und übergibt dem Befehl einen
Namen für den Ordner, in dem das Virtuelle Environment gespeichert werden soll.
Dieser heißt hier `venv`. Soll der Ordner anders heißen (bspw.
"mein_environment"), so wäre der Befehl der nachfolgende. Dieser müsste dann in
den Befehlen in den nächsten Abschnitten angepasst werden, weshalb eine
Änderung des Ordner-Namens nicht empfohlen wird.

```bash
$ python3 -m venv mein_environment
```

**Environment aktivieren:**

````{dropdown} _Windows (CMD)_

```cmd
$ venv\Scripts\activate
```

````

````{dropdown} _Windows (PowerShell)_

```powershell
venv\Scripts\Activate.ps1
```
````

````{dropdown} _Linux/macOS_

```bash
source venv/bin/activate
```

````

**Pakete installieren:**

Stellen Sie sicher, dass das Virtuelle Environment des Kurses aktiviert ist.
Dann installieren Sie die Python-Pakete, die für den Kurs benötigt werden mit
dem Nachfolgenden Befehl.

```bash
$ pip install -r requirements.txt
```

Erhalten Sie den Fehler, dass `pip` nicht verfügbar ist, kann das daran liegen,
dass Ihr Virtuelles Environment nicht aktiviert ist. Ist es aktiviert können
Sie auch den folgenden Befehl ausprobieren:

```bash
$ python3 -m pip install -r requirements.txt
```

**Environment deaktivieren:**

```bash
deactivate
```

Detaillierte Informationen finden Sie in der [offiziellen
`venv`-Dokumentation](https://docs.python.org/3/library/venv.html).

### Option B: conda (Anaconda)

Conda bietet erweiterte Paketverwaltung und kann auch nicht-Python-Pakete
installieren. Dies kann die Installation von bestimmten Paketen bspw. für
Machine Learning erleichtern. Wir benötigen diese Funktionalität nicht für den
vorliegenden Kurs.

**Environment erstellen:**

```bash
# Neues Environment mit Python 3.13 erstellen
$ conda create -n selbstlernkurs-python python=3.13
$ conda activate selbstlernkurs-python

$ pip install -r requirements.txt
```

Wir benutzen hier auch bei der Nutzung von `conda` das Programm `pip` zur
Installation der Pakete.

**Environment verwalten:**

```bash
# Verfügbare Environments anzeigen
conda env list

# Environment aktivieren
conda activate selbstlernkurs-python

# Environment deaktivieren
conda deactivate

# Environment löschen (falls nötig)
conda env remove -n selbstlernkurs-python
```

Weitere Informationen in der [offiziellen
`conda`-Dokumentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## Test des Setups

Nach der Installation und Einrichtung sollten Sie Ihr Setup testen, um
sicherzustellen, dass alles korrekt funktioniert.

### Grundlegende Python-Installation testen

1. **Python-Version überprüfen:**

    ```bash
    $ python3 --version
    Python 3.13.7
    ```

    Sollte Python 3.11 oder höher anzeigen. Die bei Ihnen installierte
    Python-Version kann von der hier gezeigten abweichen.

2. **Verfügbarkeit des Pakets `jupyter` testen:**

    ```bash
    $ python3 -c "import jupyter; print('Jupyter verfügbar')"
    ```

### JupyterLab starten

Wir benutzen JupyterLab als Oberfläche für die Arbeit mit Code im Kurs. Führen
Sie den nachfolgenden Befehl in einem Terminal aus. Dies startet einen Jupyter
Server und öffnet Ihren Webbrowser mit einem neuen Tab in dem Sie die
Jupyter-Lab-Oberfläche sehen.

```bash
jupyter lab
```

## Fehlerbehebung

**Häufige Probleme:**

- **"Python not found":** Stellen Sie sicher, dass Python zum PATH hinzugefügt wurde
- **"Module not found":** Aktivieren Sie Ihr virtuelles Environment vor der Installation
- **Jupyter startet nicht:** Überprüfen Sie, ob Jupyter in Ihrem Environment installiert ist

**Weitere Hilfe:**

- [Python FAQ](https://docs.python.org/3/faq/)
- [Anaconda Troubleshooting](https://docs.anaconda.com/anaconda/user-guide/troubleshooting/)
- [Git FAQ](https://git-scm.com/docs/gitfaq)
