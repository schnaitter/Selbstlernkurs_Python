---
numbering:
    heading_1: true
    heading_2: true
    title: true
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

:::

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

Verbessern Sie die Fehlertoleranz des Skripts. Geben Sie der Nutzer\*in
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
```

```{hint} 📝 Kleine Aufgabe 1
:icon: false

Diese Aufgabe kann als Kleine Aufgabe abgegeben werden.
```
