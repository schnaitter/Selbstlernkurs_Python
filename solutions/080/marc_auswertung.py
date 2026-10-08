#! /usr/bin/env python3
"""Musterloesung zu Aufgabe 1 des Projekts MARC-XML.

Das Skript liest ``assets/data/beispieldaten.marcxml`` mit der
Standardbibliothek ``xml.etree.ElementTree`` ein, wandelt jeden Record in ein
Dictionary um und filtert die Titel, die deutschsprachig (``ger``) sind oder
das Schlagwort ``Metadaten`` tragen. Fuer die Treffer wird eine Statistik
ausgegeben und eine BibTeX-Datei geschrieben.

Aufruf (aus dem Projektverzeichnis oder aus ``solutions/080/``):

.. code-block:: console

    $ python3 solutions/080/marc_auswertung.py

Die erzeugte Datei ``aufgabe.bib`` liegt neben diesem Skript.
"""

from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

MARC_NS = "http://www.loc.gov/MARC21/slim"
NAMENSRAUM = {"m": MARC_NS}

QUELLDATEI = "beispieldaten.marcxml"
ZIELDATEI = "aufgabe.bib"


def finde_projektwurzel():
    """Sucht das Verzeichnis, das den Ordner ``assets/data`` enthaelt."""
    start = Path.cwd().resolve()
    for kandidat in [start, *start.parents]:
        if (kandidat / "assets" / "data").is_dir():
            return kandidat
    raise FileNotFoundError("Projektwurzel mit assets/data nicht gefunden.")


def kontrolle(record, tag):
    """Text eines Kontrollfelds (oder ``None``)."""
    feld = record.find(f"m:controlfield[@tag='{tag}']", NAMENSRAUM)
    return feld.text if feld is not None else None


def unterfeld(record, tag, code):
    """Erstes Unterfeld mit diesem Code im ersten Datenfeld mit diesem Tag."""
    feld = record.find(f"m:datafield[@tag='{tag}']", NAMENSRAUM)
    if feld is None:
        return None
    sub = feld.find(f"m:subfield[@code='{code}']", NAMENSRAUM)
    return sub.text if sub is not None else None


def alle_unterfelder(record, tag, code):
    """Alle Unterfelder mit diesem Code aus allen Datenfeldern mit diesem Tag."""
    return [
        sub.text
        for feld in record.findall(f"m:datafield[@tag='{tag}']", NAMENSRAUM)
        for sub in feld.findall(f"m:subfield[@code='{code}']", NAMENSRAUM)
    ]


def als_dict(record):
    """Wandelt einen MARC-Record in ein Dictionary mit sprechenden Schluesseln."""
    return {
        "id": kontrolle(record, "001"),
        "isbn": unterfeld(record, "020", "a"),
        "sprache": unterfeld(record, "041", "a"),
        "autor": unterfeld(record, "100", "a"),
        "titel": unterfeld(record, "245", "a"),
        "untertitel": unterfeld(record, "245", "b"),
        "ort": unterfeld(record, "264", "a"),
        "verlag": unterfeld(record, "264", "b"),
        "jahr": unterfeld(record, "264", "c"),
        "schlagwoerter": alle_unterfelder(record, "650", "a"),
    }


def einlesen(pfad):
    """Liest eine MARC-XML-Datei und gibt eine Liste von Dictionaries zurueck."""
    records = ET.parse(pfad).getroot().findall("m:record", NAMENSRAUM)
    return [als_dict(record) for record in records]


def filtern(titel_liste):
    """Titel, die deutschsprachig sind oder das Schlagwort ``Metadaten`` tragen."""
    return [
        titel
        for titel in titel_liste
        if titel["sprache"] == "ger" or "Metadaten" in titel["schlagwoerter"]
    ]


def statistik_ausgeben(titel_liste, treffer):
    """Gibt Sprachverteilung, Jahrespanne und Gesamtzahl aus."""
    sprachen = Counter(titel["sprache"] for titel in titel_liste)
    jahre = [int(titel["jahr"]) for titel in titel_liste if titel["jahr"]]

    print("\nStatistik")
    print("--------")
    print("Titel je Sprache:")
    for sprache, anzahl in sorted(sprachen.items()):
        print(f"  {sprache}: {anzahl}")
    print(f"Fruehestes Jahr: {min(jahre)}")
    print(f"Spaetestes Jahr: {max(jahre)}")
    print(f"Gesamtzahl der Titel: {len(titel_liste)}")
    print(f"Gefilterte Titel: {len(treffer)}")


def bibtex_schluessel(eintrag):
    """Erzeugt einen eindeutigen BibTeX-Schluessel."""
    nachname = eintrag["autor"].split(",")[0].lower()
    erstes_wort = eintrag["titel"].split()[0].lower()
    return f"{nachname}{eintrag['jahr']}{erstes_wort}"


def maskiere(text):
    """Maskiert Sonderzeichen fuer BibTeX."""
    for zeichen in "&%$#_{}":
        text = text.replace(zeichen, "\\" + zeichen)
    return text


def als_bibtex(eintrag):
    """Erzeugt einen BibTeX-Eintrag vom Typ ``@book``."""
    titel = eintrag["titel"].rstrip(" :")
    if eintrag["untertitel"]:
        titel = f"{titel}: {eintrag['untertitel']}"

    felder = [
        ("author", eintrag["autor"]),
        ("title", titel),
        ("year", eintrag["jahr"]),
        ("publisher", eintrag["verlag"]),
        ("address", eintrag["ort"]),
        ("isbn", eintrag["isbn"]),
        ("keywords", ", ".join(eintrag["schlagwoerter"])),
    ]

    zeilen = [f"@book{{{bibtex_schluessel(eintrag)},"]
    for name, wert in felder:
        zeilen.append(f"  {name} = {{{maskiere(str(wert))}}},")
    zeilen.append("}")
    return "\n".join(zeilen)


def exportieren(treffer, zieldatei):
    """Schreibt die Treffer als BibTeX-Datei."""
    eintraege = [als_bibtex(eintrag) for eintrag in treffer]
    inhalt = "\n\n".join(eintraege) + "\n"
    zieldatei.write_text(inhalt, encoding="utf-8")
    print(f"\nBibTeX geschrieben: {zieldatei}")
    print(f"Eintraege: {len(eintraege)}")


def main():
    """Fuehrt Filterung, Statistik und BibTeX-Export aus."""
    projektwurzel = finde_projektwurzel()
    quelldatei = projektwurzel / "assets" / "data" / QUELLDATEI
    zieldatei = Path(__file__).resolve().parent / ZIELDATEI

    titel_liste = einlesen(quelldatei)
    treffer = filtern(titel_liste)

    print(f"Treffer ({len(treffer)}):")
    for titel in treffer:
        print(
            f"{titel['jahr']} | {titel['autor']} | "
            f"{titel['titel']} | {titel['isbn']}"
        )

    statistik_ausgeben(titel_liste, treffer)
    exportieren(treffer, zieldatei)


if __name__ == "__main__":
    main()
