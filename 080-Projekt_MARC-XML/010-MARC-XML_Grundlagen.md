---
short_title: MARC-XML-Grundlagen
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# MARC-XML: Grundlagen

```{caution} Work In Progress
Diese Inhalte sind noch in Bearbeitung.
```

Bevor wir {term}`MARC-XML` mit {term}`Python` verarbeiten, klären wir in diesem Kapitel, was
MARC überhaupt ist, wie ein Record aufgebaut ist und wie aus dem klassischen
MARC-Format eine XML-Repräsentation wird.

```{seealso} Vorwissen
:icon: false

Für dieses Kapitel sind Grundkenntnisse zu Dateiformaten und zum Umgang mit
Textdateien hilfreich. Diese haben Sie im
[Projekt CSV I](../040-Projekt_CSV_I/000-Einleitung.md) und im
[Projekt CSV II](../070-Projekt_CSV_II/000-Einleitung.md) erworben.
```

## Was ist MARC?

**MARC** steht für _MAchine-Readable Cataloging_ (maschinenlesbare
Katalogisierung) und ist ein Standard für den Austausch bibliografischer Daten.
Er wurde in den 1960er Jahren an der Library of Congress entwickelt und wird
heute in der Variante **{term}`MARC 21`** weltweit in Bibliotheken eingesetzt.

Ein **Record** (Datensatz) beschreibt eine Ressource – meist ein Buch, eine
Zeitschrift oder eine elektronische Ressource. Jeder Record besteht aus einer
festen Anzahl durchnummerierter **Felder** (Fields), die wiederum
**Unterfelder** (Subfields) enthalten. Das klassische MARC-Austauschformat ist
ein kompaktes Binärformat (ISO 2709); für Menschen und moderne Software ist die
XML-Variante **MARC-XML** deutlich angenehmer.

## Felder und Unterfelder

Jedes Feld wird über einen dreistelligen **Tag** (Feldnummer) angesprochen. Man
unterscheidet zwei Arten:

- **Kontrollfelder** (Control Fields, Tags `00X`) enthalten keinen Unterfeldcode,
  sondern einen einzelnen Wert, z. B. `001` (Record-ID) oder `008`
  (Fixfeld mit codierten Angaben wie Erscheinungsjahr und Sprache).
- **Datenfelder** (Data Fields, Tags ab `010`) enthalten **Unterfelder**. Jedes
  Unterfeld beginnt mit einem `$`-Code, z. B. `$a` (Titel), `$b` (Zusatz zum
  Titel) oder `$c` (Erscheinungsjahr).

Datenfelder tragen zusätzlich zwei **Indikatoren** (Indicators) `ind1` und
`ind2`. Sie steuern die Interpretation des Feldes, z. B. ob ein Titel mit einem
Artikel beginnt oder wie ein Name einzuordnen ist. Ein Leerzeichen als
Indikator bedeutet „nicht definiert“ bzw. „keine Aussage“.

Die folgende Tabelle zeigt die Felder, die wir in diesem Projekt verwenden:

| Tag   | Bedeutung                                | Beispiel-Unterfelder                   |
| ----- | ---------------------------------------- | -------------------------------------- |
| `001` | Record-ID (Kontrollfeld)                 | –                                      |
| `008` | Fixfeld mit codierten Angaben            | Erscheinungsjahr, Sprache              |
| `020` | Internationale Standardbuchnummer (ISBN) | `$a`                                   |
| `041` | Sprachcode des Inhalts                   | `$a` (ISO 639-2, z. B. `ger`)          |
| `100` | Hauptverantwortlichkeit (Person)         | `$a` (Name)                            |
| `245` | Titel und Verantwortlichkeitsangabe      | `$a` (Titel), `$b` (Untertitel)        |
| `264` | Erscheinungsangaben (RDA)                | `$a` (Ort), `$b` (Verlag), `$c` (Jahr) |
| `260` | Erscheinungsangaben (älteres Format)     | `$a`, `$b`, `$c`                       |
| `650` | Schlagwort (Sachschlagwort)              | `$a`                                   |

