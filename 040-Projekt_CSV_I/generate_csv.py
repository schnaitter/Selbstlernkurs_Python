import csv
import random

import numpy as np

# Partially generated via Claude

# Echte Bücher mit ISBN-13, Autor*innen und Erscheinungsjahr
books = [
    ("9783518587010", "Harari, Yuval Noah", 2013, "Eine kurze Geschichte der Menschheit"),
    ("9783446254251", "Kahneman, Daniel", 2012, "Schnelles Denken, langsames Denken"),
    ("9783596196036", "Kafka, Franz", 1925, "Der Prozess"),
    ("9783518465189", "Butler, Judith", 1990, "Das Unbehagen der Geschlechter"),
    ("9783518587287", "Han, Byung-Chul", 2016, "Die Austreibung des Anderen"),
    ("9783518465905", "Foucault, Michel", 1975, "Überwachen und Strafen"),
    ("9783518587157", "Latour, Bruno", 2017, "Kampf um Gaia"),
    ("9780141439518", "Orwell, George", 1949, "Nineteen Eighty-Four"),
    ("9780141182605", "Austen, Jane", 1813, "Pride and Prejudice"),
    ("9780141439600", "Dickens, Charles", 1861, "Great Expectations"),
    ("9780143058144", "Morrison, Toni", 1987, "Beloved"),
    ("9780374533557", "Knausgård, Karl Ove", 2009, "My Struggle: Book 1"),
    ("9780143124276", "Rushdie, Salman", 1981, "Midnight's Children"),
    ("9783518465172", "Adorno, Theodor W.", 1951, "Minima Moralia"),
    ("9783518293447", "Habermas, Jürgen", 1981, "Theorie des kommunikativen Handelns"),
    ("9783518587164", "Sloterdijk, Peter", 1998, "Sphären I"),
    ("9780241951446", "Murakami, Haruki", 1984, "Norwegian Wood"),
    ("9780374532741", "Ferrante, Elena", 2011, "My Brilliant Friend"),
    ("9783518587119", "Mbembe, Achille", 2016, "Politik der Feindschaft"),
    ("9783518587201", "Rosa, Hartmut", 2016, "Resonanz"),
    ("9783518465196", "Arendt, Hannah", 1958, "The Human Condition"),
    ("9783518587225", "Bauman, Zygmunt", 2000, "Liquid Modernity"),
    ("9780141439471", "Woolf, Virginia", 1927, "To the Lighthouse"),
    ("9780141185422", "Joyce, James", 1922, "Ulysses"),
    ("9783518587249", "Boltanski, Luc", 1999, "Der neue Geist des Kapitalismus"),
    ("9783518293454", "Luhmann, Niklas", 1984, "Soziale Systeme"),
    ("9780374530532", "Atwood, Margaret", 1985, "The Handmaid's Tale"),
    ("9780141439556", "Brontë, Charlotte", 1847, "Jane Eyre"),
    ("9780141439587", "Eliot, George", 1871, "Middlemarch"),
    (
        "9783518465202",
        "Benjamin, Walter",
        1936,
        "Das Kunstwerk im Zeitalter seiner technischen Reproduzierbarkeit",
    ),
]


dataset = []
for year in range(2020, 2026):
    dataset_year = []
    random.shuffle(books)
    for i, book in enumerate(books):
        dataset_year.append(
            {
                "isbn": book[0],
                "author": book[1],
                "year": book[2],
                "title": book[3],
                "sales_year": year,
            }
        )

    # Generiere Power-Law-verteilte Kaufzahlen (Pareto-Verteilung)
    # P(x) ~ x^(-alpha), typisch alpha zwischen 2 und 3 für long-tail
    alpha = 2.5  # Pareto-Exponent
    x_min = 5  # Minimale Verkaufszahl

    # Pareto-Verteilung mit numpy
    sales = (np.random.pareto(alpha - 1, len(books)) + 1) * x_min
    sales = np.round(sales).astype(int)
    sales = np.sort(sales)[::-1]  # Absteigend sortieren

    # Füge Verkaufszahlen hinzu
    for i, row in enumerate(dataset_year):
        row["sales"] = int(sales[i])

    dataset += dataset_year

# CSV-Datei schreiben
with open("books_powerlaw_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f, fieldnames=["isbn", "author", "year", "title", "sales_year", "sales"]
    )
    writer.writeheader()
    writer.writerows(dataset)

print(f"\n✓ CSV-Datei gespeichert: books_powerlaw_dataset.csv")
