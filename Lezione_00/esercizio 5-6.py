# esercizio 5-6 

età = input("Inserisci età: ")
x = età

if 0 <= x < 2:
    print("the person is a baby")

elif 2 <= x < 4:  
    print("the person is a toddler")

elif 4 <= x < 13:
    print("the person is a kid")

elif 13 <= x < 20:
    print("the person is a teenager")

elif 20 <= x < 65:
    print("the person is an adult")

else:
    print("the person is an elder")