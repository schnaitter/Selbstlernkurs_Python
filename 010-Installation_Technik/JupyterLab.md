---
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Die JupyterLab-Oberfläche

## Überblick über JupyterLab

JupyterLab ist die nächste Generation der webbasierten Entwicklungsumgebung für das Jupyter-Projekt. Es bietet eine flexible und erweiterbare Oberfläche für interaktive Datenanalyse und wissenschaftliches Rechnen.

```{figure} ../assets/010/JupyterLab_Parts.png
:name: fig:lab_parts
:centered:
:width: 100%

Bestandteile der Jupyter-Lab-Oberfläche: ①  Menüleiste, ②  Seitenleiste, ③
Arbeitsbereich, ④  rechte Seitenleiste. Hier sind im Arbeitsbereich ein Editor
und ein Terminal übereinander angeordnet. In der rechten Seitenleiste ist der
Debugger geöffnet.

```

## Die Hauptkomponenten der Oberfläche

### 1. Menüleiste

Die obere Menüleiste enthält alle wichtigen Funktionen:

- **File**: Dateioperationen (Neu, Öffnen, Speichern, Export)
- **Edit**: Bearbeitung (Rückgängig, Kopieren, Einfügen)
- **View**: Ansichtsoptionen und Layout-Einstellungen
- **Run**: Ausführung von Code-Zellen
- **Kernel**: Kernel-Management (Neustart, Wechsel)
- **Git**: Git-Integration
- **Tabs**: Tab-Verwaltung
- **Settings**: Einstellungen und Konfiguration
- **Help**: Hilfe und Dokumentation

> **Screenshot benötigt:** Detailansicht der Menüleiste mit aufgeklapptem "Run"-Menü

### 2. Linke Seitenleiste

Die linke Seitenleiste bietet schnellen Zugriff auf wichtige Tools:

- **Datei-Browser** (📁): Navigation durch das Dateisystem
- **Laufende Kernels/Terminals** (⚡): Übersicht aktiver Prozesse
- **Befehlspalette** (🔍): Schneller Zugriff auf alle Befehle
- **Inhaltsverzeichnis** (📋): Navigation in Notebooks
- **Erweiterungs-Manager** (🧩): Installation und Verwaltung von Extensions

> **Screenshot benötigt:** Linke Seitenleiste mit geöffnetem Datei-Browser, der typische Python-Projektstruktur zeigt

### 3. Arbeitsbereich (Main Work Area)

Der zentrale Arbeitsbereich ist das Herzstück von JupyterLab:

- **Flexible Tab-Anordnung**: Mehrere Dokumente gleichzeitig öffnen
- **Geteilte Ansichten**: Fenster durch Ziehen von Tabs aufteilen
- **Live-Bearbeitung**: Mehrere Ansichten desselben Dokuments

> **Screenshot benötigt:** Arbeitsbereich mit drei geteilten Fenstern: Notebook links, Code-Editor rechts oben, Terminal rechts unten

### 4. Rechte Seitenleiste (optional)

- **Property Inspector**: Eigenschaften des aktuellen Elements
- **Debugger**: Debugging-Tools für Code

## Erste Schritte mit der Oberfläche

### Notebook erstellen und verwenden

1. **Neues Notebook**: File → New → Notebook → Python 3
2. **Code-Zellen**: Eingabe von Python-Code
3. **Markdown-Zellen**: Dokumentation und Erklärungen
4. **Ausführung**: Shift+Enter oder Run-Button

> **Screenshot benötigt:** Neues leeres Notebook mit einer Code-Zelle und einer Markdown-Zelle

### Workspace-Layout anpassen

- **Tabs verschieben**: Ziehen zum Aufteilen der Ansicht
- **Größe ändern**: Ziehen der Trennlinien zwischen Bereichen
- **Seitenleisten**: Ein-/Ausblenden über View-Menü

> **Screenshot benötigt:** Vor/Nach-Vergleich: Standard-Layout vs. angepasstes Layout mit mehreren Fenstern

### Wichtige Tastenkombinationen

- `Ctrl+Shift+C`: Befehlspalette öffnen
- `Shift+Enter`: Zelle ausführen und zur nächsten
- `Ctrl+Enter`: Zelle ausführen ohne Weiterspringen
- `Tab`: Code-Vervollständigung
- `Shift+Tab`: Tooltip/Dokumentation anzeigen

## Dateiformate und Viewer

JupyterLab kann verschiedene Dateiformate direkt anzeigen:

- **Notebooks** (.ipynb): Interaktive Code-Dokumente
- **Text-Dateien** (.py, .txt, .md): Mit Syntax-Highlighting
- **Bilder** (.png, .jpg, .svg): Direkter Viewer
- **Daten** (.csv, .json): Tabellarische Ansicht

> **Screenshot benötigt:** Datei-Browser mit verschiedenen Dateitypen und Preview eines CSV-Files

## Weiterführende Ressourcen

- **Offizielle Dokumentation**: [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- **Interface Guide**: [User Interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html)
- **Getting Started**: [JupyterLab Overview](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)

## Tipps für Einsteiger

1. **Experimentieren Sie**: Die Oberfläche ist flexibel - probieren Sie verschiedene Layouts aus
2. **Shortcuts lernen**: Tastenkombinationen beschleunigen die Arbeit erheblich
3. **Extensions nutzen**: Erweitern Sie JupyterLab um zusätzliche Funktionen
4. **Dokumentation**: Nutzen Sie die eingebaute Hilfe (Help-Menü)

> **Screenshot benötigt:** Help-Menü mit Keyboard Shortcuts und About-Dialog
