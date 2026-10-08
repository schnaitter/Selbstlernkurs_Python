---
short_title: "Projekt: Taschenrechner II"
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Projekt: Taschenrechner II

```{seealso} 🎓 Lernziele
:icon: false

In diesem Kapitel erlernen Sie, …

- … wie Sie Nutzereingaben einlesen und Ergebnisse ausgeben.
- … eine Nutzerinteraktion Schritt für Schritt ausgestalten.
- … fehlertoleranten Code schreiben.

```

```{note} Projektziel

Ziel des Projekts ist es, aufbauend auf dem [Projekt: Taschenrechner
I](../020-Projekt_Taschenrechner_I/000-Einleitung.md) einen interaktiven
Taschenrechner zu entwickeln: Die Nutzer\*in gibt nacheinander
einen Operator und beliebig viele Operanden ein und erhält dann das jeweilige
Berechnungsergebnis ausgegeben. Das Programm ist damit ebenfalls eine
[REPL](https://de.wikipedia.org/wiki/Read-Eval-Print-Loop).

```

Im [Projekt: Taschenrechner I](../020-Projekt_Taschenrechner_I/000-Einleitung.md)
haben Sie die Grundlagen gelegt: mathematische Operationen, Kontrollstrukturen
und Funktionen, das Speichern von Code in Dateien und das Ausführen von
Skripten. In diesem Kapitel bauen Sie darauf auf und entwickeln den
Taschenrechner Schritt für Schritt weiter.

**Kapitelinhalt:**

1. [Projekt: Taschenrechner II](./010-Taschenrechner.ipynb) – die genaue
   Beschreibung der Interaktion und des gewünschten Programmablaufs.
2. [Nutzereingaben](./020-Nutzerinneneingabe.ipynb) – wie Sie mit `input()`
   Werte von der Nutzer\*in einlesen und Ergebnisse ausgeben.
3. [Schleifen](./030-Schleifen.ipynb) – wie Sie Code mit `while`- und
   `for`-Schleifen wiederholen.
4. [Implementierung des Taschenrechners](./040-Implementierung.ipynb) – die
   schrittweise Umsetzung des Skripts `taschenrechner.py`.
5. [Aufgabe: Erweiterung des Taschenrechners](./050-Aufgabe_Erweiterung.md) –
   eine Aufgabe zur Erweiterung des Taschenrechners um weitere Operatoren und
   zur Fehlertoleranz.

```{seealso} Vorwissen
:icon: false

Dieses Kapitel setzt das [Projekt: Taschenrechner
I](../020-Projekt_Taschenrechner_I/000-Einleitung.md) voraus. Dort haben Sie
gelernt, mit Zahlen zu rechnen, den Programmfluss mit
[Kontrollstrukturen](../020-Projekt_Taschenrechner_I/025-Kontrollstrukturen.ipynb)
zu steuern, Code in `.py`-Dateien zu speichern, einfache
Funktionen zu schreiben und [ausführbare
Skripte](../020-Projekt_Taschenrechner_I/050-Ausführbare_Skripte.md) zu
erstellen. Falls Ihnen diese Grundlagen fehlen, arbeiten Sie das Projekt
Taschenrechner I zuerst durch.

```

```{seealso} 📚 Weiterführende Ressourcen
:icon: false

- **Offizielle Dokumentation:** [`input()` — Built-in Functions](https://docs.python.org/3/library/functions.html#input)
- **Offizielle Dokumentation:** [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) im Python-Tutorial
- **Buch (kostenlos):** Allen B. Downey, [*Think Python*](https://greenteapress.com/wp/think-python-2e/)
- **Bibliotheksspezifische OER:** [Library Carpentry: Introduction to Python](https://librarycarpentry.org/lc-python-intro/)

```
