#esercizio 3-5.
name: list = ["Francesca", "Eleonora", "Andrea", "Matteo"]
message: str = "sei invitato/a alla cena di gala di martedì p.v. allo Sheraton"
for index in name:
    print(f"Caro/a {index}, {message}!")

denied: str = "Andrea"
print(denied)

name.pop(2)
print(name)

name.append("Carlo")
print(name)
for index in name: 
    print(f"Caro/a {index}, {message}!")