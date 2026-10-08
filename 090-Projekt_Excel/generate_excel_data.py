#! /usr/bin/env python3
"""Erzeugt eine bewusst "unsaubere" Excel-Datei mit bibliothekarischen Daten.

Das Skript gehört zum Abschlussprojekt ``090-Projekt_Excel``. Es erzeugt
reproduzierbar (fester Zufallsseed) eine Datei
``assets/data/bibliothek_unsauber.xlsx``. Die Daten enthalten absichtlich
typische Qualitätsprobleme realer Bibliotheksdaten:

* fehlende Werte,
* doppelte Datensätze,
* Zahlen, die als Text gespeichert sind,
* uneinheitliche Kategorien (z. B. ``"ZB"`` statt ``"Zentralbibliothek"``),
* gemischte Datumsformate.

Die Datei enthält zwei Tabellenblätter:

* ``Ausleihen`` - der eigentliche, unsaubere Datensatz,
* ``Standorte`` - eine kleine Nachschlagetabelle mit Standorten.
"""

import random
from pathlib import Path

import pandas as pd

# Fester Seed, damit die erzeugte Datei reproduzierbar ist.
SEED = 42

# Dateipfad unabhängig vom aktuellen Arbeitsverzeichnis bestimmen:
# Skript liegt in ``090-Projekt_Excel/``, die Daten in ``assets/data/``.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = PROJECT_ROOT / "assets" / "data" / "bibliothek_unsauber.xlsx"

TITEL = [
    "Einführung in die Bibliothekswissenschaft",
    "Metadaten in der Praxis",
    "Informationskompetenz vermitteln",
    "Grundlagen der Katalogisierung",
    "Digitalisierung im Archiv",
    "Open Access verstehen",
    "Datenmanagement für Einsteiger*innen",
    "Bibliotheken im digitalen Wandel",
    "Literaturrecherche effizient",
    "Records Management",
    "Bibliometrie kompakt",
    "Urheberrecht in Bibliotheken",
    "Digital Humanities",
    "Wissensorganisation",
    "Bestandsmanagement",
    "Forschungsdaten verwalten",
    "Linked Open Data",
    "E-Books in Bibliotheken",
    "Leseförderung und Medienpädagogik",
    "Bibliotheksethik",
    "Nutzer*innenforschung",
    "Repositorien aufbauen",
    "Langzeitarchivierung",
    "Makerspaces in Bibliotheken",
]

AUTOREN = [
    "Albrecht, Beate",
    "Behrens, Carl",
    "Clausen, Dana",
    "Dittrich, Erik",
    "Engel, Friederike",
    "Fischer, Gerd",
    "Gerlach, Hanna",
    "Hoffmann, Ingo",
    "Iversen, Jana",
    "Jäger, Konrad",
    "Klein, Lena",
    "Lindner, Malik",
    "Möller, Nadine",
]

STANDORTE = [
    "Zentralbibliothek",
    "Zweigstelle Nord",
    "Zweigstelle Süd",
    "Campus West",
    "Magazin",
]

MEDIEN = ["Buch", "E-Book", "Zeitschrift", "DVD", "Hörbuch"]


def zufaellige_kategorien(standort: str, medium: str) -> tuple[str, str]:
    """Verfälscht Kategorien zufällig zu uneinheitlichen Schreibweisen."""
    standort_varianten = {
        "Zentralbibliothek": ["Zentralbibliothek", "ZB", "zentralbibliothek "],
        "Zweigstelle Nord": ["Zweigstelle Nord", "Nord", " Zweigstelle Nord"],
        "Zweigstelle Süd": ["Zweigstelle Süd", "Süd", "Zweigstelle Sued"],
        "Campus West": ["Campus West", "West", "campus west"],
        "Magazin": ["Magazin", "mag ", "MAG"],
    }
    medium_varianten = {
        "Buch": ["Buch", "buch", "Buch "],
        "E-Book": ["E-Book", "eBook", "E-Book "],
        "Zeitschrift": ["Zeitschrift", "Zeitschr.", "zeitschrift"],
        "DVD": ["DVD", "dvd", "DVD "],
        "Hörbuch": ["Hörbuch", "Hörbuch ", "hoerbuch"],
    }
    return (
        random.choice(standort_varianten[standort]),
        random.choice(medium_varianten[medium]),
    )


