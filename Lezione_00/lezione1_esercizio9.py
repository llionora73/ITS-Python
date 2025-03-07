nome: str = input("Inserisci nome: ")
vendite: int = input("Inserisci vendite: ")

max_nome = nome
max_vendite = vendite

min_nome = nome
min_vendite = vendite


count = 1

while count < 20:
    new_nome: str = input("Inserisci nome: ")
    new_vendite: int = input("Inserisci vendite: ")

    if new_vendite > max_vendite:
        max_nome = new_nome
        max_vendite = new_vendite

    if new_vendite < min_vendite:
        min_nome = new_nome
        min_vendite = new_vendite

    count += 1  

print(f"Massime vendite: {max_nome}, {max_vendite}")
print(f"Minime vendite: {min_nome}, {min_vendite}")



max_nome = ""
max_vendite = float('-inf')  # Minimo possibile

min_nome = ""
min_vendite = float('inf')  # Massimo possibile

count = 0  # Conta il numero di iterazioni

while count < 20:
    new_nome = input("Inserisci nome: ")
    new_vendite = int(input("Inserisci vendite: "))

    # Controllo massimo
    if new_vendite > max_vendite:
        max_nome = new_nome
        max_vendite = new_vendite

    # Controllo minimo
    if new_vendite < min_vendite:
        min_nome = new_nome
        min_vendite = new_vendite

    count += 1  

# Stampa dei risultati
print(f"Massime vendite: {max_nome}, {max_vendite}")
print(f"Minime vendite: {min_nome}, {min_vendite}")