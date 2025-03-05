# esercizio 3C-3

oggetti: list[str] = []

'''
i=1
inserire primo oggetto. 
item=input()
inserire il primo oggetto (item) nella lista chiamata oggetti.
oggetti.append(item)

i=2
inserire secondo oggetto.
item= input()
oggetti.append(item)

i=3
inserire terzo oggetto.
item=input()
oggetti.append(item)

'''
#for i in range(3) -> 0<= i < 3
#for i in range(1,4) -> 1<= i < 4

for i in range(3):
    item: str = str(input("Inserisci oggetto: "))
    oggetti.append(item)
    print(oggetti)    

match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte", "uova"] :
        print("Prodotti alimentari")
    case  ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")