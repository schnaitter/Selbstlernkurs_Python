---
numbering:
    heading_1: true
    heading_2: true
    title: true
    figure:
        template: Abb. %s
jupyter:
    jupytext:
        text_representation:
            extension: .md
            format_name: markdown
            format_version: "1.3"
            jupytext_version: 1.17.3
    kernelspec:
        display_name: Selbstlernkurs_Python
        language: python
        name: python3
---

# Die Read-Eval-Print-Loop (REPL)

Im Kapitel zur Installation haben Sie einmal `python3 --version` im Terminal
ausgeführt um sicherzustellen, dass Sie ein aktuelles und funktionierendes
Python installiert haben. Nun machen Sie die ersten Schritte mit Python Code.

## Starten der Python REPL

`````{margin}
````{admonition} Wiederholung
:class: seealso
Im gesamten Kurs werden Eingaben im Terminal wie folgt dargestellt:
```console
$ echo "Hallo Welt"
Hallo Welt
```
Dabei beginnen Zeilen mit einem Terminal-Befehl mit `$ ` und darauffolgende Zeilen bis zum nächsten `$ ` die Ausgabe des Befehls. Wenn Sie die Schritte nachvollziehen, geben Sie den Befehl selbst ein und 'starten' diesen mit `<Enter>`.

Achten Sie darauf, dass Sie ggf. Dateipfade anpassen müssen. Mehr dazu im [Exkurs: Unix](/030-Exkurs_Unix/Einleitung.md).
````
`````

Führen Sie das Programm `python3` im Terminal aus, so startet es in die REPL.

```console
$ python3
Python 3.13.7 (main, Aug 14 2025, 11:12:11) [Clang 17.0.0 (clang-1700.0.13.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Um die REPL zu verlassen, tippen Sie `quit()` oder nutzen Sie (in Unix-basierten Betriebssysteme) die Tastekombination `<Strg-D>`.

## Ihr erstes Python

Die REPL verhält sich ähnlich zum Terminal, nur dass nicht Befehle nach (typischerweise) einem `$ ` eingegeben werden, sondern dass Python-Code nach einem `>>> ` eingegeben wird.

Nachfolgend finden Sie ein paar Beispiele. Probieren Sie diese selbst aus und ändern Sie sie dann ab.

```python-repl
>>> 2+2
4
```

```python-repl
>>> "Hallo, Welt!"
'Hallo, Welt!"
```

```python-repl
>>> print("Hallo, Welt!")
Hallo, Welt!
```

Ist der Python-Code noch nicht vollständig, so verändert sich der Prompt zu `... `.

```python-repl
>>> print(
...
... "Hallo"
... )
Hallo
```

## Die Struktur einer REPL

Eine REPL ist ein Programm, welches:

1. _**R**ead_: Einen Befehl oder hier ein Stück Python-Code einliest.
2. _**E**val_: Dann den Code ausführt.
3. _**P**rint_: Das Ergebnis des ausgeführten Codes zurück gibt.
4. _**L**oop_: Und das solange wiederholt, bis es beendet wird (bei Python via `quit()`).

```{code-cell}
:tags: [remove-cell]
from jupyterquiz import display_quiz
c = { '--jq-multiple-choice-bg': '#202080',
      '--jq-mc-button-bg': '#fafafa',
      '--jq-mc-button-border': '#e0e0e0e0',
      '--jq-mc-button-inset-shadow': '#555555',
      '--jq-many-choice-bg': '#202080',
      '--jq-numeric-bg': '#202080',
      '--jq-numeric-input-bg': '#c0c0c0',
      '--jq-numeric-input-label': '#101010',
      '--jq-numeric-input-shadow': '#999999',
      '--jq-string-bg': '#202080',
      '--jq-incorrect-color': '#c80202',
      '--jq-correct-color': '#009113',
      '--jq-text-color': '#fafafa',
      '--jq-link-color': '#9abafa' }
```

TODO: Abbildung REPL

TODO: genauere Erklärung des Ablaufs von bspw. `print("Hallo")`.

## Lernstandskontrolle

```{code-cell}
:tags: [remove-input]
q = [{
        "question": "Welche Ausgabe erhalten Sie, wenn Sie <pre>>>> 3**3</pre> in die REPL eingeben?",
        "type": "multiple_choice",
        "answers": [
            { "code": "3**3", "correct": False },
            { "code": "9", "correct": True },
            { "code": "6", "correct": False },
            { "code": "33", "correct": False },
            { "code": "333", "correct": False },
            { "code": "SyntaxError", "correct": False }
        ]
    },
    {
        "question": "Wie können Sie eine Kommazahl in Python eingeben?<br>Probieren Sie auch die falschen Optionen aus. Was ist deren Ergebnis?",
        "type": "multiple_choice",
        "answers": [
            { "code": "12,34", "correct": False },
            { "code": "12.34", "correct": True },
            { "code": "1234e-2", "correct": True },
            { "code": "123,4e-1", "correct": False },
        ]
    },
    {
        "question": "Welche Ausgabe ergibt die folgende Eingabe in die REPL? Geben die Ausgabe bis zum ersten Leerzeichen ein.<pre>>>> test</pre>",
        "type": "string",
        "answers": [
            { "answer": "NameError:", "correct": True,
              "match_case": False, "fuzzy_threshold": 0.9,
              "feedback": "Korrekt. Wie in der Fehlermeldung angegeben ist die Variable `test` nicht definiert, weshalb Sie deren Wert nicht auslesen können."},
        ]
    }]
display_quiz(q, colors=c)
```
