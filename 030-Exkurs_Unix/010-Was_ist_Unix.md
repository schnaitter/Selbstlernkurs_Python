---
short_title: Was ist Unix?
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Was ist Unix?

{term}`Unix` ist ein Betriebssystem, das 1969 bei AT&T Bell Labs entwickelt wurde.
Heute basieren viele moderne Betriebssysteme auf Unix-Prinzipien:

- **Linux** (Ubuntu, Debian, Fedora, etc.)
- **macOS** (basiert auf BSD Unix)
- **BSD-Varianten** (FreeBSD, OpenBSD)

Auch wenn Windows kein Unix-System ist, bietet es mit WSL (Windows Subsystem
for Linux) und Git Bash Unix-ähnliche Umgebungen.

## Die Unix-Philosophie

:::::{margin}
::::{seealso} Unix-Philosophie

Die Unix-Philosophie hat die moderne Softwareentwicklung stark geprägt. Viele
erfolgreiche Tools und Programmiersprachen (inklusive {term}`Python`) folgen diesen
Prinzipien.

::::
:::::

Unix folgt einfachen, aber mächtigen Grundprinzipien:

1. **Ein Programm soll eine Aufgabe gut erfüllen**
   Statt großer, komplexer Programme gibt es viele kleine, spezialisierte
   Tools.

2. **Programme sollen zusammenarbeiten**
   Die Ausgabe eines Programms kann als Eingabe für ein anderes dienen (Pipes).

3. **Alles ist eine Datei**
   Dateien, Verzeichnisse, Geräte – alles wird über das Dateisystem
   angesprochen.

4. **Textbasierte Schnittstellen**
   Text ist universell lesbar und verarbeitbar. Daher nutzen Unix-Programme oft
   Textein- und -ausgabe.

## Warum ist Unix relevant für Python-Entwicklung?

:::::{margin}
::::{hint} JupyterHub

Auf JupyterHub arbeiten Sie bereits auf einem Unix-System (Linux). Alle
Befehle, die Sie in diesem Exkurs lernen, funktionieren dort direkt.

::::
:::::

Wenn Sie Python-Programme entwickeln, werden Sie häufig mit Unix-Systemen
arbeiten:

- {term}`JupyterHub` läuft auf einem Linux-Server
- Viele **Web-Server und Cloud-Dienste** nutzen Linux
- **Python-Pakete installieren** und **virtuelle Umgebungen** verwalten erfolgt
  oft über das Terminal
- **Ausführbare Python-Skripte** basieren auf Unix-Konzepten (Shebang,
  Dateirechte)
- {term}`Git` und viele Entwicklungstools sind für Unix optimiert

## Unix-Zugang unter verschiedenen Betriebssystemen

| Betriebssystem | Unix-Zugang                                                              |
| -------------- | ------------------------------------------------------------------------ |
| **macOS**      | Natives Unix-System. Terminal über {kbd}`Cmd`+{kbd}`Space` → "Terminal"  |
| **Linux**      | Natives Unix-System. Terminal meist über {kbd}`Strg`+{kbd}`Alt`+{kbd}`T` |
| **Windows**    | WSL (Windows Subsystem for Linux) oder Git Bash installieren             |
| **JupyterHub** | Terminal über "File → New → Terminal"                                    |

````{exercise}
:label: unix-uname

Öffnen Sie ein Terminal auf Ihrem System (oder auf JupyterHub) und geben Sie
folgenden Befehl ein:

```console
$ uname
```

Dieser Befehl zeigt den Namen des Betriebssystems an. Auf Linux sehen Sie
`Linux`, auf macOS `Darwin`.
````

````{solution} unix-uname
:class: dropdown

**Auf Linux/JupyterHub:**

```console
$ uname
Linux
```

**Auf macOS:**

```console
$ uname
Darwin
```

**Für mehr Informationen:**

```console
$ uname -a
```

Dies zeigt detaillierte Systeminformationen (Kernelversion,
Prozessorarchitektur, etc.).
````
