# esercizio 5-9

users = {}

if not users:
    print("We need to find some users!")
else:
    print(f"Hello {users['nome']}!")


nome = input("Inserisci nome: ")
ruolo = input("Inserisci ruolo: ")

users = {"nome": nome, "ruolo": ruolo}

print(users)

users.clear()

if not users:
    print("We need to find some users!")