```{note} 260 oder 264?
Das Feld `260` stammt aus der älteren Katalogisierung (AACR2), das Feld `264`
wurde mit dem Regelwerk **RDA** (_Resource Description and Access_) eingeführt.
In modernen Datensätzen findet man häufig `264`, in älteren Beständen noch
`260`. Beim Einlesen sollten Sie beide Felder berücksichtigen.
```

## Der Leader

Jeder Record beginnt mit einem **Leader** (Feldkopf). Er ist immer genau
24 Zeichen lang und enthält an festen Positionen codierte Angaben, z. B.:

- Position 5: Status des Records (`n` = neu)
- Position 6: Art der Ressource (`a` = Text)
- Position 7: bibliografische Ebene (`m` = Monografie)

Ein typischer Leader sieht so aus:

```text
00000nam a2200000 a 4500
```

Die Stellen `00000` am Anfang enthalten bei Bedarf die Länge des Records; in
MARC-XML darf das Feld auch als Platzhalter (mit Nullen) gefüllt sein.

## Von MARC zu MARC-XML

MARC-XML bildet einen Record eins zu eins als XML-Elemente ab. Die folgende
Übersicht zeigt die Zuordnung:

| MARC-Konzept         | XML-Element                             |
| -------------------- | --------------------------------------- |
| Sammlung von Records | `<collection>`                          |
| einzelner Record     | `<record>`                              |
| Feldkopf             | `<leader>`                              |
| Kontrollfeld         | `<controlfield tag="…">`                |
| Datenfeld            | `<datafield tag="…" ind1="…" ind2="…">` |
| Unterfeld            | `<subfield code="…">`                   |

Schauen wir uns einen vollständigen Record aus unseren Beispieldaten an:

```xml
<record>
  <leader>00000nam a2200000 a 4500</leader>
  <controlfield tag="001">000000001</controlfield>
  <controlfield tag="003">DE-101</controlfield>
  <controlfield tag="005">20240101120000.0</controlfield>
  <controlfield tag="008">240101s2021    gw                  ger d</controlfield>
  <datafield tag="020" ind1=" " ind2=" ">
    <subfield code="a">9783110470017</subfield>
  </datafield>
  <datafield tag="041" ind1="0" ind2=" ">
    <subfield code="a">ger</subfield>
  </datafield>
  <datafield tag="100" ind1="1" ind2=" ">
    <subfield code="a">Keller, Miriam</subfield>
  </datafield>
  <datafield tag="245" ind1="1" ind2="0">
    <subfield code="a">Datenkuration in wissenschaftlichen Bibliotheken :</subfield>
    <subfield code="b">Praktiken, Werkzeuge und Standards</subfield>
  </datafield>
  <datafield tag="264" ind1=" " ind2="1">
    <subfield code="a">Berlin</subfield>
    <subfield code="b">Wissenschaftsverlag Berlin</subfield>
    <subfield code="c">2021</subfield>
  </datafield>
  <datafield tag="650" ind1=" " ind2="7">
    <subfield code="a">Metadaten</subfield>
  </datafield>
</record>
```

## Namensräume (Namespaces)

MARC-XML-Elemente gehören zu einem **Namensraum** (Namespace). Der Standard-
Namensraum lautet:

```text
http://www.loc.gov/MARC21/slim
```

Er wird über das Attribut `xmlns` am Wurzelelement festgelegt:

```xml
<collection xmlns="http://www.loc.gov/MARC21/slim">
```

Der Namensraum verhindert, dass Elemente wie `<record>` oder `<leader>` mit
gleichnamigen Elementen aus anderen XML-Formaten verwechselt werden. Für uns hat
das eine wichtige Konsequenz: Beim Suchen nach Elementen mit
`xml.etree.ElementTree` müssen wir den Namensraum mitangeben, z. B. mit der
Schreibweise `{http://www.loc.gov/MARC21/slim}record`. Dazu später mehr.

