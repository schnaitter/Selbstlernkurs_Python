---
short_title: Berechtigungen
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Berechtigungen und ausführbare Skripte

:::::{margin}
::::{seealso} Ausführbare Python-Skripte

Dieses Kapitel ergänzt das Kapitel [Ausführbare
Skripte](../020-Projekt_Taschenrechner_I/050-Ausführbare_Skripte.md) aus dem
Taschenrechner-Projekt mit den Unix-Grundlagen.

::::
:::::

In Unix hat jede Datei Berechtigungen (Permissions), die festlegen, wer was mit
der Datei tun darf. Diese Berechtigungen sind besonders wichtig, wenn Sie
Python-Skripte direkt ausführbar machen möchten.

## Die drei Arten von Berechtigungen

Jede Datei hat drei Arten von Berechtigungen:

| Berechtigung            | Symbol | Bedeutung                                               |
| ----------------------- | ------ | ------------------------------------------------------- |
| **Read** (Lesen)        | `r`    | Datei lesen / Verzeichnisinhalt anzeigen                |
| **Write** (Schreiben)   | `w`    | Datei ändern / Dateien im Verzeichnis erstellen/löschen |
| **Execute** (Ausführen) | `x`    | Datei als Programm ausführen / In Verzeichnis wechseln  |

## Die drei Nutzer\*innen-Gruppen

Berechtigungen gelten für drei verschiedene Gruppen:

| Gruppe                    | Bedeutung                                      |
| ------------------------- | ---------------------------------------------- |
| **User** (Eigentümer\*in) | Die Person, die die Datei erstellt hat         |
| **Group** (Gruppe)        | Nutzer\*innen, die zur gleichen Gruppe gehören |
| **Others** (Alle anderen) | Alle anderen Nutzer\*innen des Systems         |

## Berechtigungen anzeigen (`ls -l`)

:::::{margin}
::::{note} Verzeichnisrechte

Bei Verzeichnissen bedeutet:

- `r`: Inhalt auflisten
- `w`: Dateien erstellen/löschen
- `x`: In Verzeichnis wechseln

::::
:::::

Mit `ls -l` sehen Sie die Berechtigungen:

```console
$ ls -l
-rw-r--r--  1 alice users  1234 Okt 17 10:00 README.md
-rwxr-xr-x  1 alice users   512 Okt 17 10:05 skript.py
drwxr-xr-x  2 alice users  4096 Okt 17 09:00 data
```

Die erste Spalte zeigt die Berechtigungen in diesem Format:

```
-rwxr-xr-x
│└┬┘└┬┘└┬┘
│ │  │  └─ Others:   r-x (lesen, ausführen)
│ │  └──── Group:    r-x (lesen, ausführen)
│ └─────── User:     rwx (lesen, schreiben, ausführen)
└───────── Dateityp: - = Datei, d = Verzeichnis, l = Link
```

### Beispiele

```
-rw-r--r--  Eigentümer*in kann lesen/schreiben, alle anderen nur lesen
-rwxr-xr-x  Eigentümer*in kann alles, andere können lesen/ausführen
drwxr-xr-x  Verzeichnis, Eigentümer*in kann alles, andere lesen/betreten
```

## Berechtigungen ändern (`chmod`)

:::::{margin}
::::{hint} `chmod` = Change Mode

Mit `chmod` ändern Sie die Zugriffsrechte einer Datei oder eines
Verzeichnisses.

::::
:::::

Mit `chmod` (change mode) ändern Sie Berechtigungen.

### Symbolische Notation

```console
$ chmod u+x skript.py
```

- `u` = User (Eigentümer\*in)
- `g` = Group (Gruppe)
- `o` = Others (Andere)
- `a` = All (Alle drei)

- `+` = Berechtigung hinzufügen
- `-` = Berechtigung entfernen
- `=` = Berechtigung exakt setzen

Beispiele:

```console
$ chmod u+x datei.py       # Eigentümer*in: ausführbar machen
$ chmod go-w datei.txt     # Group und Others: Schreibrecht entziehen
$ chmod a+r datei.txt      # Alle: Leseberechtigung geben
$ chmod u=rwx,go=rx dir/   # User: rwx, Group+Others: rx
```

### Numerische Notation

Berechtigungen können auch als Zahl angegeben werden:

| Berechtigung  | Wert |
| ------------- | ---- |
| `r` (read)    | 4    |
| `w` (write)   | 2    |
| `x` (execute) | 1    |

Die Werte werden addiert:

```
rwx = 4+2+1 = 7
rw- = 4+2+0 = 6
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
```

Drei Ziffern für User, Group, Others:

```console
$ chmod 755 skript.py
```

Bedeutet:

- User: 7 (rwx)
- Group: 5 (r-x)
- Others: 5 (r-x)

Häufige Kombinationen:

```console
$ chmod 644 datei.txt     # rw-r--r-- (normale Datei)
$ chmod 755 skript.py     # rwxr-xr-x (ausführbares Skript)
$ chmod 700 privat.txt    # rwx------ (nur Eigentümer*in)
$ chmod 777 öffentlich    # rwxrwxrwx (alle Rechte für alle - selten sinnvoll!)
```

## Python-Skripte ausführbar machen

:::::{margin}
::::{seealso} Shebang-Zeile

Mehr zur Shebang-Zeile im Kapitel [Ausführbare
Skripte](../020-Projekt_Taschenrechner_I/050-Ausführbare_Skripte.md).

::::
:::::

Um ein Python-Skript direkt ausführbar zu machen (ohne `python3` davor):

