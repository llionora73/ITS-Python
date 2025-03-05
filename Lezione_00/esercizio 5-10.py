# esercizio 5-10

current_users = [{"nome": "mario", "ruolo": "admin"},
    {"nome": "maria", "ruolo": "utente"},
    {"nome": "sara", "ruolo": "admin"},
    {"nome": "marco", "ruolo": "utente"}]

new_users = []

nome = input("Inserisci nome: ")
ruolo = input("Inserisci ruolo: ")

new_user = {"nome": nome, "ruolo": ruolo}

if new_users[nome] == current_users[nome]:
    print("Username has already been used. You will need to enter a new username.")
else:
    current_users.append(new_user)
    print("Username is available.")