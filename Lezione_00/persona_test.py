'''
# Dal file persona.py importa la classe Persona
from persona import Persona

# creare un oggetto di tipo Persona
eds: Persona = Persona("Eleonora", "De Santis", 47)

print(eds)

print(eds.name, eds.lastname, eds.age)

'''

# dal file persna2 importa la classe Persona

from persona2 import Persona
eds: Persona = Persona()

# voglio richiamare la funzione dispolayData della classe Persona per stampare le informazioni relative alla persona eds

eds.displayData()


# impostare il nome della persona eds

eds.setName("Eleonora")

print("......")

eds.displayData()

# impostare ilcognome della persona eds
eds.setLastname("De Santis")

# impostare l'eta della persona eds
eds.setAge(47)

print("....")
eds.displayData()

print(eds.getName(), eds.getLastname(), eds.getAge())