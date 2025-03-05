# Funzioni

sum = 0
for i in range(1, 11):
    sum += i
    print("Sum from 1 to", i, "is", sum)

sum = 0
for i in range(20, 38):
    sum += i
    print("Sum from 20 to", i, "is", sum)

sum = 0
for i in range(35, 50):
    sum += i
    print("Sum from 35 to", i, "is", sum)

# oppure

somma = sum(range(1, 11))
print(somma)

somma = sum(range(20, 38))
print(somma)

somma = sum(range(35, 50))
print(somma)


# oppure

# def functionName(list of parameters):
def sum(a:int, b:int) -> int:
    
# instructions for function body(code to be executed)
    sum:int = 0
    for i in range(a, b+1):
        sum = sum + i
        return sum

mysum = sum(1, 10)
print(f"Sum from 1 to 10 is {sum(1, 10)}")

# oppure

def sum(a: int, b: int):
    total: int = 0
    for i in range(a, b+1):
        total += i
    return total

mysum = sum(1, 10)
print(mysum)


# esercizio

def subtract(a:int, b:int):
    subtract = (a - b)
    return subtract

print(subtract(10, 5)) 

# oppure 

def subtract(a:int, b:int):
    result:int = a - b
    return result

myresult = subtract(4, 1)
print(myresult)

# no return

def hello(nome) -> None:
    print(f"Hello, {nome}!")

hello("Alice") 
Print(type(hello()))


# define a function returning multiple values(returning a tuple)
def operations(a: int, b: int) -> tuple[int, int]:
    sum_result:int = a + b
    diff_result:int = a - b

    # Returns a tuple with two values
    return sum_result, diff_result

# Assigns values to two variables
sum_value, diff_value = operations(10, 5)
print("Sum:", sum_value) # Output: Sum: 15
print("Difference:", diff_value) # Output: Difference: 5

# Print the type of the returned value
print(type(operations(10, 5)))  # Output: <class 'tuple'>

# define a function returning a list
def get_coordinates() -> list[float]:
    return [12.5, 45.8]

coords = get_coordinates()
print(coords[0], coords[1], sep=", ")

print(type(coords))


# define a function returning a dictionary
def get_user(myname:str, myrole:str) -> dict[str, str]:
    return {"name": myname, "role": myrole}

user = get_user("Alice", "Admin")
print(user["name"]) # Output: Alice
print(user["role"]) # Output: Admin
print(type(user))


# Functions with parameters passed by position
def describe_person(name:str, age:int, city:str):
    print(f"{name} is {age} years old and lives in {city}.")
# Chiamata alla funzione con passaggio per posizione
describe_person("Alice", 25, "Rome")



# Functions with parameters passed by keyword
def describe_person(name:str, age:int, city:str):
    print(f"{name} is {age} years old and lives in {city}.")
# Chiamata alla funzione con passaggio per posizione
describe_person("Alice", 25, "Rome")
# The function describe_person can be written 
describe_person("Alice", city="Rome", age=25)
describe_person(age=25, city= "Rome", name="Alice")
describe_person(city="Rome", age=25, name="Alice") # ERROR( Arguments passed by position must precede arguments passed by keyword(Similarly for parameters))



# Functions with default values
def total(w, x, y=10, z=20):
    return (w ** x) + y + z
# calling function total, while omitting the last two values
total(2, 3)
# Output: 38 -> calulated as 2^3 + 10 + 20
# calling function total, while omitting the last values
total(2, 3, 4)
# Output: 32 -> calculated as 2^3 + 4
# calling function total with 4 input values
total(2, 3, 4, 5)
# Output: 17 -> calculated as 2^3 + 4 + 5