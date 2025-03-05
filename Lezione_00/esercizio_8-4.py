def make_shirt(size:str="large", message:str="I love python!") -> None:
    print(f"My size is: {size} and I want to buy the shirt with this message: \"{message}\"")

# Making a large shirt with the default message
make_shirt()

# Making a medium shirt with the default message
make_shirt(size="Medium")

# Making a custom shirt with a different message
make_shirt(size="Small", message="Code is life!")