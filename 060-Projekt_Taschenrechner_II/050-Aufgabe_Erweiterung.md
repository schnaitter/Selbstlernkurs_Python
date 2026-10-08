---
numbering:
    heading_1: true
    heading_2: true
    title: true
kernelspec:
    name: python3
    display_name: Python 3
    language: python
---

# Aufgabe: Erweiterung des Taschenrechners

```{exercise} Erweiterung des Taschenrechners um zwei Funktionalitäten
:label: taschenrechner-erweiterung

**Funktionalität 1:**

Erweitern Sie den Taschenrechner um Multiplikation (`*`), Subtraktion (`-`) und
Division (`/`).

Dazu müssen Sie:

- überarbeiten, wie Sie die zugelassenen Operatoren überprüfen,
- diese bei der Berechnung jeweils korrekt verarbeiten und
- und die leere Operatoren-Eingabe korrekt behandeln.

:::{hint} Testen ob ein Element `in` einer Liste ist

```python
abc = ["a", "b", "c"]
print("a" in abc) # True
print("d" in abc) # False
```


:::{hint} "Neutrale" Werte bei mathematischen Berechnungen

Für mathematische Operationen gibt es Werte, welche Sie mehrmals in die
Berechnung einbeziehen können, ohne das Ergebnis zu verändern.

Für die Addition ist dies 0:

$$
42 + 0 = 42 \\
0 + 42= 42
$$

Für die Multiplikation ist dies 1:

$$
42 \cdot 1 = 42\\
1 \cdot 42 = 42
$$

Für die Subtraktion ist dies ebenfalls 0, jedoch ist hier die Reihenfolge
relevant:

$$ 42-0 = 42 $$

$$
0-42 \neq 42\\
0 - 42 = -42
$$

Ähnliches gilt für die Division:

$$ 42 \div 1 = 42 = \frac{42}{1} $$

$$
1 \div 42 \neq 42\\
1 \div 42 = \frac{1}{42}
$$

Wenn Sie überprüfen, dass es mindestens zwei Operanden gibt, können Sie
Subtraktion und Division korrekt lösen, indem Sie anfangs Ihr Ergebnis auf den
ersten Wert setzen und dann die restlichen Operanden einbeziehen. Hierzu gibt
es die Funktion `.pop(0)`, welche Ihnen das Element am Index 0 zurückgibt und
dieses dann aus der Liste entfernt.

```python
xs = [1,2,3]
print(xs)
x = xs.pop(0)
print(xs)
print(x)
```

:::

**Funktionalität 2:**

Verbessern Sie die Fehlertoleranz des {term}`Skript`s. Geben Sie der Nutzer\*in
Rückmeldung bei der Nutzung falscher Operatoren und wenn die Eingabe für einen
Operand nicht als Zahl umgewandelt werden kann. Erlauben Sie dann jeweils
weitere Versuche, solange keine leere Eingabe durch die Nutzer\*in erfolgt.

Hierfür müssen Sie die passenden Exceptions "einfangen" und korrekt behandeln.
Dies geht analog zum folgenden Code:

```python
try: # enclose code you think will raise an Exception
    n = int("Hallo")
except ValueError as e: # explicitly catch the ValueError; multiple except-clauses are allowed
    print("Please only enter whole numbers. Try again.")
```

**Weitere Funktionalitäten (freiwillig)**

Mögliche Erweiterungen sind:

- Unterstützung weiterer Operatoren
- Unterstützung von Funktionen wie `math.floor()`
- Unterstützung von geklammerten Ausdrücken
- Unterstützung eines Modus, in dem Operator und Operanden nicht durch neue
  Zeilen ({kbd}`Enter`) sondern durch Leerzeichen getrennt sind. Dadurch wären
  Eingaben über Dateien in diesem Format möglich.

    ```txt
    + 1 2
    - 3 4
    * 2 32

    ```

    Die Nutzung wäre dann bspw.

    ```bash
    $ cat berechnungen.txt | ./taschenrecher.py
    3
    -1
    64
    ```

```{hint} 📝 Kleine Aufgabe 1
:icon: false

Diese Aufgabe kann als Kleine Aufgabe abgegeben werden.
```


## Selbsttest

Prüfen Sie mit den folgenden Fragen, ob Sie die wichtigsten Bausteine aus
Projekt Taschenrechner II beherrschen.

```{code-cell} python
:tags: [remove-cell]
from jupyterquiz import display_quiz

c = {
    "--jq-multiple-choice-bg": "#202080",
    "--jq-mc-button-bg": "#fafafa",
    "--jq-mc-button-border": "#e0e0e0e0",
    "--jq-mc-button-inset-shadow": "#555555",
    "--jq-many-choice-bg": "#202080",
    "--jq-numeric-bg": "#202080",
    "--jq-numeric-input-bg": "#c0c0c0",
    "--jq-numeric-input-label": "#101010",
    "--jq-numeric-input-shadow": "#999999",
    "--jq-string-bg": "#202080",
    "--jq-incorrect-color": "#c80202",
    "--jq-correct-color": "#009113",
    "--jq-text-color": "#fafafa",
    "--jq-link-color": "#9abafa"
}
```

```{code-cell} python
:tags: [remove-input]
q = [
    {
        "question": "Welchen Datentyp liefert `input()` immer?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "str (Zeichenkette)",
                "correct": True
            },
            {
                "code": "int",
                "correct": False
            },
            {
                "code": "float",
                "correct": False
            },
            {
                "code": "bool",
                "correct": False
            }
        ]
    },
    {
        "question": "Mit welchem Schlüsselwort wiederholen Sie Code, solange eine Bedingung gilt?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "while",
                "correct": True
            },
            {
                "code": "if",
                "correct": False
            },
            {
                "code": "repeat",
                "correct": False
            },
            {
                "code": "loop",
                "correct": False
            }
        ]
    },
    {
        "question": "Welche Exception löst `int(\"Hallo\")` aus? (Name ohne Klammern)",
        "type": "string",
        "answers": [
            {
                "answer": "ValueError",
                "correct": True,
                "match_case": False,
                "fuzzy_threshold": 0.9,
                "feedback": "Richtig: `int()` kann den Text nicht umwandeln und wirft einen `ValueError`."
            }
        ]
    },
    {
        "question": "Wie prüfen Sie, ob das Zeichen `\"+\"` in der Liste `erlaubt = [\"+\", \"-\"]` enthalten ist?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "\"+\" in erlaubt",
                "correct": True
            },
            {
                "code": "erlaubt.contains(\"+\")",
                "correct": False
            },
            {
                "code": "erlaubt == \"+\"",
                "correct": False
            },
            {
                "code": "\"+\" in erlaubt.keys()",
                "correct": False
            }
        ]
    },
    {
        "question": "Wie verlassen Sie eine `while`-Schleife vorzeitig?",
        "type": "multiple_choice",
        "answers": [
            {
                "code": "mit `break`",
                "correct": True
            },
            {
                "code": "mit `continue`",
                "correct": False
            },
            {
                "code": "mit `stop`",
                "correct": False
            },
            {
                "code": "mit `exit`",
                "correct": False
            }
        ]
    }
]

display_quiz(q, colors=c)
```
