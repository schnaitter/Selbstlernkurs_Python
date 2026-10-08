#! /usr/bin/env python3
"""Vollständige beschreibende Statistik ohne pandas (Projekt CSV II).

Referenzlösung zur Aufgabe ``040-Aufgabe_Statistik.ipynb``. Das Skript liest
den zentralen Buchdatensatz ausschließlich mit Bordmitteln ein
(``csv``, ``collections``) und berechnet selbst:

* Anzahl, Summe, Minimum, Maximum,
* Mittelwert, Median, Modus,
* Standardabweichung (Grundgesamtheit und Stichprobe),
* Gesamtverkäufe je Verkaufsjahr,
* die fünf Autor\\*innen mit den höchsten Gesamtverkäufen.

Fehlerhafte Zeilen werden gesammelt und gemeldet, statt das Programm zu
beenden. Es wird keine Bibliothek wie ``pandas`` oder ``statistics`` genutzt.

Aufruf::

    ./statistik.py [CSV-DATEI]
"""

import csv
import sys
from collections import Counter, defaultdict
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
    """Liest den Datensatz robust ein.

    Rückgabe: ``(daten, fehlerhafte_zeilen)``. ``daten`` ist eine Liste
    typisierter Dictionaries, ``fehlerhafte_zeilen`` eine Liste von
    ``(Zeilennummer, Meldung)``-Tupeln.
    """
    daten = []
    fehlerhafte_zeilen = []

    with open(csv_pfad, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        erwartet = len(reader.fieldnames or [])

        for zeilennummer, zeile in enumerate(reader, start=2):
            if len(zeile) != erwartet:
                fehlerhafte_zeilen.append(
                    (
                        zeilennummer,
                        f"{len(zeile)} statt {erwartet} Feldern",
                    )
                )
                continue
            try:
                daten.append(
                    {
                        "isbn": zeile["isbn"],
                        "author": zeile["author"],
                        "year": int(zeile["year"]),
                        "title": zeile["title"],
                        "sales_year": int(zeile["sales_year"]),
                        "sales": int(zeile["sales"]),
                    }
                )
            except (TypeError, ValueError) as fehler:
                fehlerhafte_zeilen.append((zeilennummer, str(fehler)))

    return daten, fehlerhafte_zeilen


# ---------------------------------------------------------------------------
# Kennzahlen – selbst implementiert, ohne `statistics`
# ---------------------------------------------------------------------------

def mittelwert(werte):
    """Arithmetisches Mittel: Summe geteilt durch Anzahl."""
    return sum(werte) / len(werte)


def median(werte):
    """Median: der mittlere Wert der sortierten Liste."""
    sortiert = sorted(werte)
    n = len(sortiert)
    mitte = n // 2
    if n % 2 == 1:
        return sortiert[mitte]
    return (sortiert[mitte - 1] + sortiert[mitte]) / 2


def modus(werte):
    """Häufigster Wert (Modus); bei Gleichstand der kleinere Wert.

    Rückgabe: ``(wert, häufigkeit)``.
    """
    zaehler = Counter(werte)
    wert, haeufigkeit = max(
        zaehler.items(), key=lambda paar: (paar[1], -paar[0])
    )
    return wert, haeufigkeit


def varianz(werte, stichprobe=False):
    """Mittlere quadratische Abweichung vom Mittelwert.

    ``stichprobe=True`` verwendet den Nenner ``n - 1`` (Stichprobenvarianz).
    """
    n = len(werte)
    my = mittelwert(werte)
    quadratsumme = sum((x - my) ** 2 for x in werte)
    nenner = n - 1 if stichprobe else n
    return quadratsumme / nenner


def standardabweichung(werte, stichprobe=False):
    """Quadratwurzel der Varianz (Grundgesamtheit oder Stichprobe)."""
    return varianz(werte, stichprobe=stichprobe) ** 0.5


def kennzahlen(werte, name):
    """Gibt die geforderten Kennzahlen einer Zahlenliste aus."""
    wert, haeufigkeit = modus(werte)
    print(f"--- {name} ---")
    print(f"Anzahl:                        {len(werte)}")
    print(f"Summe:                         {sum(werte)}")
    print(f"Minimum:                       {min(werte)}")
    print(f"Maximum:                       {max(werte)}")
    print(f"Mittelwert:                    {mittelwert(werte):.2f}")
    print(f"Median:                        {median(werte):.2f}")
    print(f"Modus:                         {wert} ({haeufigkeit}-mal)")
    print(f"Standardabweichung (n):        {standardabweichung(werte):.2f}")
    print(
        "Standardabweichung (n-1):      "
        f"{standardabweichung(werte, stichprobe=True):.2f}"
    )
    return mittelwert(werte), median(werte)


def main():
    csv_pfad = sys.argv[1] if len(sys.argv) > 1 else standard_pfad()
    daten, fehlerhafte_zeilen = lies_daten(csv_pfad)

    if not daten:
        print(f"Keine gültigen Datensätze in {csv_pfad} gefunden.")
        sys.exit(1)

    print(f"Datei: {csv_pfad}")
    print(f"Gültige Datensätze: {len(daten)}")
    print(f"Fehlerhafte Zeilen: {len(fehlerhafte_zeilen)}")
    for nummer, meldung in fehlerhafte_zeilen:
        print(f"   Zeile {nummer}: {meldung}")

    verkaufszahlen = [satz["sales"] for satz in daten]

    print()
    my, med = kennzahlen(verkaufszahlen, "Verkäufe je Buch und Jahr")

    # 4) Gruppierung: Gesamtverkäufe pro Verkaufsjahr
    pro_jahr = defaultdict(int)
    for satz in daten:
        pro_jahr[satz["sales_year"]] += satz["sales"]

    print("\nGesamtverkäufe je Verkaufsjahr:")
    for jahr in sorted(pro_jahr):
        print(f"   {jahr}: {pro_jahr[jahr]:>6}")

    # 5) Rangliste: Top-5-Autor*innen
    pro_autor = defaultdict(int)
    for satz in daten:
        pro_autor[satz["author"]] += satz["sales"]

    ranking = sorted(pro_autor.items(), key=lambda paar: paar[1], reverse=True)
    print("\nTop 5 Autor*innen nach Gesamtverkäufen:")
    for platz, (autor, summe) in enumerate(ranking[:5], start=1):
        print(f"   {platz}. {autor}: {summe}")

    # 6) Einordnung der Verteilung
    print("\nEinordnung:")
    if med != 0:
        abweichung = abs(my - med) / med * 100
    else:
        abweichung = float("inf")
    if abweichung > 30:
        print(
            "   Mittelwert und Median weichen deutlich voneinander ab. "
            "Das ist ein typisches Zeichen für eine schiefe Verteilung: "
            "Einzelne sehr hohe Werte ziehen den Mittelwert nach oben, "
            "während der Median davon kaum beeinflusst wird."
        )
    else:
        print(
            "   Mittelwert und Median liegen nah beieinander. "
            "Die Verteilung ist vergleichsweise symmetrisch."
        )


if __name__ == "__main__":
    main()
