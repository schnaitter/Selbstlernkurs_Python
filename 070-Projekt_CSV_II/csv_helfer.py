#! /usr/bin/env python3
"""Gemeinsame Hilfsfunktionen für das Modul Projekt CSV II.

Die Notebooks in ``070-Projekt_CSV_II`` arbeiten mit derselben zentralen
Testdatei ``assets/data/books_powerlaw_dataset.csv``. Damit das Einlesen
unabhängig vom aktuellen Arbeitsverzeichnis funktioniert, suchen die
Funktionen die Datei ab dem aktuellen Ordner aufwärts.
"""

import csv
from pathlib import Path

DATENSATZ_RELATIV = Path("assets") / "data" / "books_powerlaw_dataset.csv"


def finde_datensatz():
    """Sucht die zentrale CSV-Datei ab dem aktuellen Verzeichnis aufwärts.

    Rückgabe: ``pathlib.Path`` zur gefundenen Datei. Wird die Datei nicht
    gefunden, löst die Funktion einen ``FileNotFoundError`` aus.
    """
    start = Path.cwd().resolve()
    for ordner in [start, *start.parents]:
        kandidat = ordner / DATENSATZ_RELATIV
        if kandidat.exists():
            return kandidat
    raise FileNotFoundError(
        f"{DATENSATZ_RELATIV} wurde nicht gefunden"
    )


def lade_daten(pfad):
    """Liest die CSV-Datei und gibt eine Liste typisierter Dictionaries zurück."""
    daten = []
    with open(pfad, encoding="utf-8", newline="") as f:
        for zeile in csv.DictReader(f):
            daten.append({
                "isbn": zeile["isbn"],
                "author": zeile["author"],
                "year": int(zeile["year"]),
                "title": zeile["title"],
                "sales_year": int(zeile["sales_year"]),
                "sales": int(zeile["sales"]),
            })
    return daten
