---
numbering:
    heading_1: true
    heading_2: true
    title: true
    figure:
        template: Abb. %s
---

# Installation und technische Voraussetzungen

Um den Kurs zu bearbeiten benötigen Sie eine Python-Installation, einen
Code-Editor und idealerweise ein (Unix-)Terminal. Sie können dies entweder
lokal bei sich auf dem Computer installieren oder Sie nutzen eine
Jupyter-Installation wie [Binder](https://mybinder.org) oder einen lokalen
Jupyter Hub.

Binder erstellt jeweils neue Virtuelle Maschinen in denen die Inhalte des
Kurses eingerichtet werden und bietet Ihnen dann eine Jupyter-Lab-Oberfläche.
Binder speichert jedoch keine Änderungen oder Ergebnisse weshalb Sie diese
jeweils selbstständig herunterladen müssen.

Nachfolgend finden Sie Anleitungen für den [Jupyter Hub der
Humboldt-Universität zu Berlin](https://jupyterhub.cms.hu-berlin.de) _(nur für
HU-Mitglieder)_ sowie für die lokale Installation. Dann folgt eine Anleitung für die Jupyter-Lab-Oberfläche, welche wir für die Durchführung des Kurses nutzen werden.

## Warum Python?

````{margin}
```{hint} Python 3 vs. Python 2

Python als Programmiersprache gibt es seit 1989. Während der Entwicklung der
Sprache entschieden sich die Entwickler\*innen einen Bruch der
Rückwärtskompatibilität in Kauf zu nehmen, um grundlegende Änderungen im
Inneren der Sprache und des Compilers/Interpreters vorzunehmen. Seit 2008 gibt
es daher Python 3 (`python3`). Python 2.7 war die letzte Python 2 Version
(früher `python`). Auch wenn Python 2.7 schon sein vielen Jahren nicht mehr
offiziell unterstützt wird sind viele Systeme noch so konfiguriert, dass der
Befehl `python` den (vermutlich nicht mehr installierten) Python 2 Interpreter
ausführt.

Wenn Sie sich nicht sicher sind, wie genau Ihr System konfiguriert ist, nutzen
Sie `python3`. Das funktioniert immer.

```
````

Python ist eine Programmiersprache, welche sich besonders gut für den Einstieg
in die Programmierung eignet. Die Syntax ist klar und verständlich, was es
Anfänger\*innen ermöglicht, sich auf die Konzepte des Programmierens zu
konzentrieren, anstatt sich in komplexer Syntax zu verlieren. Gleichzeitig ist
Python eine vollwertige, professionelle Programmiersprache, die in vielen
Bereichen der Wissenschaft, Datenanalyse und Softwareentwicklung eingesetzt
wird. Durch die große Community und umfangreiche Bibliothekslandschaft können
Sie mit Python sowohl einfache Skripte als auch komplexe Anwendungen
entwickeln.
