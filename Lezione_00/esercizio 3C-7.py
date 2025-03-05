# esercizio 3C-7

TESTA: str= []
CROCE:  str= []
risultati: str= []

lancio = int(input("Quanti lanci vuoi inserire? "))

for i in range(lancio):
    item = input(f"Inserisci 't' o 'T' se è uscito 'testa', mentre inserisci 'c' o 'C' se è uscito 'croce': ")

    match item:

         case 't' | 'T':  
            TESTA.append(item)
        case 'c' | 'C':  
            CROCE.append(item)
        case _:  
            print("Inserimento non valido. Usa 't' per testa o 'c' per croce.")

total = len(TESTA) + len(CROCE)

if total > 0:
    percentuale_testa = (len(TESTA) / total) * 100
    percentuale_croce = (len(CROCE) / total) * 100
    print(f"Percentuale di testa: {percentuale_testa:.2f}%")
    print(f"Percentuale di croce: {percentuale_croce:.2f}%")
else:
    print("Nessun dato valido inserito.")