```{hint} Warum überhaupt XML?
{term}`XML` ist ein weit verbreitetes Format für den strukturierten Datenaustausch.
Bibliotheksverbünde, die Deutsche Nationalbibliothek (DNB) und Repositorien
liefern Metadaten häufig als XML – sei es über **OAI-PMH** (Protokoll zum
Ernten von Metadaten) oder **SRU** (Suchschnittstelle). Wer MARC-XML lesen und
schreiben kann, beherrscht also eine zentrale Schnittstelle des
Bibliothekswesens.
```

## Bibliothekarischer Kontext

MARC-Daten entstehen in der **Katalogisierung** (auch „Erschließung“ genannt).
Fachkräfte erfassen Titel in einem Bibliothekssystem, vergeben Schlagwörter und
Normdaten (z. B. Personennamen) und exportieren die Records anschließend in
MARC. Über Katalogisierungsverbünde werden die Daten zwischen Bibliotheken
ausgetauscht.

Zentrale Anwendungsfälle für dieses Kapitel sind:

- **Import und Export**: Daten aus einem Lieferanten- oder Verbundsystem in ein
  eigenes System überführen.
- **Transformation**: Zwischenformate wie {term}`JSON`, {term}`CSV` oder {term}`BibTeX` ineinander
  umwandeln.
- **Qualitätskontrolle**: Records filtern, fehlende Felder finden, Statistiken
  erheben.
- **Import-Vorbereitung**: Aus maschinenlesbaren Daten valide MARC-XML-Dateien
  erzeugen, die ein Bibliothekssystem einlesen kann.

## MARC und JSON im Vergleich

Unsere Quelldaten liegen als JSON vor. Beide Formate speichern strukturierte
Daten, unterscheiden sich aber in der Darstellung:

| Aspekt       | JSON                                | MARC-XML                            |
| ------------ | ----------------------------------- | ----------------------------------- |
| Struktur     | Objekte (`{}`) und Listen (`[]`)    | Elemente mit Tags                   |
| Feldnamen    | frei wählbar, sprechend (`title`)   | numerische Tags (`245`)             |
| Wiederholung | Listen                              | mehrfache Elemente mit gleichem Tag |
| Metadaten    | Kommentare/`metadata`-Felder üblich | codierte Fixfelder (`008`)          |
| Verwendung   | Web-APIs, Konfiguration             | Bibliothekssysteme, Austausch       |

Der Transformationsweg in diesem Projekt führt also von sprechenden JSON-Feldern
über ein festes Mapping zu den numerischen MARC-Tags.

## Ausblick: `pymarc`

Alle Beispiele dieses Kapitels nutzen nur die **Standardbibliothek**
(`xml.etree.ElementTree`). Das ist bewusst so gewählt: Sie lernen die
XML-Grundlagen und erzeugen keine zusätzlichen Abhängigkeiten.

In der Praxis greifen viele Bibliotheken zum {term}`Paket` **`pymarc`**, das die
MARC-Logik direkt kapselt und auch das binäre MARC-Format (ISO 2709) lesen und
schreiben kann. Der Aufruf ist deutlich kompakter, z. B.:

```python
# Nur zur Illustration – in diesem Kurs nicht ausgeführt.
from pymarc import MARCReader

with open("beispiel.mrc", "rb") as datei:
    for record in MARCReader(datei):
        print(record.title)
```

`pymarc` gehört nicht zu den Abhängigkeiten dieses Kurses. Wenn Sie später
regelmäßig mit MARC arbeiten, lohnt sich ein Blick in die offizielle
Dokumentation (siehe unten).

```{seealso} Weiterführende Ressourcen
:icon: false

- Library of Congress: [MARC 21 Format for Bibliographic Data](https://www.loc.gov/marc/bibliographic/) – die offizielle Feldübersicht.
- Library of Congress: [MARCXML](https://www.loc.gov/marc/marcxml.html) – Spezifikation und Beispiele.
- Deutsche Nationalbibliothek: [MARC 21](https://www.dnb.de/DE/Professionell/Standardisierung/Formate/MARC21/marc21_node.html) – Anwendung im deutschsprachigen Raum.
- Python-Dokumentation: [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html).
- `pymarc`: [Dokumentation](https://pymarc.readthedocs.io/) – komfortable MARC-Bibliothek für Python.
```
