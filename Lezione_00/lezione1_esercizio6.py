

n = int(input("Inserisci un numero: "))

if n > 0:  # Controllo che sia positivo
    fattoriale = 1
    for i in range(1, n + 1):
        fattoriale *= i  # Calcola il fattoriale
    print(f"Il fattoriale di {n} è: {fattoriale}")
else:
    print("Il numero inserito deve essere un intero positivo.")