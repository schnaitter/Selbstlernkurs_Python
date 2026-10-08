#! /usr/bin/env python3
"""Referenzlösung zur Bestseller-Aufgabe (Projekt CSV I).

Das Skript liest die zentrale Verkaufs-CSV mit ``csv.DictReader`` ein,
aggregiert die Verkäufe je Werk und beantwortet die Fragen der Aufgabe:

1. Welches Werk wurde insgesamt am häufigsten verkauft?
2. Welches Werk war in den meisten Jahren Bestseller?
3. Welches Werk unter den Bestsellern wurde am seltensten gekauft?

Die "Bestseller" eines Jahres sind dabei die Werke, die im jeweiligen
Verkaufsjahr (``sales_year``) die höchste Verkaufszahl erzielt haben.

Aufruf::

    ./bestseller.py [CSV-DATEI]

Ohne Argument wird der zentrale Datensatz
``assets/data/books_powerlaw_dataset.csv`` verwendet. So lässt sich das Skript
auch auf den selbst erzeugten Datensatz (1990--2025) anwenden.
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
    """Liest die CSV-Datei und gibt eine Liste typisierter Dictionaries zurück.

    Fehlerhafte Zeilen (falsche Feldanzahl oder nicht als Zahl lesbare Werte)
    werden übersprungen und mit Zeilennummer gemeldet, damit das Programm
    nicht abbricht.
    """
    daten = []
    fehlerhafte_zeilen = []

    with open(csv_pfad, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        erwartet = len(reader.fieldnames or [])

        for zeilennummer, zeile in enumerate(reader, start=2):
            if len(zeile) != erwartet:
                fehlerhafte_zeilen.append(
                    f"Zeile {zeilennummer}: {len(zeile)} statt {erwartet} Felder"
                )
                continue
            try:
                daten.append(
                    {
                        "isbn": zeile["isbn"],
                        "author": zeile["author"],
                        "title": zeile["title"],
                        "year": int(zeile["year"]),
                        "sales_year": int(zeile["sales_year"]),
                        "sales": int(zeile["sales"]),
                    }
                )
            except ValueError as fehler:
                fehlerhafte_zeilen.append(f"Zeile {zeilennummer}: {fehler}")

    return daten, fehlerhafte_zeilen


def aggregiere(daten):
    """Aggregiert die Gesamtverkäufe je Werk (Schlüssel: ISBN)."""
    gesamtverkaeufe = defaultdict(int)
    werke = {}

    for satz in daten:
        isbn = satz["isbn"]
        gesamtverkaeufe[isbn] += satz["sales"]
        werke[isbn] = satz

    return gesamtverkaeufe, werke


def ermittle_bestseller_je_jahr(daten):
    """Bestimmt für jedes Verkaufsjahr die Werke mit der höchsten Verkaufszahl.

    Rückgabe: ``{jahr: {isbn, ...}}``. Bei Gleichstand werden alle betroffenen
    Werke aufgenommen.
    """
    pro_jahr = defaultdict(list)
    for satz in daten:
        pro_jahr[satz["sales_year"]].append(satz)

    bestseller_je_jahr = {}
    for jahr, saetze in pro_jahr.items():
        maximum = max(satz["sales"] for satz in saetze)
        bestseller_je_jahr[jahr] = {
            satz["isbn"] for satz in saetze if satz["sales"] == maximum
        }

    return bestseller_je_jahr


def beschrifte(satz):
    """Kurze, lesbare Beschreibung eines Werks."""
    return f"{satz['title']} – {satz['author']} ({satz['year']})"


def main():
    csv_pfad = sys.argv[1] if len(sys.argv) > 1 else standard_pfad()

    daten, fehlerhafte_zeilen = lies_daten(csv_pfad)
    if not daten:
        print(f"Keine gültigen Datensätze in {csv_pfad} gefunden.")
        sys.exit(1)

    gesamtverkaeufe, werke = aggregiere(daten)
    bestseller_je_jahr = ermittle_bestseller_je_jahr(daten)

    jahre_als_bestseller = defaultdict(int)
    for isbns in bestseller_je_jahr.values():
        for isbn in isbns:
            jahre_als_bestseller[isbn] += 1

    print(f"Datei: {csv_pfad}")
    print(f"Datensätze: {len(daten)}, Werke: {len(werke)}")
    if fehlerhafte_zeilen:
        print(f"Übersprungene, fehlerhafte Zeilen: {len(fehlerhafte_zeilen)}")

    # Frage 1: meiste Verkäufe insgesamt
    top_isbn = max(gesamtverkaeufe, key=lambda isbn: gesamtverkaeufe[isbn])
    print("\n1) Meistverkauftes Werk insgesamt:")
    print(f"   {beschrifte(werke[top_isbn])}")
    print(f"   Verkäufe: {gesamtverkaeufe[top_isbn]}")

    # Frage 2: am häufigsten Bestseller
    jahre_isbn = max(jahre_als_bestseller, key=lambda isbn: jahre_als_bestseller[isbn])
    print("\n2) Werk mit den meisten Bestseller-Jahren:")
    print(f"   {beschrifte(werke[jahre_isbn])}")
    print(f"   Bestseller in {jahre_als_bestseller[jahre_isbn]} von "
          f"{len(bestseller_je_jahr)} Jahren")

    # Frage 3: seltenster Bestseller unter den Bestsellern
    seltenste_isbn = min(
        jahre_als_bestseller, key=lambda isbn: gesamtverkaeufe[isbn]
    )
    print("\n3) Seltenster Bestseller (unter allen Bestsellern):")
    print(f"   {beschrifte(werke[seltenste_isbn])}")
    print(f"   Verkäufe insgesamt: {gesamtverkaeufe[seltenste_isbn]}")
    print(f"   Bestseller in {jahre_als_bestseller[seltenste_isbn]} Jahr(en)")

    # Zusatz: Bestseller je Jahr ausgeben
    print("\nBestseller je Verkaufsjahr:")
    for jahr in sorted(bestseller_je_jahr):
        for isbn in sorted(bestseller_je_jahr[jahr]):
            print(f"   {jahr}: {beschrifte(werke[isbn])} "
                  f"({gesamtverkaeufe[isbn]} Verkäufe insgesamt)")


if __name__ == "__main__":
    main()
