soglia:  int = input("Inserisci numero soglia: ")
count = 0

while True:
    if count == 7:
        break

    n = int(input("Inserisci un numero: "))
    
    if n > soglia:
        print(n)
        count = count +1
        
    else:
        count = count +1 
