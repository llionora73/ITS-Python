# esercizio 3C-2 

voto:int = int(input("Inserisci il voto di laurea: "))

match voto: 
    case voto if voto>=106 and voto<=110:
        print(f"GPA 4.0")
    case voto if voto>=101 and voto<=105:
        print(f"GPA 3.7")
    case voto if voto>=96 and voto<=100:
        print(f"GPA 3.3")
    case voto if voto>=86 and voto<=90:
        print(f"GPA 2.7")
    case voto if voto>=81 and voto<=85:
        print(f"GPA 2.3")
    case voto if voto>=76 and voto<=80:
        print(f"GPA 2.0")
    case voto if voto>=70 and voto<=75:
        print(f"GPA 1.7")
    case voto if voto>=66 and voto<=69:
        print(f"GPA 1.0")
    case _:
        print("Voto non valido!")