'''
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
For example:
print(remove_elements({5, 6, 7}, [7, 8, 9]))
{5, 6}
'''

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    