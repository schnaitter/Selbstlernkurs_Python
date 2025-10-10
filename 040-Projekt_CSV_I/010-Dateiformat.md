---
short_title: CSV
numbering:
    heading_1: true
    heading_2: true
    title: true
---

# Dateiformat CSV

Das Dateiformat CSV (_comma separated values_, `.csv`) ist ein gängiges Format
für den Austausch tabellarischer Daten. Wie der Name sagt nutzt eine
"klassische" CSV-Datei Kommata für die Trennung von einzelnen Werten (Spalten).
Oft wird aber auch ein Semikolon genutzt.

## Struktur einer CSV-Datei

Eine CSV-Datei sieht typischerweise so aus:

Alle Werte in der CSV-Datei werden als Text (Zeichenkette, String)
abgespeichert und auch so eingelesen. Sollen manche Werte/Spalten bspw. als
Zahl interpretiert werden, so muss diese Transformation explizit durchgeführt
werden.

Ein Datensatz entspricht in einer CSV-Datei immer einer Zeile in der Datei. Die
Reihenfolge der Zeilen ist normalerweise nicht sinntragend, d.h. wenn ein
anderer Datensatz "referenziert" werden soll, dann sollte dies über eindeutige
IDs in Schlüsselspalten geschehen und nicht über einen Zeilen-Index.

Zellen können Leerzeichen enthalten. Zellen können optional mit doppelten
Anführungsstrichen umschlossen sein. Dann können auch Zeichen wie `,` oder `\r`
(CR, Carriage Return),`\n` (LF, Line Feed, Newline) in der Zelle stehen. Manche
Programme können jedoch nicht mit solchen Dateien umgehen, weshalb dies nicht
unbedingt empfohlen wird. Dies ist auch einer der Gründe, warum häufig ein
Semikolon für die Spalten-Trennung genutzt wird. Das Semikolon wird innerhalb
typischer Daten viel seltener genutzt als das Komma.

## Beispieldateien

```csv
id, family name, given name, birthdate
0, musterfrau, martha, 1.2.2003
1, müller, kim, 1999-8-7
2, 王, 祖寇, February 21, 2005
```

```csv
index;date;time;temp
2;2025-10-10;11:51:02;21.4
3;2025-10-10;11:51:12;21.5
6;2025-10-10;11:57:05;21.1
7;2025-10-10;11:57:20;21.6
```

```csv
"Matrikel Nr.", "Nachname", "Vorname", "Adresse", "HZB"
"123456", "Aa-Bb", "Ccc", "Muster Str. 7b", "2,4"
"234567", "Aa", "Ddd", "Deppendorf 12", "1,0"
"345678", "Bb", "Eee", "Alexanderplatz 4", "1,3"

```

Es gibt auch das verwandte Dateiformat TSV (_tabulator separated values_,
`.tsv`), welches einen Tabulator (`\t`) als Trennzeichen nutzt.

```tsv
Matrikel Nr.\tNachname\tVorname\tAdresse\tHZB
123456\tAa-Bb\tCcc\tMuster Str. 7b\t2,4
234567\tAa\tDdd\tDeppendorf 12\t1,0
345678\tBb\tEee\tAlexanderplatz 4\t1,3

```
