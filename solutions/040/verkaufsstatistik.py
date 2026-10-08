#! /usr/bin/env python3
"""Statistik-Ausgabe zu den Verkaufszahlen (Projekt CSV I).

Zweites Referenzskript zur Bestseller-Aufgabe: Statt einer einzelnen
Bestenliste gibt es hier einen Überblick über den gesamten Datensatz –
Gesamtverkäufe, Verkäufe je Jahr und die zehn erfolgreichsten Werke.

Aufruf::

    ./verkaufsstatistik.py [CSV-DATEI]
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path


def standard_pfad():
    """Liefert den Pfad zum zentralen Datensatz im Projekt."""
    return (
        Path(__file__).resolve().parent.parent.parent
        / "assets"
        / "data"
        / "books_powerlaw_dataset.csv"
    )


def lies_daten(csv_pfad):
    """Liest die CSV-Datei robust ein und typisiert die Zahlenspalten."""
    daten = []
    with open(csv_pfad, encoding="utf-8", newline="") as f:
        for zeile in csv.DictReader(f):
            try:
                daten.append(
                    {
                        "isbn": zeile["isbn"],
                        "author": zeile["author"],
                        "title": zeile["title"],
                        "sales_year": int(zeile["sales_year"]),
                        "sales": int(zeile["sales"]),
                    }
                )
            except (TypeError, ValueError):
                continue
    return daten


def main():
    csv_pfad = sys.argv[1] if len(sys.argv) > 1 else standard_pfad()
    daten = lies_daten(csv_pfad)

    if not daten:
        print(f"Keine gültigen Datensätze in {csv_pfad} gefunden.")
        sys.exit(1)

    verkaeufe = [satz["sales"] for satz in daten]
    pro_jahr = defaultdict(int)
    pro_werk = defaultdict(int)
    titel_je_isbn = {}

    for satz in daten:
        pro_jahr[satz["sales_year"]] += satz["sales"]
        pro_werk[satz["isbn"]] += satz["sales"]
        titel_je_isbn[satz["isbn"]] = f"{satz['title']} – {satz['author']}"

    print(f"Datei: {csv_pfad}")
    print(f"Datensätze:             {len(daten)}")
    print(f"Werke:                  {len(pro_werk)}")
    print(f"Verkaufsjahre:          {len(pro_jahr)}")
    print(f"Verkäufe insgesamt:     {sum(verkaeufe)}")
    print(f"Verkäufe je Datensatz:  {sum(verkaeufe) / len(verkaeufe):.2f}")

    print("\nVerkäufe je Verkaufsjahr:")
    for jahr in sorted(pro_jahr):
        print(f"   {jahr}: {pro_jahr[jahr]:>6}")

    print("\nTop 10 Werke nach Gesamtverkäufen:")
    ranking = sorted(pro_werk.items(), key=lambda paar: paar[1], reverse=True)
    for platz, (isbn, summe) in enumerate(ranking[:10], start=1):
        print(f"   {platz:>2}. {summe:>5}  {titel_je_isbn[isbn]}")


if __name__ == "__main__":
    main()
