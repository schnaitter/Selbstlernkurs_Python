#! /usr/bin/env python3
"""Synthetische Beispieldaten für das Projekt MARC-XML erzeugen.

Das Skript erzeugt zwei zueinander passende Dateien:

* ``assets/data/beispieldaten.json`` – bibliografische Quelldaten als JSON
* ``assets/data/beispieldaten.marcxml`` – dieselben Titel als valider
  MARC-XML-Auszug

Die Daten sind frei erfunden und lizenzrein. Die ISBN-13 wird aus einer
12-stelligen Basis inklusive korrekter Prüfziffer berechnet, damit die
Beispiele realistisch, aber nicht an echte Ausgaben gebunden sind.
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

# MARCXML-Namensraum (Namespace) laut Library of Congress
MARC_NS = "http://www.loc.gov/MARC21/slim"
ET.register_namespace("", MARC_NS)
NS = f"{{{MARC_NS}}}"

# Leader für eine Monografie (Sprache, gedruckte Ressource)
LEADER = "00000nam a2200000 a 4500"

# Ländercode (MARC 008, Position 15–17) je Erscheinungsort
LAENDERCODES = {
    "Berlin": "gw ",
    "München": "gw ",
    "Leipzig": "gw ",
    "Frankfurt": "gw ",
    "Göttingen": "gw ",
    "London": "enk",
    "New York": "nyu",
    "Paris": "fr ",
    "Amsterdam": "ne ",
    "Wien": "au ",
    "Zürich": "sz ",
    "Lisboa": "po ",
    "Roma": "it ",
    "Tokyo": "ja ",
    "Cape Town": "sa ",
    "Stockholm": "sw ",
    "Helsinki": "fi ",
}

# Bibliografische Titel (synthetisch). Die ISBN ist eine 12-stellige Basis,
# die Prüfziffer wird beim Erzeugen ergänzt.
TITEL = [
    {
        "isbn_basis": "978311047001",
        "autor": "Keller, Miriam",
        "titel": "Datenkuration in wissenschaftlichen Bibliotheken",
        "untertitel": "Praktiken, Werkzeuge und Standards",
        "ort": "Berlin",
        "verlag": "Wissenschaftsverlag Berlin",
        "jahr": 2021,
        "sprache": "ger",
        "schlagwoerter": [
            "Bibliothekswissenschaft",
            "Forschungsdaten",
            "Metadaten",
        ],
    },
    {
        "isbn_basis": "978312398012",
        "autor": "Okafor, Chidi",
        "titel": "Metadata for Digital Collections",
        "untertitel": "A Practical Introduction",
        "ort": "London",
        "verlag": "Thames & Library Press",
        "jahr": 2019,
        "sprache": "eng",
        "schlagwoerter": ["Metadata", "Digital libraries"],
    },
    {
        "isbn_basis": "978201359001",
        "autor": "Dupont, Claire",
        "titel": "Catalogage et données ouvertes",
        "untertitel": "",
        "ort": "Paris",
        "verlag": "Éditions du Patrimoine",
        "jahr": 2020,
        "sprache": "fre",
        "schlagwoerter": ["Catalogage", "Open data"],
    },
    {
        "isbn_basis": "978328901234",
        "autor": "Schneider, Jonas",
        "titel": "Praktische Algorithmen für Bibliotheken",
        "untertitel": "Von der Signatur zur Suchmaschine",
        "ort": "München",
        "verlag": "InfoTech Verlag",
        "jahr": 2022,
        "sprache": "ger",
        "schlagwoerter": ["Algorithmen", "Information Retrieval"],
    },
    {
        "isbn_basis": "978944100123",
        "autor": "Almeida, Sofia",
        "titel": "Preserving the Digital Record",
        "untertitel": "Strategies for Long-Term Access",
        "ort": "Amsterdam",
        "verlag": "Museum & Archive Press",
        "jahr": 2018,
        "sprache": "eng",
        "schlagwoerter": ["Digital preservation", "Archives"],
    },
    {
        "isbn_basis": "978370500987",
        "autor": "Nowak, Ewa",
        "titel": "Open Access und die Bibliothek der Zukunft",
        "untertitel": "Strategien für wissenschaftliche Einrichtungen",
        "ort": "Wien",
        "verlag": "Akademischer Verlag Wien",
        "jahr": 2023,
        "sprache": "ger",
        "schlagwoerter": ["Open Access", "Wissenschaft", "Bibliothek"],
    },
    {
        "isbn_basis": "978190200340",
        "autor": "Kowalski, Piotr",
        "titel": "Library Linked Data",
        "untertitel": "From Records to Knowledge Graphs",
        "ort": "New York",
        "verlag": "Metropolitan Library Press",
        "jahr": 2021,
        "sprache": "eng",
        "schlagwoerter": ["Linked data", "Semantic web"],
    },
    {
        "isbn_basis": "978972001230",
        "autor": "Ferreira, Luís",
        "titel": "Gestão de Coleções na Era Digital",
        "untertitel": "",
        "ort": "Lisboa",
        "verlag": "Editora Biblioteca Nova",
        "jahr": 2017,
        "sprache": "por",
        "schlagwoerter": ["Gestão de coleções", "Bibliotecas digitais"],
    },
    {
        "isbn_basis": "978449801230",
        "autor": "Tanaka, Yuki",
        "titel": "Archives and Memory",
        "untertitel": "Collecting the Contemporary",
        "ort": "Tokyo",
        "verlag": "Sakura Academic Press",
        "jahr": 2020,
        "sprache": "eng",
        "schlagwoerter": ["Archives", "Memory", "Collecting"],
    },
    {
        "isbn_basis": "978303800120",
        "autor": "Bianchi, Marco",
        "titel": "Digitalisierung von Kulturerbe",
        "untertitel": "Workflows und Standards",
        "ort": "Zürich",
        "verlag": "Kulturgut Verlag",
        "jahr": 2019,
        "sprache": "ger",
        "schlagwoerter": ["Digitalisierung", "Kulturerbe", "Metadaten"],
    },
    {
        "isbn_basis": "978062100456",
        "autor": "Osei, Ama",
        "titel": "Community Archives",
        "untertitel": "Participation and Power",
        "ort": "Cape Town",
        "verlag": "Ubuntu Press",
        "jahr": 2022,
        "sprache": "eng",
        "schlagwoerter": ["Community archives", "Participation"],
    },
    {
        "isbn_basis": "978917001234",
        "autor": "Lindqvist, Elsa",
        "titel": "Biblioteket och AI",
        "untertitel": "Möjligheter och utmaningar",
        "ort": "Stockholm",
        "verlag": "Nordisk Biblioteksförlag",
        "jahr": 2023,
        "sprache": "swe",
        "schlagwoerter": ["Künstliche Intelligenz", "Bibliothek"],
    },
    {
        "isbn_basis": "978880001230",
        "autor": "Rossi, Giulia",
        "titel": "Il catalogo aperto",
        "untertitel": "Dati collegati in biblioteca",
        "ort": "Roma",
        "verlag": "Edizioni Biblioteche",
        "jahr": 2021,
        "sprache": "ita",
        "schlagwoerter": ["Catalogazione", "Linked data"],
    },
    {
        "isbn_basis": "978386301230",
        "autor": "Meyer, Katharina",
        "titel": "Digital Humanities in der Praxis",
        "untertitel": "Projekte, Methoden, Werkzeuge",
        "ort": "Göttingen",
        "verlag": "Universitätsverlag Göttingen",
        "jahr": 2020,
        "sprache": "ger",
        "schlagwoerter": ["Digital Humanities", "Methoden"],
    },
    {
        "isbn_basis": "978311098765",
        "autor": "Haddad, Nadia",
        "titel": "Records, Rights and Access",
        "untertitel": "Copyright in the Digital Library",
        "ort": "Berlin",
        "verlag": "Wissenschaftsverlag Berlin",
        "jahr": 2018,
        "sprache": "eng",
        "schlagwoerter": ["Copyright", "Access", "Digital library"],
    },
    {
        "isbn_basis": "978398765432",
        "autor": "Petrov, Ivan",
        "titel": "Automatisierung mit Python",
        "untertitel": "Skripte für den Bibliotheksalltag",
        "ort": "Leipzig",
        "verlag": "Code & Buch",
        "jahr": 2024,
        "sprache": "ger",
        "schlagwoerter": ["Python", "Automatisierung", "Bibliothek"],
    },
    {
        "isbn_basis": "978952001230",
        "autor": "Virtanen, Aino",
        "titel": "Open Data for Memory Institutions",
        "untertitel": "",
        "ort": "Helsinki",
        "verlag": "Pohjois Publishing",
        "jahr": 2022,
        "sprache": "eng",
        "schlagwoerter": ["Open data", "Museums"],
    },
    {
        "isbn_basis": "978354001239",
        "autor": "Diallo, Fatou",
        "titel": "Katalogisierung nach RDA",
        "untertitel": "Ein Leitfaden für die Praxis",
        "ort": "Frankfurt",
        "verlag": "Berufsverlag Information",
        "jahr": 2023,
        "sprache": "ger",
        "schlagwoerter": ["RDA", "Katalogisierung", "Metadaten"],
    },
]


def isbn13(basis: str) -> str:
    """Berechnet aus einer 12-stelligen Basis die vollständige ISBN-13."""
    if len(basis) != 12 or not basis.isdigit():
        raise ValueError(f"ISBN-Basis muss 12 Ziffern haben: {basis!r}")
    summe = sum(
        int(zahl) * (1 if i % 2 == 0 else 3) for i, zahl in enumerate(basis)
    )
    pruefziffer = (10 - summe % 10) % 10
    return basis + str(pruefziffer)


def feld_008(jahr: int, sprache: str, ort: str) -> str:
    """Erzeugt ein vereinfachtes, strukturell korrektes 008-Feld."""
    land = LAENDERCODES.get(ort, "   ")
    return f"240101s{jahr:04d}    {land}{' ' * 17}{sprache} d"


def datafield(
    record: ET.Element, tag: str, ind1: str, ind2: str, subfelder
) -> None:
    """Hängt ein Datenfeld mit Unterfeldern an einen Record."""
    feld = ET.SubElement(
        record, f"{NS}datafield", {"tag": tag, "ind1": ind1, "ind2": ind2}
    )
    for code, wert in subfelder:
        ET.SubElement(feld, f"{NS}subfield", {"code": code}).text = wert


def kontrolle(record: ET.Element, tag: str, wert: str) -> None:
    """Hängt ein Kontrollfeld an einen Record."""
    ET.SubElement(record, f"{NS}controlfield", {"tag": tag}).text = str(wert)


def baue_titel() -> list[dict]:
    """Reichert die Titel um ID und vollständige ISBN an."""
    ergebnis = []
    for index, vorlage in enumerate(TITEL, start=1):
        eintrag = dict(vorlage)
        eintrag["id"] = f"{index:09d}"
        eintrag["isbn"] = isbn13(vorlage["isbn_basis"])
        del eintrag["isbn_basis"]
        ergebnis.append(eintrag)
    return ergebnis


def schreibe_json(titel: list[dict], pfad: Path) -> None:
    """Schreibt die JSON-Quelldaten."""
    daten = {
        "quelle": "Synthetische Beispieldaten für den Selbstlernkurs Python",
        "stand": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "anzahl_titel": len(titel),
        "titel": titel,
    }
    pfad.write_text(
        json.dumps(daten, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def schreibe_marcxml(titel: list[dict], pfad: Path) -> None:
    """Schreibt die Titel als MARC-XML-Collection."""
    collection = ET.Element(f"{NS}collection")
    for eintrag in titel:
        record = ET.SubElement(collection, f"{NS}record")
        ET.SubElement(record, f"{NS}leader").text = LEADER

        kontrolle(record, "001", eintrag["id"])
        kontrolle(record, "003", "DE-101")
        kontrolle(record, "005", "20240101120000.0")
        kontrolle(
            record,
            "008",
            feld_008(eintrag["jahr"], eintrag["sprache"], eintrag["ort"]),
        )

        datafield(record, "020", " ", " ", [("a", eintrag["isbn"])])
        datafield(record, "041", "0", " ", [("a", eintrag["sprache"])])
        datafield(record, "100", "1", " ", [("a", eintrag["autor"])])
        if eintrag["untertitel"]:
            datafield(
                record,
                "245",
                "1",
                "0",
                [("a", eintrag["titel"] + " :"), ("b", eintrag["untertitel"])],
            )
        else:
            datafield(record, "245", "1", "0", [("a", eintrag["titel"])])
        datafield(
            record,
            "264",
            " ",
            "1",
            [
                ("a", eintrag["ort"]),
                ("b", eintrag["verlag"]),
                ("c", str(eintrag["jahr"])),
            ],
        )
        for schlagwort in eintrag["schlagwoerter"]:
            datafield(record, "650", " ", "7", [("a", schlagwort)])

    baum = ET.ElementTree(collection)
    ET.indent(baum, space="  ")
    baum.write(pfad, encoding="utf-8", xml_declaration=True)


def main() -> None:
    projektwurzel = Path(__file__).resolve().parent.parent
    datenverzeichnis = projektwurzel / "assets" / "data"
    datenverzeichnis.mkdir(parents=True, exist_ok=True)

    titel = baue_titel()
    json_pfad = datenverzeichnis / "beispieldaten.json"
    marcxml_pfad = datenverzeichnis / "beispieldaten.marcxml"

    schreibe_json(titel, json_pfad)
    schreibe_marcxml(titel, marcxml_pfad)

    print(f"✓ {len(titel)} Titel erzeugt")
    print(f"✓ JSON gespeichert:    {json_pfad.relative_to(projektwurzel)}")
    print(f"✓ MARC-XML gespeichert: {marcxml_pfad.relative_to(projektwurzel)}")


if __name__ == "__main__":
    main()
