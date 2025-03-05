def add_one(num:int):    #funzione 1
        
        result= num+1
        return result

def add_one_to_list(par2:list[int]):

    new_list: list[int] = []

    for elemento in par2:

        incremento = add_one(elemento)
        new_list.append(incremento)
    
    return new_list

print(add_one_to_list([5, 6, 7]))       