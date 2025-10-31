---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Installation und Konfiguration

## Git installieren

Bevor Sie Git nutzen können, müssen Sie es auf Ihrem Computer installieren. Möglicherweise ist Git bereits installiert – das prüfen wir gleich.

### Installation überprüfen

Öffnen Sie ein Terminal (siehe Kapitel [Exkurs: Unix](../030-Exkurs_Unix/Einleitung.md)) und geben Sie ein:

```bash
git --version
```

Wenn Git installiert ist, sehen Sie eine Ausgabe wie:

```
git version 2.39.2
```

Die genaue Versionsnummer kann variieren – wichtig ist nur, dass Git gefunden wurde.

### Git installieren (falls noch nicht vorhanden)

Falls Sie eine Fehlermeldung erhalten, müssen Sie Git noch installieren:

::::{tab-set}

:::{tab-item} macOS
Git ist Teil der Xcode Command Line Tools. Geben Sie im Terminal ein:

```bash
xcode-select --install
```

Alternativ können Sie Git mit [Homebrew](https://brew.sh) installieren:

```bash
brew install git
```
:::

:::{tab-item} Windows
Laden Sie Git von der offiziellen Website herunter:
[https://git-scm.com/download/win](https://git-scm.com/download/win)

Führen Sie das Installationsprogramm aus und verwenden Sie die Standard-Einstellungen.

**Tipp**: Bei der Installation wird auch "Git Bash" installiert – ein Terminal für Windows, das Unix-Befehle versteht.
:::

:::{tab-item} Linux
Git ist in den Paketquellen der meisten Distributionen enthalten:

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install git
```

**Fedora:**
```bash
sudo dnf install git
```

**Arch Linux:**
```bash
sudo pacman -S git
```
:::

::::

Weitere Installationsanleitungen finden Sie im Kapitel [Installation und Technik](../010-Installation_Technik/Einleitung.md).

## Git konfigurieren

Nach der Installation müssen Sie Git einmalig konfigurieren. Git speichert bei jedem Commit (=gespeicherte Version) Ihren Namen und Ihre E-Mail-Adresse. Das ist wichtig für die Nachvollziehbarkeit, besonders bei Zusammenarbeit.

### Grundkonfiguration: Name und E-Mail

Öffnen Sie ein Terminal und geben Sie folgende Befehle ein (ersetzen Sie die Beispieldaten durch Ihre eigenen):

```bash
git config --global user.name "Erika Mustermann"
git config --global user.email "erika.mustermann@example.com"
```

:::::{margin}
**Hinweis**: Das `--global`-Flag bedeutet, dass diese Einstellung für alle Git-Repositories auf Ihrem Computer gilt. Sie müssen dies nur einmal tun.
:::::

### Konfiguration überprüfen

Um zu sehen, welche Einstellungen aktuell gespeichert sind:

```bash
git config --list
```

Oder nur Name und E-Mail anzeigen:

```bash
git config user.name
git config user.email
```

### Optional: Standard-Texteditor festlegen

Git öffnet manchmal einen Texteditor, z.B. für Commit-Nachrichten. Sie können festlegen, welcher Editor verwendet werden soll:

```bash
# Visual Studio Code
git config --global core.editor "code --wait"

# Nano (einfacher Terminal-Editor)
git config --global core.editor "nano"

# Vim (fortgeschrittener Terminal-Editor)
git config --global core.editor "vim"
```

:::::{admonition} Standard-Editor
:class: tip
Falls Sie keinen Editor festlegen, verwendet Git den Standard-Editor Ihres Systems (häufig Vim oder Nano). Vim kann für Anfänger\*innen verwirrend sein – wenn Sie sich unsicher sind, empfehlen wir Nano oder VS Code.
:::::

### Optional: Standard-Branch-Name

Neuere Git-Versionen verwenden `main` als Standard-Name für den Haupt-Branch. Ältere Versionen nutzen `master`. Um Konsistenz zu gewährleisten:

```bash
git config --global init.defaultBranch main
```

### Optional: Farben aktivieren

Git kann Ausgaben farblich hervorheben (z.B. Änderungen in grün/rot):

```bash
git config --global color.ui auto
```

## Konfigurationsdatei

Alle globalen Einstellungen werden in einer Datei gespeichert:
- **Linux/macOS**: `~/.gitconfig`
- **Windows**: `C:\Users\IhrName\.gitconfig`

Sie können diese Datei auch direkt mit einem Texteditor bearbeiten. Sie sollte etwa so aussehen:

```ini
[user]
    name = Erika Mustermann
    email = erika.mustermann@example.com
[core]
    editor = nano
[init]
    defaultBranch = main
[color]
    ui = auto
```

## Zusammenfassung

Nach diesen Schritten ist Git einsatzbereit! Die wichtigsten Befehle waren:

```bash
# Git-Version prüfen
git --version

# Name und E-Mail konfigurieren (erforderlich)
git config --global user.name "Ihr Name"
git config --global user.email "ihre.email@example.com"

# Konfiguration anzeigen
git config --list
```

:::::{admonition} Bereit für den nächsten Schritt
:class: success
Git ist jetzt installiert und konfiguriert. Im nächsten Kapitel lernen Sie die grundlegenden Konzepte kennen, die Git zugrunde liegen.
:::::
