#esercizio 3C-5

utente = {"nome": input("Inserisci nome: "), 
          "ruolo": input("Inserisci ruolo: "), 
          "età": int(input("Inserisci età: "))}

match utente:
    case {"nome": name, "ruolo": "admin"}:
        print(f"Accesso completo a tutte le funzionalità")

    case {"nome": name, "ruolo": "utente"}:
        print(f"Può gestire i contenuti ma non modificare le impostazioni")

    case {"età": età} if età >= 18:
        print(f"Accesso standard a tutti i servizi")
    
    case {"età": età} if età < 18:
        print(f"Accesso limitato! Alcune funzionalità sono bloccate")

    case {"nome": name, "ruolo": "ospite"}:
        print(f"Accesso ristretto! Solo visualizzazione dei contenuti")

    case _:
        print("Attenzione! Ruolo non riconosciuto! Accesso Negato!")