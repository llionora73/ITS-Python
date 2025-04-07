# Scrivi una funzione safe_sqrt(number) che calcola la radice quadrata di un numero usando math.sqrt(). 
# Gestisci ValueError se l'input è negativo restituendo un messaggio informativo.

import math

def my_sqrt(n: float) -> float:
    try:
        return math.sqrt(n) 
    
    except ValueError: 
        print("The number should be positive")
        return None 

print(my_sqrt(10)) 
print(my_sqrt(-5))
