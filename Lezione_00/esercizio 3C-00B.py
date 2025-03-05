# esercizio 3C-00B

name: str = str(input("Insert name: "))
gender:  str = str(input("Insert gender: "))

match gender:
    case "f":
        print(f"{name}, Femmina")
    case "m":
        print(f"{name}, Maschio")
    case _:
        print(f"Mi dispiace {name}, non e' possibile procedere con la generazione di un documento di identità!")