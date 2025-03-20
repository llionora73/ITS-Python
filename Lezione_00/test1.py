
def nome_funzione(param1: type1, param2: type2) -> None:

    pass



def nome_funzione(x, y, int = 1, *args, **kwargs) -> None:

    for key, value in kwargs.items():

        if key == "chiave1":
            print(value)

        elif key == "chiave2":
            print(value)
    
        else:
            print("chiave non riconosciuta")

    print(args, kwargs)


def nome_funzione(dataclass) -> None:

dataclass.nome
dataclass.cognome
dataclass.data_di_nascita




