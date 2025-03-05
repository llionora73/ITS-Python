# esercizio 3-6.
name: list = ["Francesca", "Eleonora", "Matteo", "Carlo"]
message: str = "vogliamo informarti che abbiamo un tavolo in più per invitare un tuo amico"
for index in name:
    print(f"Caro/a {index}, {message}!")

name1: str = "Mario"
name2: str = "Chiara"
name3: str = "Filippo"

name.insert(0, "Mario")
print(name)

name.insert(3, "Chiara")
print(name)

name.insert(6, "Filippo")
print(name)

message: str = "sei invitato/a alla cena di gala di martedì p.v. allo Sheraton"
for index in name:
    print(f"Caro/a {index}, {message}!")