---
numbering:
    heading_1: true
    heading_2: true
    title: true
    figure:
        template: Abb. %s
---

# Jupyter Hub der Humboldt-Universität Berlin

Der Jupyter Hub der HU ermöglicht Ihnen den Zugang über Ihren HU-Account. Ihre Dateien und Änderungen werden aktuell gespeichert, jedoch können sie jeweils am Ende des Semesters gelöscht werden. Laden Sie daher Dateien, die Sie längerfristig behalten wollen, herunter.

## Zugang zum Jupyter Hub

### URL und Anmeldung

- **URL:** <https://jupyterhub.cms.hu-berlin.de>
- **Anmeldung:** Mit HU-Account (Benutzername und Passwort)
- **Zugang:** Sowohl innerhalb des HU-Netzwerks als auch über VPN möglich

```{figure} ../assets/010/Jupyter_Hub_Login.png
:name: fig:hub_login
:centered:
:width: 80%

Login zum Jupyter Hub der HU Berlin
```

## Verfügbare Umgebungen (Profile)

Der Jupyter Hub bietet sechs verschiedene Jupyter-Lab-Umgebungen:

1. **Python** - Standard Python-Umgebung für allgemeine Programmierung
2. **Spark** - Für Big Data-Verarbeitung mit Apache Spark
3. **R** - Für statistische Analysen und Data Science mit R
4. **TensorFlow** - Für Machine Learning und Deep Learning
5. **Natural Language Processing** - Speziell für NLP-Aufgaben
6. **CUDA** - Umgebung mit GPU-Unterstützung für rechenintensive Aufgaben

```{figure} ../assets/010/Jupyter_Hub_Profile.png
:name: fig:hub_profiles
:centered:
:width: 80%

Profile des Jupyter Hubs. Wir nutzen für diesen Kurs das Profil "Datascience Jupyterlab"
```

## Login

### 1. Anmeldung und Profilauswahl

1. Öffnen Sie https://jupyterhub.cms.hu-berlin.de in Ihrem Browser
2. Melden Sie sich mit Ihren HU-Zugangsdaten an
3. Wählen Sie das erste Profil

```{figure} ../assets/010/Jupyter_Hub_Jupyter_Lab.png
:name: fig:hub_lab_startpage
:centered:
:width: 80%

Startansicht der Jupyter-Lab-Oberfläche. In diesem Screenshot sind mehr Ordner zu sehen als bei Ihnen beim ersten Start.
```

### 2. Arbeiten mit Jupyter Notebooks

- Erstellen Sie neue Notebooks über den Launcher
- Verwenden Sie den Datei-Explorer zur Navigation
- Nutzen Sie die verfügbaren Kernels entsprechend Ihrem gewählten Profil

**TODO:** Screenshot eines geöffneten Jupyter Notebooks einfügen - zeigt eine Zelle mit Code und deren Ausgabe

## Download der Inhalte

```{caution} Datenbeständigkeit

- **Semesterende:** Daten werden nach jedem Semester gelöscht
- **Inaktivität:** Daten werden nach einem Jahr ohne Login gelöscht
- **Backup:** Laden Sie wichtige Daten regelmäßig auf Ihre lokale Festplatte herunter

```

Daher empfehlen wir:

1. Arbeiten Sie direkt im Jupyter Hub
2. Laden Sie fertige Notebooks und Dateien regelmäßig herunter
3. Optional: Verwenden Sie Git-Integration für Versionskontrolle

**TODO:** Screenshot des Download-Prozesses einfügen - zeigt, wie Dateien über den Datei-Explorer heruntergeladen werden (Rechtsklick → Download)

## Test des Setups

1. Melden Sie sich am Jupyter Hub an
2. Wählen Sie das Python-Profil
3. Erstellen Sie ein neues Notebook
4. Führen Sie eine einfache Python-Zelle aus:
    ```python
    print("Hello World!")
    import sys
    print(f"Python Version: {sys.version}")
    ```

## Weiterführende Ressourcen

### Offizielle Dokumentation

- [Digitale Lehre HU Berlin - JupyterHub](https://www.digitale-lehre.hu-berlin.de/de/lehr-und-lernlandschaft/jupyterhub)
- [AI at HU Berlin - JupyterHub in Teaching](https://ki.cms.hu-berlin.de/en/more-about-llm-hpc-jh/jupyterhub/jupyterhub-in-teaching)

### Blog-Beiträge

- [CMS Blog: JupyterHub – Coding lernen mit Jupyter Notebooks](https://blogs.hu-berlin.de/cms/2024/08/28/jupyterhub-coding-lernen-mit-jupyter-notebooks/)
- [CMS Blog: Infrastruktur und Service](https://blogs.hu-berlin.de/cms/2022/06/30/infrastruktur-und-service-hu-cloud-jupyter-hub-und-kuenstliche-intelligenz-in-der-lehre/)

**TODO:** Überprüfen Sie regelmäßig die offiziellen Blogs für Updates und neue Features.

_Letzte Aktualisierung: Oktober 2025 - Stand: Pilotbetrieb_

**TODO:** Aktualisieren Sie dieses Dokument, wenn der JupyterHub aus dem Pilotbetrieb in den regulären Betrieb übergeht.
