---
short_title: Terminal & Shell
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Terminal und Shell

Die Begriffe "Terminal" und "Shell" werden oft synonym verwendet, bezeichnen
aber unterschiedliche Dinge.

## Terminal vs. Shell

:::::{margin}
::::{note} Historisch

Früher waren Terminals physische Geräte (Bildschirm + Tastatur), die mit einem
zentralen Computer verbunden waren. Heute nutzen wir **Terminal-Emulatoren** –
Programme, die das Verhalten dieser alten Terminals nachahmen.

::::
:::::

| Begriff      | Beschreibung                                                                       | Beispiele                                                      |
| ------------ | ---------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Terminal** | Das Fenster, das Sie sehen. Zeigt Text an und nimmt Tastatureingaben entgegen.     | Terminal.app (macOS), GNOME Terminal (Linux), Windows Terminal |
| **Shell**    | Das Programm, das im Terminal läuft. Interpretiert Ihre Befehle und führt sie aus. | bash, zsh, fish                                                |

**Analogie:** Das Terminal ist wie ein Telefonhörer – die Shell ist das
Gespräch, das Sie führen.

## Welche Shell nutze ich?

Die am häufigsten genutzten Shells sind:

- **bash** (Bourne Again Shell) – Standard auf vielen Linux-Systemen und
  JupyterHub
- **zsh** (Z Shell) – Standard auf macOS seit 2019
- **fish** (Friendly Interactive Shell) – moderne Alternative mit vielen
  Komfortfunktionen

Für diesen Kurs ist es egal, welche Shell Sie nutzen. Die grundlegenden Befehle
funktionieren überall gleich.

Um herauszufinden, welche Shell Sie nutzen:

```console
$ echo $SHELL
/bin/bash
```

Oder für detailliertere Informationen:

```console
$ echo $0
bash
```

## Terminal öffnen

:::::{margin}
::::{hint} JupyterHub

Im JupyterLab von JupyterHub öffnen Sie ein Terminal über das Menü: **File →
New → Terminal**

Das Terminal öffnet sich in einem neuen Tab.

::::
:::::

::::{tab-set}

:::{tab-item} macOS

- {kbd}`Cmd`+{kbd}`Space` → "Terminal" eingeben → {kbd}`Enter`
- Oder: Programme → Dienstprogramme → Terminal

:::

:::{tab-item} Linux

- {kbd}`Strg`+{kbd}`Alt`+{kbd}`T`
- Oder: Menü → Terminal

:::

:::{tab-item} Windows

- **WSL:** "wsl" im Startmenü suchen
- **Git Bash:** Nach Installation von Git for Windows verfügbar
- **PowerShell:** Unterstützt manche Unix-Befehle, aber nicht alle

:::

::::

## Der Prompt

:::::{margin}
::::{seealso} Prompt-Anpassung

Der Prompt lässt sich anpassen. Viele Entwickler\*innen nutzen Tools wie
[Starship](https://starship.rs/) oder [Oh My Zsh](https://ohmyz.sh/) für
informativere, bunte Prompts.

::::
:::::

Wenn Sie ein Terminal öffnen, sehen Sie den **Prompt** – eine Zeile, die
anzeigt, dass die Shell bereit für Eingaben ist:

```console
user@hostname:~$
```

Der Prompt kann unterschiedlich aussehen:

- `$ ` für normale Nutzer\*innen
- `# ` für Administrator\*innen (root)
- Oft werden Nutzername, Hostname und aktuelles Verzeichnis angezeigt

In diesem Kurs stellen wir den Prompt vereinfacht als `$ ` dar:

```console
$ befehl
Ausgabe des Befehls
```

Zeilen mit `$ ` sind Befehle, die Sie eingeben (ohne das `$ `). Zeilen ohne `$
` sind die Ausgabe des Befehls.

## Grundlegende Navigation

Probieren Sie diese Befehle aus:

```console
$ whoami
```

Zeigt Ihren Nutzernamen an.

```console
$ hostname
```

Zeigt den Namen des Computers an (auf JupyterHub sehen Sie den Servernamen).

```console
$ date
```

Zeigt das aktuelle Datum und die Uhrzeit an.

## Befehlshistorie

:::::{margin}
::::{hint} Nützliche Tastenkombinationen

- {kbd}`Strg`+{kbd}`L`: Terminal leeren (wie `clear`)
- {kbd}`Strg`+{kbd}`C`: Laufenden Befehl abbrechen
- {kbd}`Strg`+{kbd}`D`: Terminal schließen (wie `exit`)
- {kbd}`Tab`: Automatische Vervollständigung

Unter Mac nutzen Sie statt {kbd}`Strg` die Taste {kbd}`Ctrl`.

::::
:::::

Die Shell speichert eine Historie Ihrer Befehle:

- {kbd}`↑` (Pfeil hoch): Vorheriger Befehl
- {kbd}`↓` (Pfeil runter): Nächster Befehl
- `history`: Zeigt alle bisherigen Befehle

Das ist besonders praktisch, wenn Sie einen längeren Befehl wiederholen oder
leicht anpassen möchten.

## Tab-Vervollständigung

Ein extrem nützliches Feature: Drücken Sie {kbd}`Tab` während Sie einen Befehl
oder Dateinamen eingeben.

```console
$ dat[Tab]
$ date
```

Die Shell vervollständigt automatisch. Gibt es mehrere Möglichkeiten, zeigt
zweimaliges Drücken von {kbd}`Tab` alle Optionen an.

:::::{admonition} 💪 Übung
:icon: false

Probieren Sie folgende Dinge aus:

1. Öffnen Sie ein Terminal
2. Geben Sie `whoami` ein und drücken Sie {kbd}`Enter`
3. Drücken Sie {kbd}`↑` um den letzten Befehl wiederzuholen
4. Geben Sie `dat` ein und drücken Sie {kbd}`Tab` – was passiert?
5. Geben Sie `echo Hallo Welt` ein
6. Tippen Sie `history` um Ihre Befehlshistorie zu sehen

:::{dropdown} ✅ Erwartete Ergebnisse

```console
$ whoami
ihr_nutzername
$ whoami
ihr_nutzername
$ date
Fr 17. Okt 2025 14:30:25 CEST
$ echo Hallo Welt
Hallo Welt
$ history
    1  whoami
    2  whoami
    3  date
    4  echo Hallo Welt
    5  history
```

Die tatsächliche Ausgabe kann je nach System variieren.

:::
:::::
