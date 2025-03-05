# esercizio 4-11

pizza: list=["margherita", "capricciosa","Napoli"]

friend_pizza: list=["margherita", "capricciosa","Napoli"]

pizza.append("Diavola")
print(pizza)

for i in pizza:
    print(f"Le mie pizze preferite sono: {i}")

friend_pizza.append("4 stagioni")
print(friend_pizza)

for i in friend_pizza:
    print(f"Le pizze preferite del mio amico sono: {i}")