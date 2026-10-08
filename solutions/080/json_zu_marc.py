#! /usr/bin/env python3
"""Musterloesung zu Aufgabe 2 des Projekts MARC-XML.

Das Skript liest ``assets/data/beispieldaten.json`` ein, ergaenzt drei frei
erfundene Titel und schreibt daraus die valide MARC-XML-Datei ``aufgabe.marcxml``
neben dieses Skript. Am Ende wird mit ``ElementTree`` geprueft, dass die
erzeugte Datei genauso viele Records enthaelt wie die verwendete Titelliste.

Die drei Zusatztitel stehen bewusst im Skript, damit die gelieferten
Beispieldaten unter ``assets/data/`` unveraendert bleiben. In einer eigenen
Loesung koennen die Titel naturlich direkt in der JSON-Datei ergaenzt werden.

Aufruf (aus dem Projektverzeichnis oder aus ``solutions/080/``):

.. code-block:: console

    $ python3 solutions/080/json_zu_marc.py
"""

import json
from pathlib import Path
from xml.etree import ElementTree as ET

MARC_NS = "http://www.loc.gov/MARC21/slim"
ET.register_namespace("", MARC_NS)
NS_TAG = f"{{{MARC_NS}}}"

QUELLDATEI = "beispieldaten.json"
ZIELDATEI = "aufgabe.marcxml"

LEADER = "00000nam a2200000 a 4500"

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

# Drei frei erfundene Zusatztitel mit eindeutigen IDs.
ZUSATZ_TITEL = [
    {
        "id": "000000101",
        "isbn": "9783000000101",
        "autor": "Beispiel, Bea",
        "titel": "Metadaten fuer Einsteiger*innen",
        "untertitel": "Ein praktischer Leitfaden",
        "ort": "Berlin",
        "verlag": "Lehrbuchverlag",
        "jahr": 2024,
        "sprache": "ger",
        "schlagwoerter": ["Metadaten", "Bibliothek"],
    },
    {
        "id": "000000102",
        "isbn": "9783000000102",
        "autor": "Muster, Max",
        "titel": "Linked Data in Libraries",
        "untertitel": "From Records to Graphs",
        "ort": "London",
        "verlag": "Open Press",
        "jahr": 2023,
        "sprache": "eng",
        "schlagwoerter": ["Linked Data", "Metadata"],
    },
    {
        "id": "000000103",
        "isbn": "9783000000103",
        "autor": "Sample, Sophie",
        "titel": "Digitale Bestandsentwicklung",
        "untertitel": "Strategien fuer kleine Bibliotheken",
        "ort": "Wien",
        "verlag": "Akademischer Verlag Wien",
        "jahr": 2022,
        "sprache": "ger",
        "schlagwoerter": ["Bestandsmanagement", "Digitalisierung"],
    },
]


def finde_projektwurzel():
    """Sucht das Verzeichnis, das den Ordner ``assets/data`` enthaelt."""
    start = Path.cwd().resolve()
    for kandidat in [start, *start.parents]:
        if (kandidat / "assets" / "data").is_dir():
            return kandidat
    raise FileNotFoundError("Projektwurzel mit assets/data nicht gefunden.")


def feld_008(jahr, sprache, ort):
    """Vereinfachtes, aber strukturell korrektes 008-Feld (40 Zeichen)."""
    land = LAENDERCODES.get(ort, "   ")
    return f"240101s{jahr:04d}    {land}{' ' * 17}{sprache} d"


def kontrollfeld(record, tag, wert):
    """Haengt ein Kontrollfeld an einen Record."""
    ET.SubElement(record, NS_TAG + "controlfield", {"tag": tag}).text = str(wert)


def datenfeld(record, tag, ind1, ind2, unterfelder):
    """Haengt ein Datenfeld mit Unterfeldern an einen Record."""
    feld = ET.SubElement(
        record, NS_TAG + "datafield", {"tag": tag, "ind1": ind1, "ind2": ind2}
    )
    for code, wert in unterfelder:
        ET.SubElement(feld, NS_TAG + "subfield", {"code": code}).text = str(wert)


def json_zu_record(eintrag):
    """Erzeugt aus einem JSON-Titel ein MARC-XML-Record-Element."""
    record = ET.Element(NS_TAG + "record")
    ET.SubElement(record, NS_TAG + "leader").text = LEADER

    kontrollfeld(record, "001", eintrag["id"])
    kontrollfeld(record, "003", "DE-101")
    kontrollfeld(
        record,
        "008",
        feld_008(eintrag["jahr"], eintrag["sprache"], eintrag["ort"]),
    )

    datenfeld(record, "020", " ", " ", [("a", eintrag["isbn"])])
    datenfeld(record, "041", "0", " ", [("a", eintrag["sprache"])])
    datenfeld(record, "100", "1", " ", [("a", eintrag["autor"])])

    unterfelder_245 = [("a", eintrag["titel"])]
    if eintrag.get("untertitel"):
        unterfelder_245.append(("b", eintrag["untertitel"]))
    datenfeld(record, "245", "1", "0", unterfelder_245)

    datenfeld(
        record,
        "264",
        " ",
        "1",
        [
            ("a", eintrag["ort"]),
            ("b", eintrag["verlag"]),
            ("c", eintrag["jahr"]),
        ],
    )

    for schlagwort in eintrag["schlagwoerter"]:
        datenfeld(record, "650", " ", "7", [("a", schlagwort)])

    return record


def main():
    """Erzeugt die MARC-XML-Datei und prueft die Record-Anzahl."""
    projektwurzel = finde_projektwurzel()
    quelldatei = projektwurzel / "assets" / "data" / QUELLDATEI
    zieldatei = Path(__file__).resolve().parent / ZIELDATEI

    with open(quelldatei, encoding="utf-8") as datei:
        daten = json.load(datei)

    titel = daten["titel"] + ZUSATZ_TITEL
    print(f"Titel aus JSON: {len(daten['titel'])}")
    print(f"Zusatztitel: {len(ZUSATZ_TITEL)}")
    print(f"Zu schreibende Titel: {len(titel)}")

    collection = ET.Element(NS_TAG + "collection")
    for eintrag in titel:
        collection.append(json_zu_record(eintrag))

    baum = ET.ElementTree(collection)
    ET.indent(baum, space="  ")
    baum.write(zieldatei, encoding="utf-8", xml_declaration=True)
    print(f"MARC-XML geschrieben: {zieldatei}")

    # Kontrolle: Datei zuruecklesen und Records zaehlen.
    namensraum = {"m": MARC_NS}
    pruef_records = ET.parse(zieldatei).getroot().findall("m:record", namensraum)
    print(f"Records in der Zieldatei: {len(pruef_records)}")
    if len(pruef_records) == len(titel):
        print("Kontrolle erfolgreich: Anzahl stimmt mit der Titelliste ueberein.")
    else:
        raise SystemExit(
            "FEHLER: Record-Anzahl stimmt nicht mit der Titelliste ueberein."
        )


if __name__ == "__main__":
    main()
