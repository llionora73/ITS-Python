# esercizio 3-7.
name: list = ["Mario", "Francesca", "Eleonora","Chiara", "Matteo", "Carlo", "Filippo"]
message: str = "vogliamo informarti che abbiamo un tavolo in meno e possiamo invitare solo due persone"
for index in name:
    
    print(f"Caro/a {index}, {message}!")

name.pop("Mario")
print(name)
message: str = "siamo dispiaciuti di informarla che non possiamo invitarla a cena."
print(f"Caro Mario, {message}!")
    
name.pop("Francesca")
print(name)
message: str = "siamo dispiaciuti di informarla che non possiamo invitarla a cena."
print(f"Cara Francesca, {message}!")

    
name.pop("Eleonora")
print(name)
message: str = "siamo dispiaciuti di informarla che non possiamo invitarla a cena."
print(f"Cara Eleonora, {message}!")

name.pop("Chiara")
print(name)
message: str = "siamo dispiaciuti di informarla che non possiamo invitarla a cena."
print(f"Cara Chiara, {message}!")


name.pop("Matteo")
print(name)
message: str = "siamo dispiaciuti di informarla che non possiamo invitarla a cena."
print(f"Caro Matteo, {message}!")

name: list=["Carlo","Filippo"]
message2: str = "vogliamo informarla che il suo posto al tavolo risulta ancora disponibile"
for index in name:
    
    print(f"Caro/a {index}, {message2}!")

name.del("Carlo","Filippo")
print(name)
