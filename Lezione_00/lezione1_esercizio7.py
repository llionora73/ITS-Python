
pari = 0
dispari = 0
count = 0

while True:
    if count == 10:
        print("Numeri pari:", pari)
        print("Numeri dispari:", dispari)
        break

    n = int(input("Inserisci un numero: "))
    
    if n % 2 == 0:
        pari += 1  
    else:
        dispari += 1  

    count += 1 