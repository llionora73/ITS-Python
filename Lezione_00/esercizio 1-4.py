# esercizio 1-4

# Si scriva un programma che dato un intero di quattro cifre, per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, una cifra per riga:

numero = int(input("Inserisci un numero a 4 cifre: "))

# Convertire il numero in una stringa e stampare ogni cifra su una nuova riga
for cifra in str(numero):
    print(cifra)