
def recursiveArmonica(n: float) -> float:
    if n <= 0:
        print("Errore: ")

    elif n == 1:
        return 1.0
    
    else:
        return (1/n) * recursiveArmonica(n-1)
    
print(recursiveArmonica(10))