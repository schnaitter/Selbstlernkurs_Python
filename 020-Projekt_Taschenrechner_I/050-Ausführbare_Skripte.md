---
short_title: Skripte
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# (Ausführbare) Skripte

Eine Python-Datei wird umgangssprachlich zum Skript, wenn sie ein bis zwei
Eigenschaften ausweist:

1. Die Datei "tut" etwas beim Ausführen und beinhaltet bspw. nicht nur
   Funktionsdefinitionen.
2. Die Datei ist "ausführbar" und es muss nicht explizit der Python-Interpreter
   genutzt werden.

## Der Einstiegspunkt eines Skripts

Ein Skript kann auf zwei grundlegende Weisen gestaltet sein, damit es beim
ausführen "etwas tut". Aller Code in der Datei wird von oben nach unten
ausgeführt. Führt dieser Code zu Effekten, die "von außen" sichtbar sind, so
"tut" der Code etwas. Ein Beispiel dafür ist:

```{include} ../solutions/020/skript1.py
:lang: python
:enumerated: true
:linenos: true

```

Wird dieses Skript ausgeführt, so ist der gedruckte Text "von außen" sichtbar:

```console
$ python3 skript1.py
Hallo, da draußen!
```

Importiert man das Skript, so wird ebenfalls der Text gedruckt.

```python-repl
>>> import skript1
Hallo, da draußen!
>>>
```

Das ist nicht unbedingt immer gewünschtes Verhalten. Es gibt die Möglichkeit,
gewissen Code nur auszuführen, wenn eine Datei als Skript ausgeführt nicht aber
importiert wird. Sehen wir uns hierzu eine weitere Version des Skripts an:

```{include} ../solutions/020/skript2.py
:lang: python
:enumerated: true
:linenos: true

```

Wird diese Datei importiert, so steht anschließend die Funktion `return_five()`
zur Verfügung, ohne, dass der Text gedruckt wurde:

```python-repl
import skript2
>>> skript2.return_five()
5
>>>
```

Wird die Datei jedoch als Skript ausgeführt, so wird der Text ausgeführt.

```console
$ python3 skript2.py
Hallo, da draußen!
5
```

Somit können Dateien sowohl als Skript als auch als Modul für den Import
fungieren.

## Ausführbarkeit der Datei

Manchmal würde man gerne ein Skript wie folgt ausführen:

```console
$ skript3
Hallo, da draußen!
5
```

Auf diese Lösung kommen wir hier nicht ganz (um mehr zu erfahren recherchieren
Sie `$PATH`-Variablen), aber wir werden die folgende Option hinbekommen. Im
Ordner, in dem ein Skript liegt soll folgende Nutzung möglich sein:

```console
$ ./skript3.py
Hallo, da draußen!
5
```

Dafür müssen zwei Bedingungen erfüllt sein:

1. Die Datei muss Rechte für die Ausführbarkeit haben.
2. Das Terminal muss wissen, mit welchem Programm das Skript ausgeführt werden
   soll.

Eine Datei hat Lese-, Schreib- und Ausführbarkeitsrechte für verschiedene
Nutzer\*innen-Gruppen. Unter Unix können wir die Datei für alle Nutzer\*innen
ausführbar machen indem wir den Befehl `chmod +x skript3.py` im Terminal
ausführen.

In Unix-basierten Betriebssystemen kann die erste Zeile einer Datei eine
sogenannte Shebang-Zeile sein. Diese beginnt mit `#!` (Hash und Bang) und
signalisiert dadurch, dass die Datei an das in der Shebang-Zeile definierte
Programm für die Ausführung übergeben werden soll. Es empfiehlt sich hier,
nicht direkt auf `python3` zu verweisen sondern das Programm `/usr/bin/env` mit
dem Parameter `python3` zu nutzen, welches den korrekten Python-Interpreter
sucht.

Das ausführbare Skript sieht damit so aus:

```{include} ../solutions/020/skript3.py
:lang: python
:enumerated: true
:linenos: true

```

Unter Windows funktionieren diese Art der Skripte etwas anders. Wir gehen hier
von der Nutzung in JupyterHub aus.
