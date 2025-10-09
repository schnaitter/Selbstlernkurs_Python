---
numbering:
    heading_1: true
    heading_2: true
    title: true
    figure:
        template: Abb. %s
---

# Aufgabe: Erweiterung des Taschenrechners

::::{important} Erweiterung des Taschenrechners um zwei Funktionalitäten

**Funktionalität 1:**

Erweitern Sie den Taschenrechner um Multiplikation (`*`), Subtraktion (`-`) und Division (`/`).

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
Für mathematische Operationen gibt es Werte, welche Sie mehrmals in die Berechnung einbeziehen können, ohne das Ergebnis zu verändern.

Für die Addiditon ist dies 0:
$$ 42 + 0 = 42 \\
0 + 42= 42 $$

Für die Multikplikation ist dies 1:
$$ 42 \cdot 1 = 42\\
1 \cdot 42 = 42 $$

Für die Subtraktion ist dies ebenfalls 0, jedoch ist hier die Reihenfolge relevant:
$$ 42-0 = 42 $$
$$ 0-42 \neq 42\\
0 - 42 = -42$$

Ähnliches gilt für die Division:
$$ 42 \div 1 = 42 = \frac{42}{1} $$
$$ 1 \div 42 \neq 42\\
1 \div 42 = \frac{1}{42}$$

Wenn Sie überprüfen, dass es mindestens zwei Operanden gibt, können Sie Subtraktion und Division korrekt lösen, indem Sie anfangs Ihr Ergebnis auf den ersten Wert setzen und dann die restlichen Operanden einbeziehen. Hierzu gibt es die Funktion `.pop(0)`, welche Ihnen das Element am Index 0 zurückgibt und dieses dann aus der Liste entfernt.

```python
xs = [1,2,3]
print(xs)
x = xs.pop(0)
print(xs)
print(x)
```
::: 


**Funktionalität 2:**

Verbessern Sie die Fehlertoleranz des Skripts. Geben Sie der Nutzer\*in Rückmeldung bei der Nutzung falscher Operatoren und wenn die Eingabe für einen Operand nicht als Zahl umgewandelt werden kann. Erlauben Sie dann jeweils weitere Versuche, solange keine leere Eingabe durch die Nutzer\*in erfolgt.

Hierfür müssen Sie die passenden Exceptions "einfangen" und korrekt behandeln. Dies geht analog zum folgenden Code:

```python
try: # enclose code you think will raise an Exception
    n = int("Hallo")
except ValueError as e: # explicitly catch the ValueError; multiple except-clauses are allowed
    print("Please only enter whole numbers. Try again.")
```

::::

```{hint} 📝 Kleine Aufgabe
:icon: false

Diese Aufgabe kann als Kleine Aufgabe abgegeben werden.
```
```{hint} 📝 Kleine Aufgabe
:icon: false

Diese Aufgabe kann als Kleine Aufgabe abgegeben werden.
```