### 1. Shebang-Zeile hinzufügen

Erste Zeile der Datei:

```python
#! /usr/bin/env python3

print("Hallo Welt!")
```

Die Shebang-Zeile (`#!`) sagt dem System, mit welchem Programm die Datei
ausgeführt werden soll.

### 2. Ausführbarkeit setzen

```console
$ chmod +x mein-skript.py
```

Oder explizit:

```console
$ chmod u+x mein-skript.py
```

### 3. Skript ausführen

```console
$ ./mein-skript.py
Hallo Welt!
```

Das `./` ist wichtig – es bedeutet "im aktuellen Verzeichnis".

## Praktisches Beispiel

Erstellen Sie ein ausführbares Python-Skript:

```console
$ cat > taschenrechner.py << 'EOF'
#! /usr/bin/env python3

def addiere(a, b):
    return a + b

if __name__ == "__main__":
    ergebnis = addiere(5, 3)
    print(f"5 + 3 = {ergebnis}")
EOF
```

Berechtigungen überprüfen:

```console
$ ls -l taschenrechner.py
-rw-r--r--  1 alice users  123 Okt 17 10:30 taschenrechner.py
```

Ausführbar machen:

```console
$ chmod +x taschenrechner.py
$ ls -l taschenrechner.py
-rwxr-xr-x  1 alice users  123 Okt 17 10:30 taschenrechner.py
```

Beachten Sie das `x` in den Berechtigungen!

Ausführen:

```console
$ ./taschenrechner.py
5 + 3 = 8
```

## Warum `./` vor dem Skriptnamen?

:::::{margin}
::::{caution} Sicherheit

Der aktuelle Ordner (`.`) ist **absichtlich nicht** im `$PATH`, um zu
verhindern, dass versehentlich unbekannte Programme ausgeführt werden.

::::
:::::

Unix sucht Programme in bestimmten Verzeichnissen, die in der Umgebungsvariable
`$PATH` definiert sind:

```console
$ echo $PATH
/usr/local/bin:/usr/bin:/bin
```

Das aktuelle Verzeichnis (`.`) ist **nicht** im `$PATH`. Daher müssen Sie `./`
explizit angeben:

```console
$ ./skript.py      # Funktioniert
$ skript.py        # Fehler: Befehl nicht gefunden
```

## Unterschied: `python3 skript.py` vs. `./skript.py`

| Mit `python3`                     | Mit `./` (ausführbar)              |
| --------------------------------- | ---------------------------------- |
| `python3 skript.py`               | `./skript.py`                      |
| Benötigt keine Shebang-Zeile      | Benötigt Shebang-Zeile             |
| Benötigt keine Ausführbarkeit     | Benötigt `chmod +x`                |
| Python-Version explizit angegeben | Python-Version aus Shebang         |
| Funktioniert auf allen Systemen   | Funktioniert nur auf Unix-Systemen |

Für die Entwicklung ist `python3 skript.py` oft einfacher. Für
Produktions-Skripte oder Tools, die wie Programme genutzt werden sollen, ist
`./skript.py` eleganter.

:::::{admonition} 💪 Übung
:icon: false

Erstellen Sie ein ausführbares Python-Skript:

1. Erstellen Sie eine Datei `hallo.py` mit folgendem Inhalt:

    ```python
    #! /usr/bin/env python3

    name = input("Wie heißen Sie? ")
    print(f"Hallo, {name}!")
    ```

2. Überprüfen Sie die Berechtigungen mit `ls -l hallo.py`
3. Versuchen Sie es auszuführen: `./hallo.py` (sollte fehlschlagen)
4. Machen Sie es ausführbar: `chmod +x hallo.py`
5. Überprüfen Sie erneut die Berechtigungen
6. Führen Sie es aus: `./hallo.py`
7. Testen Sie auch: `python3 hallo.py`

:::{dropdown} ✅ Lösung

```console
$ cat > hallo.py << 'EOF'
#! /usr/bin/env python3

name = input("Wie heißen Sie? ")
print(f"Hallo, {name}!")
EOF
$ ls -l hallo.py
-rw-r--r--  1 alice users  89 Okt 17 11:00 hallo.py
$ ./hallo.py
bash: ./hallo.py: Permission denied
$ chmod +x hallo.py
$ ls -l hallo.py
-rwxr-xr-x  1 alice users  89 Okt 17 11:00 hallo.py
$ ./hallo.py
Wie heißen Sie? Alice
Hallo, Alice!
$ python3 hallo.py
Wie heißen Sie? Bob
Hallo, Bob!
```

Beide Methoden funktionieren, aber nur nach `chmod +x` ist das direkte
Ausführen mit `./` möglich.

:::
:::::

## Zusammenfassung

| Befehl        | Bedeutung                   | Beispiel              |
| ------------- | --------------------------- | --------------------- |
| `ls -l`       | Berechtigungen anzeigen     | `ls -l datei.py`      |
| `chmod u+x`   | Ausführbar für User         | `chmod u+x skript.py` |
| `chmod 755`   | rwxr-xr-x setzen            | `chmod 755 skript.py` |
| `chmod +x`    | Ausführbar für alle         | `chmod +x skript.py`  |
| `./skript.py` | Ausführbares Skript starten | `./taschenrechner.py` |

Berechtigungen sind ein mächtiges Sicherheitsfeature von Unix-Systemen. Sie
verhindern, dass unbefugte Nutzer\*innen Dateien ändern oder Programme
ausführen können.
