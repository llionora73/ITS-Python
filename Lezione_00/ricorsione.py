
# metodo iterativo:

def countdown(n:int) -> None:

    if n < 0:
        print("Error! Inserted number is negative!")

        while n >= 0:
            print(n)
            n -= 1

countdown(-5)
countdown(5)


# oppure

def countdown(n:int) -> None:
    if n >=0 :
        while n:
            print(n)
            n = n - 1
    else:
        print("Error! Inserted number is negative!")

countdown(-5)
countdown(5)


# metodo ricorsivo

def countdown(n:int) -> None:
    if n < 0:
        print("Error! Inserted number is negative!")
    
    elif n == 0:
        print(0)

    else:
        print(n)
        countdown(n-1)


countdown(6)
countdown(-2)


# Scrivi una funzione chiamata sum che accetta un numero intero positivo n come input e restituisce la somma dei numeri da 0 a n.
# Se il numero di input n è negativo, visualizza un messaggio di errore e la funzione deve restituire None.
# Per implementare la funzione sum, devi usare esclusivamente un ciclo while e il parametro n passato come input alla funzione.
# È consentito dichiarare solo una variabile all'interno della funzione per gestire la somma.
# Quindi, chiama la funzione sum per n = -5 e n ​​= 5.

# metodo iterativo:

def sum_n(n:int) ->int:
    if n < 0:
        print("Error")
        return 0
    else:
        sum_n: int = 0
        while n:
            sum_n= sum_n + n
            n = n-1
            return int(sum_n)
        

sum_n(5)
sum_n(-5)


# metodo ricorsivo

def recursiveSum(n:int) -> int:
    if n < 0:
        print("Error")
        return 0
    
    elif n == 0:
        return 0
    
    else:
        return int(n + recursiveSum(n-1))
    
recursiveSum(-5)
recursiveSum(0)
recursiveSum(5)

# Write a function sumInRange that calculates the sum of all integers between a and b, inclusive, where a and b are passed as input to the function.
# To solve the exercise, it is mandatory to use a while loop, and it is assumed that the value of b is always greater than the value of a. 
# Therefore, if a > b, it is necessary to swap the values to ensure that a is the smaller of the two.
# Finally, it is allowed to declare only one variable, in addition to the function parameters, to store the sum.
# Then, call the function sumInRange for a = 5, b = 10 and for a = 10, b = 5.

# metodo iterativo:

def sumInRange(a:int, b:int) -> int:
    if a > b:
        temp:int = a
        a = b
        b = temp  # in alternativa:  a,b = b,a
    sum:int = 0

    while b>=a:
        sum = sum + b
        b = b -1
        return int(sum)
    
print(sumInRange(a=5, b=10))
print(sumInRange(a=10, b=5))

# Write a recursive function recursiveSumInRange that calculates the sum of all integers between a and b, inclusive, where a and b are passed as input to the function.
# Assume that the value of b is always greater than the value of a. Therefore, if a > b, it is necessary to swap the values to ensure that a is the smaller of the two.
# Then, call the function recursiveSumInRange for a = 5, b = 10 and for a = 10, b = 5.

# metodo ricorsivo:

def recursiveSumInRange(a:int, b:int) -> int:
    if a > b:
        temp:int = a
        a = b
        b = temp 

    elif b == a:
        return int(a)
    
    else:
        return int(b + recursiveSumInRange(a, b-1))

print(recursiveSumInRange(5,10))
print(recursiveSumInRange(10,5))
