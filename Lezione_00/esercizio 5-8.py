# esercizio 5-8

 
usernames = ["admin", "ospite", "utente", "minor", "supervisor"]


username = {"nome": input("Inserisci nome: "), 
            "ruolo": input("Inserisci ruolo: ")}

for i in username:
    print(f"Hello {username['nome']}")

    if username["ruolo"] == "admin":  # Check if the role is admin
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username['nome']}, thank you for logging in again.")