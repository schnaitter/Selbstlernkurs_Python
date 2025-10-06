def ausleihe_überprüfen(kontostand, aktuell):
    summe = kontostand + aktuell # in einer Funktion können Sie Variablen erstellen um Zwischenergebnisse zu speichern
    if summe > 15:
        print(f"""Sie haben bereits {kontostand} Bücher ausgeliehen.
        Wenn Sie {aktuell} Bücher ausleihen würden, kämen Sie über die Grenze von
        15 Büchern.
        
        Sie können aktuell maximal {15 - kontostand} weitere Bücher ausleihen.""")
        
        return kontostand # Eine Ausleihe war nicht möglich, es wird der alte Kontostand zurückgegeben.
        
    elif summe >= 10: 
        print(f"Ihr neuer Kontostand: {summe} Bücher.")
        
        return summe # Die Ausleihe war erfolgreich und der neue Kontostand wird zurückgegeben.
        
    else:
        print("Ausleihe erfolgreich.")
        
        return summe # Auch hier war die Ausleihe erfolgreich und es wir der neue Kontostand zurückgegeben.