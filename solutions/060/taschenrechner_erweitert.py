#! /usr/bin/env python3
"""Erweiterter Taschenrechner (Projekt Taschenrechner II).

Referenzlösung zur Aufgabe ``050-Aufgabe_Erweiterung.md``. Das Skript kann

* die vier Grundrechenarten ``+``, ``-``, ``*`` und ``/`` verarbeiten,
* beliebig viele Operanden entgegennehmen (leere Eingabe beendet die
  Operandenliste),
* falsche Operatoren und ungültige Operanden abfangen und die Eingabe
  wiederholen lassen,
* eine Division durch Null abfangen.

Eine leere Eingabe an der Operator-Abfrage beendet das Programm.

Aufruf::

    ./taschenrechner_erweitert.py
"""

ERLAUBTE_OPERATOREN = ("+", "-", "*", "/")


def lies_operator():
    """Liest einen Operator ein.

    Bei leerer Eingabe wird ``None`` zurückgegeben – das signalisiert das
    Programmende. Unbekannte Operatoren führen zu einer Fehlermeldung und
    einem erneuten Versuch. Ein Dateiende (EOF) wird wie eine leere Eingabe
    behandelt.
    """
    while True:
        try:
            text = input("> ").strip()
        except EOFError:
            return None

        if text == "":
            return None
        if text in ERLAUBTE_OPERATOREN:
            return text
        print(f"Unbekannter Operator {text!r}. Erlaubt sind: + - * /")


def lies_operanden():
    """Liest Operanden ein, bis eine leere Eingabe erfolgt.

    Nicht als Zahl lesbare Eingaben werden gemeldet und nicht übernommen;
    die Nutzer\\*in kann es erneut versuchen. Ein Komma als Dezimaltrennzeichen
    (z. B. ``3,5``) wird akzeptiert.
    """
    zahlen = []
    while True:
        try:
            text = input(">> ").strip()
        except EOFError:
            return zahlen

        if text == "":
            return zahlen
        try:
            zahlen.append(float(text.replace(",", ".")))
        except ValueError:
            print(f"{text!r} ist keine Zahl. Bitte erneut eingeben.")


def formatiere(zahl):
    """Gibt ganze Zahlen ohne unnötige Nachkommastellen aus."""
    if zahl == int(zahl):
        return str(int(zahl))
    return f"{zahl:g}"


def berechne(operator, zahlen):
    """Wendet den Operator auf die Operanden an.

    Gibt ``None`` zurück, wenn keine Operanden vorliegen oder durch Null
    geteilt werden soll.
    """
    if not zahlen:
        print(f"ERROR: Operator {operator!r} needs at least one operand.")
        return None

    ergebnis = zahlen[0]
    for zahl in zahlen[1:]:
        if operator == "+":
            ergebnis += zahl
        elif operator == "-":
            ergebnis -= zahl
        elif operator == "*":
            ergebnis *= zahl
        elif operator == "/":
            if zahl == 0:
                print("ERROR: Division durch Null ist nicht erlaubt.")
                return None
            ergebnis /= zahl

    return ergebnis


def main():
    while True:
        operator = lies_operator()
        if operator is None:
            print("Programm wird beendet.")
            break

        zahlen = lies_operanden()
        ergebnis = berechne(operator, zahlen)
        if ergebnis is not None:
            print(formatiere(ergebnis))


if __name__ == "__main__":
    main()
