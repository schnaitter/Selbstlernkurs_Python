---
short_title: Installation und Konfiguration
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Installation und Konfiguration

## Git installieren

Bevor Sie Git nutzen können, müssen Sie es auf Ihrem Computer installieren.
Möglicherweise ist Git bereits installiert – das prüfen wir gleich.

### Installation überprüfen

Öffnen Sie ein Terminal (siehe Kapitel
[Exkurs: Unix](../030-Exkurs_Unix/000-Einleitung.md)) und geben Sie ein:

```bash
git --version
```

Wenn Git installiert ist, sehen Sie eine Ausgabe wie:

```
git version 2.39.2
```

Die genaue Versionsnummer kann variieren – wichtig ist nur, dass Git gefunden
wurde.

### Git installieren (falls noch nicht vorhanden)

Falls Sie eine Fehlermeldung erhalten, installieren Sie Git nach:

- **macOS**: `xcode-select --install` (oder `brew install git`)
- **Windows**: Installer von [git-scm.com/download/win](https://git-scm.com/download/win)
  ausführen – enthält auch "Git Bash", ein Terminal mit Unix-Befehlen
- **Linux**: über die Paketverwaltung, z.B. `sudo apt-get install git`
  (Ubuntu/Debian) oder `sudo dnf install git` (Fedora)

## Git konfigurieren

Nach der Installation müssen Sie Git einmalig konfigurieren. Git speichert bei
jedem {term}`Commit` (= gespeicherte Version) Ihren Namen und Ihre E-Mail-Adresse. Das
ist wichtig für die Nachvollziehbarkeit, besonders bei Zusammenarbeit.

### Grundkonfiguration: Name und E-Mail

```bash
git config --global user.name "Erika Mustermann"
git config --global user.email "erika.mustermann@example.com"
```

:::::{margin}
**Hinweis**: Das `--global`-Flag bedeutet, dass diese Einstellung für alle
Git-Repositories auf Ihrem Computer (genauer: Ihres Accounts) gilt. Sie müssen
dies nur einmal tun.
:::::

### Konfiguration überprüfen

```bash
git config --list
```

Oder nur Name und E-Mail anzeigen:

```bash
git config user.name
git config user.email
```

### Weitere nützliche Einstellungen

**Standard-Texteditor** (wird z.B. für Commit-Nachrichten geöffnet):

```bash
# Visual Studio Code
git config --global core.editor "code --wait"

# Nano (einfacher Terminal-Editor)
git config --global core.editor "nano"
```

**Standard-{term}`Branch`-Name** (neuere Git-Versionen verwenden `main`):

```bash
git config --global init.defaultBranch main
```

**Farbige Ausgabe** aktivieren:

```bash
git config --global color.ui auto
```

:::::{admonition} Standard-Editor
:class: tip
Falls Sie keinen Editor festlegen, verwendet Git den Standard-Editor Ihres
Systems (häufig Vim oder Nano). Vim kann für Anfänger\*innen verwirrend sein –
wenn Sie sich unsicher sind, empfehlen wir Nano oder VS Code.
:::::

## Konfigurationsdatei (Überblick)

Alle globalen Einstellungen werden in einer Datei gespeichert:

- **Linux/macOS**: `~/.gitconfig`
- **Windows**: `C:\Users\IhrName\.gitconfig`

Sie können diese Datei auch direkt mit einem Texteditor bearbeiten. Sie sollte
etwa so aussehen:

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

:::::{admonition} Bereit für den nächsten Schritt
:class: success
Git ist jetzt installiert und konfiguriert. Im nächsten Kapitel lernen Sie die
grundlegenden Konzepte kennen, die Git zugrunde liegen.
:::::
