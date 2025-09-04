---
numbering:
    heading_1: true
    heading_2: true
    title: true
    figure:
        template: Abb. %s
kernelspec:
    name: python3
    display_name: "Python 3"
---

# Grundlegende Mathematik in Python

<!--
```{code-cell} python3
:tags: hide-cell
import micropip

await micropip.install('ipywidgets')
```
-->

Python beinhaltet standardmäßig Operatoren für alle grundlegenden Berechnungen,
die Sie normalerweise im Laufe eines Programmes durchführen wollen.

## Arithmetische Operationen

Die nachfolgenden Beispiel nutzen die Funktionalität eines d

### Addition

Die Addition in Python nutzt wie zu erwarten das Zeichen `+`.

```{code-cell} python3
2 + 2
```

Ganzzahlen in Python können dabei beliebig groß sein.

```{code-cell} python3
2000000000000 + 2000000000000
```

Es können mehrere Operationen hintereinander gestellt werden.

```{code-cell} python3
987654321987654321987654321 + 123456789123456789123456789 + 1
```

Dies ist äquivalent zu:

`````{margin}
````{hint} Variablen

Eine Variable wird definiert und deren Wert festgelegt, wenn sie links von einem Python Ausdruck steht:

```python
# Speichere den Wert 5 in a
a = 5
# Speichere nun den Wert 10 in a
a = 10
```

````

````{hint} "plus equal" Operator

Soll der Wert einer Variablen um einen bestimmten Wert verändert werden, so kann dies mit dem Operator `+=` geschehen.

```python
a = 10
a += 1
# a -> 11
a +=4
# a -> 15
```
Dieser Operator ist äquivalent zum folgenden Ausdruck:
```python
a = a + 1
```

````
`````

```{code-cell} python3
a = 987654321987654321987654321 + 123456789123456789123456789
a += 1
a
```

### Subtraktion

Ähnlich zur Addition funktioniert auch die Subtraktion.

```{code-cell} python3
987654321987654321987654321 - 123456789123456789123456789
```

Da so große Zahlen schnell unübersichtlich werden erlaubt Python die Nutzung von `_` in einer Zahl. Dieses Zeichen wird bei der Verarbeitung einfach ignoriert.

```{code-cell} python3
4_294_967_296 - 65_536
```

- Mathematische Operationen
    - `+`, `-`, `*`, `/`
    - `%`, `//`
    - `**`
- Zahlen
    - `int()`
    - `float()`
