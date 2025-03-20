# calcolare frequenza numero

dizionario_frequenze = {}

while True:
    numero_inserito = int(input("inserisci numero:  "))

    if numero_inserito in dizionario_frequenze:
        dizionario_frequenze[numero_inserito] += 1

    else:
        dizionario_frequenze[numero_inserito] = 1


# massimo frequenza







