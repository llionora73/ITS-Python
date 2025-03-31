# esercizio 1
'''
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
For example:
print(frequency_dict(['mela', 'banana', 'mela']))
'''
def frequency_dict(element:list)->dict:
    freq = {}
    for item in element:
        freq[item] = freq.get(item, 0) + 1
    return freq


# esercizio 2
'''
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione.
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. '
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
For example:
print(check_combination(True, False, True))
print(check_combination(False, True, False))

'''

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA:
        return "Operazione permessa"
    elif conditionB and conditionC:
        return "Operazione permessa"
    else:
        return "Operazione negata"



# esercizio 3
'''
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
For example:

print(check_access("admin", "12345", True))
print(check_access("admin", "54321", True))
'''

def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    

# esercizio 4
'''
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione 
e l'elemento iniziale viene spostato alla fine della lista. 
Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

For example:
print(rotate_left([1, 2, 3, 4, 5], 2))

'''

def rotate_left(elements: list, k: int) -> list:
    if not elements: 
        return elements
    k = k % len(elements) 
    return elements[k:] + elements[:k]

# esercizio 5
'''
Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
For example:
print(sum_above_threshold([15, 5, 25], 20))
'''

def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    if not numbers: 
        return 0  

    n_numbers = [n for n in numbers if n > threshold]  
    return sum(n_numbers)  



# esercizio 6

''''
Il codice dovrebbe stampare i numeri all'interno di una lista.
TROVA L'ERRORE E CORREGGI IL CODICE'
'''

numbers: list[int] = [1, 2, 3, 4, 5]

for i in range (len(numbers)):
    print("Number:", numbers[i])


# esercizio 7
'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
For example:
print(check_parentheses("()()"))
print(check_parentheses("(()))(")) 
'''

def check_parentheses(expression: str) -> bool:
    count = 0
    for parenteses in expression:
        if parenteses == '(':
            count += 1
        elif parenteses == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

# esercizio 8
'''
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
For example:
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 2, 3, 4, 5]))'
'''

def count_isolated(element:list) -> int:
    freq = {}
    for item in element:
        freq[item] = freq.get(item, 0) + 1
        
    isolated_count = sum(1 for item in freq if freq[item] == 1)
    return isolated_count

# esercizio 9
'''
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
For example:
print(remove_elements({5, 6, 7}, [7, 8, 9]))
{5, 6}
'''

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:


# esercizio 10
'''
Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori.
For example:
print(merge_dictionaries({'x': 5}, {'x': -5}))
result 
{'x': 0} '''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    risultato = dict1.copy()  

    for chiave, valore in dict2.items():
        if chiave in risultato:
            risultato[chiave] += valore  
        else:
            risultato[chiave] = valore  
    
    return risultato


