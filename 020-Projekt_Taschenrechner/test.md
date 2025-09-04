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

```{code-cell} python3
import micropip

await micropip.install('ipywidgets')
```

```{code-cell} python3
print(2+2)
```

```{code-cell} python3
import sys
from ipywidgets import interact

@interact(b=[8, 16, 32, 64, 128])
def bits(b):
    if sys.maxsize == 2**(b-1) - 1:
        print("Ihre CPU rechnet mit", b, "Bit.")
        print("Die größte darstellbare Ganzzahl ist", 2**(b-1) - 1)
        print("Die kleinste darstellbare Ganzzahl ist", -2**(b-1))
    else:
        print("Probieren Sie einen anderen Wert für b.")
```
