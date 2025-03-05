# esercizio 3C-4

animali: list[str] = []

for i in range(8):
    item: list = str(input("Inserisci animale: "))
    animali.append(item)

print(animali)  
    
    match animali:
        case ["cane", "gatto", "cavallo", "elefante", "leone"]:
            print("Mammifero")
        case ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
            print("Rettili")
        case ["aquila", "pappagallo", "gufo", "falco"]:
            print("Uccelli")
        case ["squalo", "trota", "salmone", "carpa"]:
            print("Pesci")
        case _:
            print("Categoria sconosciuta")