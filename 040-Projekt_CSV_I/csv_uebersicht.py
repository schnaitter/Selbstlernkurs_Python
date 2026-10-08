#! /usr/bin/env python3
"""Kleines Kommandozeilen-Werkzeug für CSV-Verkaufsdaten.

Aufruf:
    ./csv_uebersicht.py CSV-DATEI
"""

import csv
import sys


def uebersicht(csv_pfad):
    """Gibt die Anzahl der Datensätze und die Summe der Verkäufe aus."""
    anzahl = 0
    verkauft = 0

    with open(csv_pfad, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for zeile in reader:
            anzahl += 1
            verkauft += int(zeile["sales"])

    print(f"Datei: {csv_pfad}")
    print(f"Datensätze: {anzahl}")
    print(f"Verkaufte Bücher insgesamt: {verkauft}")


def main():
    # sys.argv[0] ist der Programmname, der eigentliche Parameter beginnt bei 1.
    if len(sys.argv) != 2:
        print("Aufruf: csv_uebersicht.py CSV-DATEI")
        sys.exit(1)

    uebersicht(sys.argv[1])


if __name__ == "__main__":
    main()
