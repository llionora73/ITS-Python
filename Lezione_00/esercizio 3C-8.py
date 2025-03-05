# esercizio 3C-8

frase = input("Inserisci frase: ")

Lunghezza = len(frase)
Ultimo = frase[Lunghezza - 1]

match Ultimo:
    case "?" if Lunghezza % 2 == 0:
        print("Si")
    case "?" if Lunghezza % 2 != 0:
        print("No")
    case "!":
        print("Wow!")
    case _:
        print(f"Tu dici {frase}")