# esercizio 3C-6

animali: list[str] = []
animal_type: list[str] = []
habitat: list[str] = ["acqua", "aria", "terra"]

animal_info: dict = {"nome": " ", "animal_type": " ", "habitat": " " }


n = int(input("Quanti animali vuoi inserire? "))

for i in range(n):
    item = str(input(f"Inserisci il nome dell'animale {i+1}: "))
    item2 = str(input(f"Inserisci l'habitat dell'animale {i+1} (acqua, aria, terra): "))
    animali.append(item)
    habitat.append(item2)


print("Animali inseriti:", animali)
print("Habitat associati:", habitat)
    
    match (animali, habitat):
        case "cane" | "gatto" | "cavallo" | "elefante" | "leone":
            print(f"{animali} è un Mammifero e vive su {habitat}")
        case "balena" | "delfino":
            print(f"{animali} è un Mammifero marino e vive in acqua")
        case "serpente" | "lucertola" | "tartaruga" | "coccodrillo":
            print(f"{animali} è un Rettile e vive su {habitat}")
        case "aquila" | "pappagallo" | "gufo" | "falco" | "cigno" | "anatra" | "gallina" | "tacchino":
            print(f"{animali} è un Uccello e vive in {habitat}")
        case "squalo" | "trota" | "salmone" | "carpa":
            print(f"{animali} è un Pesce e vive in {habitat}")
        case _:
            print(f"{animali} è una categoria sconosciuta e non posso fornire informazioni su habitat")