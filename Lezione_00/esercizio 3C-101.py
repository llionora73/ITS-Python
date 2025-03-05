# esercizio 3C-10

data = []  

for i in range(5):
    giorno = int(input("Inserisci giorno: "))
    mese = int(input("Inserisci mese: "))
    data.append((giorno, mese))

for dati in data:
    giorno, mese = dati

    match (giorno, mese):
        case (1, 1):
            print("Capodanno") 
        case (14, 2):
            print("San Valentino")  
        case (2, 6):
            print("Festa della Repubblica Italiana")  
        case (15, 8):
            print("Ferragosto")  
        case (31, 10):
            print("Halloween")  
        case (25, 12):
            print("Natale") 
        case _:
            print("Nessuna festività importante in questa data")