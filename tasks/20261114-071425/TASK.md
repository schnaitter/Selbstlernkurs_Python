# Build verändert versionierte Datei assets/data/bibliothek_sauber.xlsx

- STATUS: CLOSED
- PRIORITY: 20
- TAGS: 090-Projekt_Excel,build

## Problem

[`090-Projekt_Excel/020-Datenbereinigen.ipynb`](../../090-Projekt_Excel/020-Datenbereinigen.ipynb)
schreibt in der letzten Code-Zelle:

```python
bibliothek.to_excel("../assets/data/bibliothek_sauber.xlsx", index=False)
```

Die Datei [`assets/data/bibliothek_sauber.xlsx`](../../assets/data/bibliothek_sauber.xlsx)
ist versioniert und in `myst.yml` unter `static_files` eingetragen, wird also auf
der Kurs-Website als Download ausgeliefert.

Weil `jupyter book build --execute --all` alle Notebooks ausführt, wird die
Datei bei **jedem** Build neu geschrieben. Ergebnis: Das Arbeitsverzeichnis ist
nach jedem Build schmutzig, und jeder Commit enthält eine Änderung an einer
Binärdatei, die inhaltlich nichts bedeutet.

## Analyse

Diff gegen `HEAD` (geprüft am 2026-11-14, nach dem Dependency-Upgrade):

```console
$ git diff --stat assets/data/bibliothek_sauber.xlsx
 assets/data/bibliothek_sauber.xlsx | Bin 7655 -> 7654 bytes
```

Entpackt unterscheiden sich die beiden XLSX nur in `docProps/core.xml`:

```diff
-<dcterms:created>2026-10-08T06:42:54Z</dcterms:created>
-<dcterms:modified>2026-10-08T06:42:54Z</dcterms:modified>
+<dcterms:created>2026-11-13T18:20:01Z</dcterms:created>
+<dcterms:modified>2026-11-13T18:20:01Z</dcterms:modified>
```

`openpyxl` setzt beim Speichern den aktuellen Zeitstempel. Die Tabellendaten
selbst sind byte-identisch. Es gehen also keine Inhalte verloren — die
Änderung ist reines Metadaten-Rauschen.

## Mögliche Lösungen

1. **Zeitstempel normalisieren (deterministisch):** Nach `to_excel` die
   `docProps/core.xml` im Zip mit einem festen Datum überschreiben. Die Datei
   wird dann bei gleichem Inhalt byte-identisch und erzeugt keinen Diff mehr.
2. **Nur bei Inhaltsänderung schreiben:** Vor dem Speichern prüfen, ob sich die
   Daten gegenüber der vorhandenen Datei geändert haben; sonst nicht schreiben.
3. **Aus der Versionierung nehmen:** Datei aus Git entfernen und im Build (bzw.
   Deploy) erzeugen. Sie wird für `static_files` erst zur Build-Zeit gebraucht
   und existiert dann bereits — setzt aber voraus, dass jeder Build die
   Notebooks ausführt.
4. `git update-index --skip-worktree` — löst das Problem nur lokal und nicht in
   CI, daher keine echte Lösung.

## Umsetzung (2026-11-24)

Lösung 1 (Zeitstempel normalisieren) im Notebook umgesetzt. Wichtig: Die
Analyse oben übersah eine zweite Rauschquelle – neben `docProps/core.xml`
stempelt `openpyxl` auch die **Zip-Einträge** mit der aktuellen Uhrzeit
(`ZipFile.writestr` mit String-Namen). Die letzte Code-Zelle schreibt die
Datei deshalb nach `to_excel` neu und setzt beide Zeitstempelarten auf
feste Werte (2026-01-01). Der Markdown-Text erklärt die Stolperfalle als
Beispiel für reproduzierbare Builds.

Verifikation: Notebook zweimal mit `nbconvert --execute` ausgeführt (3 s
Abstand) → Datei byte-identisch (SHA-256 gleich). Dateninhalt per
`pandas.read_excel(...).equals(...)` gegen `HEAD` geprüft: identisch,
53 Zeilen. `static_files` unverändert; die versionierte Datei wurde einmalig
mit normalisierten Zeitstempeln neu erzeugt.

## Checkliste

- [x] Reproduziert: Notebook ausführen, Datei zeigt sich als geändert
- [x] Lösung gewählt (siehe oben) und im Notebook/Post-Processing umgesetzt
- [x] Zwei aufeinanderfolgende Builds erzeugen keinen Diff mehr
      (nachgewiesen über zwei Notebook-Ausführungen, s. o.)
- [x] Datei ist weiterhin über die Kurs-Website abrufbar (`static_files`)
- [x] Kapiteltext in `020-Datenbereinigen.ipynb` prüfen, falls sich der Pfad
      oder das Speicherverhalten ändert
