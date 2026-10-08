#! /usr/bin/env python3
"""Musterloesung zur Abschlussaufgabe des Projekts Excel.

Das Skript liest ``assets/data/bibliothek_unsauber.xlsx`` ein, bereinigt den
Datensatz (Duplikate, fehlende Werte, Datentypen, uneinheitliche Kategorien),
gibt Kennzahlen aus, erstellt drei Diagramme und speichert die bereinigten
Daten als Excel-Datei.

Alle Ergebnisse werden neben diesem Skript abgelegt:

* ``bibliothek_sauber.xlsx`` - bereinigter Datensatz
* ``ausleihen_je_standort.png`` - Balkendiagramm
* ``ausleihen_nach_jahr.png`` - Liniendiagramm
* ``verteilung_ausleihzahlen.png`` - Histogramm

Aufruf (aus dem Projektverzeichnis oder aus ``solutions/090/``):

.. code-block:: console

    $ python3 solutions/090/bibliothek_analyse.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # kein Bildschirmfenster im Skriptbetrieb

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

STANDORT_MAPPING = {
    "ZB": "Zentralbibliothek",
    "zentralbibliothek": "Zentralbibliothek",
    "Nord": "Zweigstelle Nord",
    "Zweigstelle Nord": "Zweigstelle Nord",
    "Süd": "Zweigstelle Süd",
    "Zweigstelle Sued": "Zweigstelle Süd",
    "Zweigstelle Süd": "Zweigstelle Süd",
    "West": "Campus West",
    "campus west": "Campus West",
    "Campus West": "Campus West",
    "mag": "Magazin",
    "MAG": "Magazin",
    "Magazin": "Magazin",
    "Zentralbibliothek": "Zentralbibliothek",
}

MEDIUM_MAPPING = {
    "buch": "Buch",
    "Buch": "Buch",
    "eBook": "E-Book",
    "E-Book": "E-Book",
    "zeitschrift": "Zeitschrift",
    "Zeitschr.": "Zeitschrift",
    "Zeitschrift": "Zeitschrift",
    "dvd": "DVD",
    "DVD": "DVD",
    "hoerbuch": "Hörbuch",
    "Hörbuch": "Hörbuch",
}


def finde_projektwurzel():
    """Sucht das Verzeichnis, das den Ordner ``assets/data`` enthaelt."""
    start = Path.cwd().resolve()
    for kandidat in [start, *start.parents]:
        if (kandidat / "assets" / "data").is_dir():
            return kandidat
    raise FileNotFoundError("Projektwurzel mit assets/data nicht gefunden.")


def parse_deutsche_zahl(serie):
    """Wandelt Text mit deutschem Tausenderpunkt in Zahlen um."""
    text = serie.astype("string").str.strip()
    hat_tausenderpunkt = text.str.match(r"^-?\d{1,3}(\.\d{3})+$", na=False)
    text = text.where(~hat_tausenderpunkt, text.str.replace(".", "", regex=False))
    return pd.to_numeric(text, errors="coerce")


def bereinige(pfad):
    """Liest die unsaubere Excel-Datei ein und gibt saubere Daten zurueck."""
    df = pd.read_excel(pfad, sheet_name="Ausleihen")
    print(f"Zeilen vor der Bereinigung: {len(df)}")

    df = df.drop_duplicates().reset_index(drop=True)
    print(f"Zeilen nach Duplikatentfernung: {len(df)}")

    df["Standort"] = df["Standort"].str.strip().map(STANDORT_MAPPING)
    df["Medium"] = df["Medium"].str.strip().map(MEDIUM_MAPPING)

    df["Erscheinungsjahr"] = pd.to_numeric(
        df["Erscheinungsjahr"].astype("string").str.strip(), errors="coerce"
    )
    df["Ausleihzahlen"] = parse_deutsche_zahl(df["Ausleihzahlen"])
    df["Zugangsdatum"] = pd.to_datetime(
        df["Zugangsdatum"], format="mixed", dayfirst=True, errors="coerce"
    )

    df = df.rename(columns={
        "Titel": "titel",
        "Autor*in": "autor",
        "Erscheinungsjahr": "jahr",
        "Ausleihzahlen": "ausleihen",
        "Standort": "standort",
        "Medium": "medium",
        "Zugangsdatum": "zugang",
    })

    df = df.dropna(subset=["titel", "autor"]).reset_index(drop=True)
    print(f"Zeilen nach der vollstaendigen Bereinigung: {len(df)}")
    return df


def kennzahlen_ausgeben(bibliothek):
    """Gibt die geforderten Kennzahlen auf der Kommandozeile aus."""
    print("\nKennzahlen je Standort")
    print("----------------------")
    print(
        bibliothek.groupby("standort")["ausleihen"]
        .agg(["count", "sum", "mean", "median"])
        .round(1)
    )

    print("\nVerteilung der Medienarten")
    print("--------------------------")
    print(bibliothek["medium"].value_counts())

    print("\nVerteilung der Standorte")
    print("------------------------")
    print(bibliothek["standort"].value_counts())

    print("\nTop 5 der ausleihstaerksten Titel")
    print("---------------------------------")
    print(
        bibliothek.nlargest(5, "ausleihen")[
            ["titel", "standort", "medium", "ausleihen"]
        ]
    )


def diagramme_erzeugen(bibliothek, zielordner):
    """Erstellt und speichert die drei geforderten Diagramme."""
    plt.rcParams["figure.figsize"] = (8, 5)

    ausleihen_standort = (
        bibliothek.groupby("standort")["ausleihen"].sum().sort_values(ascending=False)
    )
    fig, ax = plt.subplots()
    ax.bar(ausleihen_standort.index, ausleihen_standort.values, color="#2b6cb0")
    ax.set_title("Ausleihen je Standort")
    ax.set_xlabel("Standort")
    ax.set_ylabel("Ausleihen (Summe)")
    fig.tight_layout()
    fig.savefig(zielordner / "ausleihen_je_standort.png", dpi=150)
    plt.close(fig)

    ausleihen_jahr = bibliothek.groupby("jahr")["ausleihen"].sum().sort_index()
    fig, ax = plt.subplots()
    ax.plot(ausleihen_jahr.index, ausleihen_jahr.values, marker="o", color="#c05621")
    ax.set_title("Ausleihen nach Erscheinungsjahr")
    ax.set_xlabel("Erscheinungsjahr")
    ax.set_ylabel("Ausleihen (Summe)")
    fig.tight_layout()
    fig.savefig(zielordner / "ausleihen_nach_jahr.png", dpi=150)
    plt.close(fig)

    werte = bibliothek["ausleihen"].dropna()
    fig, ax = plt.subplots()
    ax.hist(werte, bins=15, color="#2f855a", edgecolor="white")
    ax.set_title("Verteilung der Ausleihzahlen")
    ax.set_xlabel("Ausleihzahlen je Titel")
    ax.set_ylabel("Häufigkeit (Anzahl Titel)")
    fig.tight_layout()
    fig.savefig(zielordner / "verteilung_ausleihzahlen.png", dpi=150)
    plt.close(fig)

    print("\nDiagramme gespeichert in:", zielordner)


def main():
    """Fuehrt Bereinigung, Statistik, Visualisierung und Export aus."""
    projektwurzel = finde_projektwurzel()
    quelldatei = projektwurzel / "assets" / "data" / "bibliothek_unsauber.xlsx"
    zielordner = Path(__file__).resolve().parent

    bibliothek = bereinige(quelldatei)
    kennzahlen_ausgeben(bibliothek)
    diagramme_erzeugen(bibliothek, zielordner)

    zieldatei = zielordner / "bibliothek_sauber.xlsx"
    bibliothek.to_excel(zieldatei, index=False)
    print("Bereinigte Daten gespeichert:", zieldatei)


if __name__ == "__main__":
    main()
