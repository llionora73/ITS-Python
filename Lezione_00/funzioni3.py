# Quale sarà l'output, l'ordine di esecuzione e l'ordine di rimozione delle funzioni dalla call stack nel seguente codice?

def alpha():
    print("Executing alpha")

def beta():
    alpha()
    print("Executing beta")

def gamma():
    print("Executing gamma")
    beta()

gamma()


# output:
Executing gamma
Executing alpha
Executing beta

# ordine esecuzione: 
Gamma() -> Beta() -> Alpha()

# ordine rimozione: 
Alpha() -> Beta() -> Gamma()


