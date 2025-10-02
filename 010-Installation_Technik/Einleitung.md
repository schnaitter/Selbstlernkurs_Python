---
numbering:
    heading_1: true
    heading_2: true
    title: true
    figure:
        template: Abb. %s
---

# Installation und technische Voraussetzungen

Um den Kurs zu bearbeiten benötigen Sie eine Python-Installation, einen Code-Editor und idealerweise ein (Unix-)Terminal. Sie können dies entweder lokal bei sich auf dem Computer installieren oder Sie nutzen eine Jupyter-Installation wie [Binder](https://mybinder.org) oder einen lokalen Jupyter Hub.

Binder erstellt jeweils neue Virtuelle Maschinen in denen die Inhalte des Kurses eingerichtet werden und bietet Ihnen dann eine Jupyter-Lab-Oberfläche. Binder speichert jedoch keine Änderungen oder Ergebnisse weshalb Sie diese jeweils selbstständig herunterladen müssen.

Nachfolgend finden Sie Anleitungen für den [Jupyter Hub der Humboldt-Universität zu Berlin](https://jupyterhub.cms.hu-berlin.de) _(nur für HU-Mitglieder)_ sowie für die lokale Installation.

## Jupyter Hub der Humboldt-Universität zu Berlin

### Login

### Download der Inhalte

### Test des Setups

## Lokale Installation

### Installation von Python

````{margin}
```{hint} Python 3 vs. Python 2

Python als Programmiersprache gibt es seit 1989. Während der Entwicklung der Sprache entschieden sich die Entwickler\*innen einen Bruch der Rückwärtskompatibilität in Kauf zu nehmen, um grundlegende Änderungen im inneren der Sprache und des Compilers/Interpreters vorzunehmen. Seit 2008 gibt es daher Python 3 (`python3`). Python 2.7 war die letzte Python 2 Version (früher `python`). Auch wenn Python 2.7 schon sein vielen Jahren nicht mehr offiziell unterstützt wird sind viele Systeme noch so konfiguriert, dass der Befehl `python` den (vermutlich nicht mehr installierten) Python 2 Interpreter ausführt.

Wenn Sie sich nicht sicher sind, wie genau Ihr System konfiguriert ist, nutzen Sie `python3`. Das funktioniert immer.
```
````

Für die lokale Nutzung dieses Kurses benötigen Sie eine Python-Installation. Es gibt zwei empfohlene Wege: die Standard-Python-Installation von Python.org oder die Anaconda-Distribution.

#### Option A: Python.org (Standard-Installation)

Die offizielle Python-Installation eignet sich für die meisten Anwendungsfälle und bietet maximale Flexibilität.

```{dropdown} **Windows**

1. Besuchen Sie die [offizielle Python-Download-Seite](https://www.python.org/downloads/windows/)
2. Laden Sie die neueste Python 3.x Version herunter (empfohlen: Python 3.13 oder 3.14)
3. Folgen Sie der [detaillierten Windows-Installationsanleitung](https://docs.python.org/3/using/windows.html) von Python.org
4. **Wichtig:** Aktivieren Sie "Add Python to PATH" während der Installation
```

```{dropdown} **macOS:**

1. Besuchen Sie die [offizielle Python-Download-Seite](https://www.python.org/downloads/macos/)
2. Laden Sie die neueste Python 3.x Version herunter
3. Folgen Sie der [macOS-Installationsanleitung](https://docs.python.org/3/using/mac.html) von Python.org
4. Alternativ: Installation über [Homebrew](https://brew.sh/): `brew install python`

```

````{dropdown} **Linux**

- **Ubuntu/Debian:** Folgen Sie der [offiziellen Linux-Anleitung](https://docs.python.org/3/using/unix.html)
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

Die bei Ihnen installierte Python-Version kann von der hier gezeigten abweichen. Solange Sie eine relativ moderne Python-Version haben (>= 3.11) können Sie die Inhalte des Kurses problemlos durcharbeiten.

#### Option B: Anaconda Distribution

````{margin}

```{caution} Lizenz von Anaconda

Für die private Nutzung und die Nutzung als Student\*in ist Anaconda für Sie kostenlos. Wollen Sie die Python-Distribution in einem Arbeitskontext nutzen sollten Sie abklären ob Sie eine Lizenz kaufen müssen.
```
````

Anaconda ist besonders für Data Science und wissenschaftliche Anwendungen geeignet und bringt viele nützliche Pakete mit.

**Alle Betriebssysteme:**

1. Besuchen Sie die [offizielle Anaconda-Download-Seite](https://www.anaconda.com/download)
2. Laden Sie die Anaconda-Distribution für Ihr Betriebssystem herunter
3. Folgen Sie der [detaillierten Installationsanleitung](https://docs.anaconda.com/anaconda/install/) von Anaconda
4. Nach der Installation steht Ihnen der [Anaconda Navigator](https://docs.anaconda.com/navigator/) zur Verfügung

**Vorteile von Anaconda:**

- Integrierte wissenschaftliche Pakete (NumPy, Pandas, Matplotlib, etc.)
- Anaconda Navigator für grafische Verwaltung
- Conda Package Manager für einfache Paketverwaltung
- Jupyter Notebook bereits vorinstalliert

**Installation überprüfen:**

```bash
conda --version
python3 --version
```

### Download der Inhalte

Um die Kursinhalte lokal zu nutzen, benötigen Sie Git und müssen das Repository klonen.

#### Git installieren

Git ist ein Versionskontrollsystem, das für das Herunterladen der Kursinhalte benötigt wird.

```{dropdown} **Windows**

1. Besuchen Sie die [offizielle Git-Download-Seite](https://git-scm.com/download/win)
2. Laden Sie Git für Windows herunter
3. Folgen Sie der [detaillierten Windows-Installationsanleitung](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#_installing_on_windows)
4. Git Bash wird mitinstalliert und bietet eine Unix-ähnliche Kommandozeile
```

```{dropdown} **macOS**

1. Git ist oft bereits vorinstalliert. Überprüfen Sie mit: `git --version`
2. Falls nicht installiert: Besuchen Sie die [Git-Download-Seite](https://git-scm.com/download/mac)
3. Alternativ über [Homebrew](https://brew.sh/): `brew install git`
4. Folgen Sie der [macOS-Installationsanleitung](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#_installing_on_macos)
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
git config --global user.name "Ihr Name"
git config --global user.email "ihre.email@example.com"
```

#### Repository klonen

1. Öffnen Sie ein Terminal (Linux/macOS) oder Git Bash (Windows)
2. Navigieren Sie zu dem Verzeichnis, in dem Sie den Kurs speichern möchten
3. Klonen Sie das Repository:

    ```bash
    git clone https://github.com/[REPOSITORY-URL]
    cd Selbstlernkurs_Python
    ```

**Verzeichnisstruktur:**

Nach dem Klonen erhalten Sie folgende Struktur:

- `000-Einleitung/` - Allgemeine Informationen zum Kurs
- `010-Installation_Technik/` - Diese Installationsanleitung
- `020-Python_Grundlagen/` - Grundlagen der Python-Programmierung
- Weitere Kapitel entsprechend dem Kursaufbau

### Einrichten eines Virtuellen Environments

Virtuelle Umgebungen (Virtual Environments) isolieren Python-Projekte voneinander und verhindern Konflikte zwischen verschiedenen Paketen und Versionen.

#### Option A: venv (Standard Python)

Venv ist das standardmäßige Tool für virtuelle Umgebungen in Python und funktioniert mit jeder Python-Installation.

**Virtuelles Environment erstellen:**

```bash
# Im Kurs-Verzeichnis
python3 -m venv venv
```

**Environment aktivieren:**

_Windows (CMD):_

```cmd
venv\Scripts\activate
```

_Windows (PowerShell):_

```powershell
venv\Scripts\Activate.ps1
```

_Linux/macOS:_

```bash
source venv/bin/activate
```

**Pakete installieren:**

```bash
# Basis-Pakete für den Kurs installieren
pip install --upgrade pip
pip install jupyter notebook matplotlib pandas numpy

# Falls eine requirements.txt existiert:
pip install -r requirements.txt
```

**Environment deaktivieren:**

```bash
deactivate
```

Detaillierte Informationen finden Sie in der [offiziellen venv-Dokumentation](https://docs.python.org/3/library/venv.html).

#### Option B: conda (Anaconda)

Conda bietet erweiterte Paketverwaltung und kann auch nicht-Python-Pakete installieren.

**Environment aus environment.yml erstellen (falls vorhanden):**

```bash
conda env create -f environment.yml
conda activate selbstlernkurs-python
```

**Manuelles Environment erstellen:**

```bash
# Neues Environment mit Python 3.13 erstellen
conda create -n selbstlernkurs-python python=3.13
conda activate selbstlernkurs-python

# Pakete installieren
conda install jupyter notebook matplotlib pandas numpy
# oder über conda-forge:
conda install -c conda-forge jupyter notebook matplotlib pandas numpy
```

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

Weitere Informationen in der [offiziellen conda-Dokumentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Test des Setups

Nach der Installation und Einrichtung sollten Sie Ihr Setup testen, um sicherzustellen, dass alles korrekt funktioniert.

#### Grundlegende Python-Installation testen

1. **Python-Version überprüfen:**

    ```bash
    $ python3 --version
    Python 3.13.7
    ```

    Sollte Python 3.11 oder höher anzeigen. Die bei Ihnen installierte Python-Version kann von der hier gezeigten abweichen.

2. **Wichtige Module testen:**

    ```bash
    python3 -c "import sys; print('Python läuft:', sys.version)"
    python3 -c "import jupyter; print('Jupyter verfügbar')"
    python3 -c "import matplotlib; print('Matplotlib verfügbar')"
    python3 -c "import pandas; print('Pandas verfügbar')"
    python3 -c "import numpy; print('NumPy verfügbar')"
    ```

#### Jupyter Notebook starten

1. **Jupyter Notebook starten:**

    ```bash
    jupyter notebook
    ```

    Dies sollte automatisch Ihren Webbrowser öffnen mit der Jupyter-Oberfläche.

2. **Erstes Test-Notebook erstellen:**

    - Klicken Sie auf "New" → "Python 3"
    - Geben Sie folgenden Code ein und führen Sie ihn aus (Shift+Enter):

    ```python
    print("Hallo, Python-Kurs!")

    # Test der wichtigsten Bibliotheken
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    # Einfache Grafik erstellen
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title("Test-Grafik - Setup erfolgreich!")
    plt.show()

    print("✅ Alle Bibliotheken funktionieren!")
    ```

#### Fehlerbehebung

**Häufige Probleme:**

- **"Python not found":** Stellen Sie sicher, dass Python zum PATH hinzugefügt wurde
- **"Module not found":** Aktivieren Sie Ihr virtuelles Environment vor der Installation
- **Jupyter startet nicht:** Überprüfen Sie, ob Jupyter in Ihrem Environment installiert ist

**Weitere Hilfe:**

- [Python FAQ](https://docs.python.org/3/faq/)
- [Anaconda Troubleshooting](https://docs.anaconda.com/anaconda/user-guide/troubleshooting/)
- [Git FAQ](https://git-scm.com/docs/gitfaq)