def zugangsdatum(jahr: int) -> str | None:
    """Erzeugt ein Zugangsdatum in einem von mehreren gemischten Formaten."""
    monat = random.randint(1, 12)
    tag = random.randint(1, 28)
    if random.random() < 0.10:
        return None
    if random.random() < 0.5:
        return f"{jahr:04d}-{monat:02d}-{tag:02d}"
    return f"{tag:02d}.{monat:02d}.{jahr:04d}"


def unsauberer_wert(spalte: str, wert: object) -> object:
    """Verändert einzelne Werte gezielt, um Typ- und Qualitätsprobleme zu erzeugen."""
    zufall = random.random()
    if spalte == "Erscheinungsjahr":
        if zufall < 0.08:
            return None
        if zufall < 0.16:
            return f"{wert} "
        if zufall < 0.20:
            return "unbekannt"
        return int(wert)
    if spalte == "Ausleihzahlen":
        if zufall < 0.07:
            return None
        if zufall < 0.14:
            return "nicht erfasst"
        if zufall < 0.24:
            # Zahl mit deutschem Tausenderpunkt wird als Text gespeichert.
            return f"{wert:,}".replace(",", ".")
        if zufall < 0.30:
            return f" {wert}"
        return int(wert)
    if spalte == "Titel":
        return None if zufall < 0.05 else wert
    if spalte == "Autor*in":
        return None if zufall < 0.08 else wert
    return wert


def erzeuge_datensatz() -> pd.DataFrame:
    """Baut den unsauberen Hauptdatensatz auf."""
    random.seed(SEED)
    zeilen: list[dict[str, object]] = []

    for index in range(60):
        standort = random.choice(STANDORTE)
        medium = random.choice(MEDIEN)
        standort_roh, medium_roh = zufaellige_kategorien(standort, medium)
        erscheinungsjahr = random.randint(1990, 2024)
        if random.random() < 0.15:
            ausleihzahlen = random.randint(1000, 9000)
        else:
            ausleihzahlen = random.randint(5, 420)
        zugang = zugangsdatum(erscheinungsjahr)

        zeile = {
            "Titel": TITEL[index % len(TITEL)],
            "Autor*in": AUTOREN[index % len(AUTOREN)],
            "Erscheinungsjahr": erscheinungsjahr,
            "Ausleihzahlen": ausleihzahlen,
            "Standort": standort_roh,
            "Medium": medium_roh,
            "Zugangsdatum": zugang,
        }
        zeile = {
            spalte: unsauberer_wert(spalte, wert)
            for spalte, wert in zeile.items()
        }
        zeilen.append(zeile)

    # Einige offensichtliche Duplikate einfügen (unsauberer Datenbestand).
    for index in (3, 17, 28, 41, 55):
        zeilen.append(dict(zeilen[index]))

    return pd.DataFrame(zeilen, dtype=object)


def erzeuge_standorte() -> pd.DataFrame:
    """Erzeugt eine kleine, saubere Nachschlagetabelle."""
    return pd.DataFrame(
        {
            "Standort": STANDORTE,
            "Adresse": [
                "Universitätsstraße 1",
                "Nordallee 12",
                "Südring 7",
                "Campusweg 3",
                "Depotstraße 99",
            ],
            "Öffnungsstunden_pro_Woche": [72, 40, 40, 35, 0],
        }
    )


def main() -> None:
    """Schreibt die Excel-Datei mit beiden Tabellenblättern."""
    ausleihen = erzeuge_datensatz()
    standorte = erzeuge_standorte()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
        ausleihen.to_excel(writer, sheet_name="Ausleihen", index=False)
        standorte.to_excel(writer, sheet_name="Standorte", index=False)

    print(f"Geschrieben: {OUTPUT_PATH}")
    print(f"Datensätze (mit Duplikaten): {len(ausleihen)}")


if __name__ == "__main__":
    main()
