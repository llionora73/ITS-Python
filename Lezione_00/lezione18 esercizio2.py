# Scrivi una funzione validate_password(password) che controlli se una password soddisfa i seguenti criteri: 
# lunghezza minima di 20 caratteri, almeno tre lettere maiuscole, almeno quattro caratteri speciali (non alfanumerici). 
# Se la password è valida, la funzione dovrebbe restituire True. Se la password non è valida, la funzione dovrebbe 
# sollevare un'eccezione incorporata (ad esempio, ValueError) con un messaggio che indica quali criteri non sono stati soddisfatti.

def validate_password(password: str) -> bool:
    if len(password) < 20:
        raise Exception("Lunghezza minima 20 caratteri")
    elif

    elif

    else:
        return True

    
print(validate_password("jlsavhaiugbòaieuvbfòaivfbaò")) 
print(validate_password("ivfbaò")) 

