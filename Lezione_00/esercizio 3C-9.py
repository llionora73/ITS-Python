# esercio 3C-9

points = []  

for i in range(8):
    x = int(input("Inserisci coordinata x: "))
    y = int(input("Inserisci coordinata y: "))
    points.append((x, y))


for point in points:
    x, y = point 

    match (x, y):
        case (0, 0):
            print("Il punto si trova all'origine")
        case (x, 0):
            print(f"Punto sull'asse X: ({x}, 0)")
        case (0, y):
            print(f"Punto sull'asse Y: (0, {y})")
        case _ if x > 0 and y > 0:
            print(f"Il punto {point} si trova nel primo quadrante.")
        case _ if x < 0 and y > 0:
            print(f"Il punto {point} si trova nel secondo quadrante.")
        case _ if x < 0 and y < 0:
            print(f"Il punto {point} si trova nel terzo quadrante.")
        case _ if x > 0 and y < 0:
            print(f"Il punto {point} si trova nel quarto quadrante.")
        case _:
            print(f"Punto generico: {point}")