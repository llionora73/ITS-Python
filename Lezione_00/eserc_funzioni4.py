def check_each(numbers:list[int]):
    for i in numbers:

        if i > 5:
            print(f"{i} è maggiore di 5")
        elif i < 5:
            print(f"{i} è minore di 5")
        else:
            print(f"{i}  è uguale a 5")

numbers = [2, 7, 34, 12, 54, 32]
check_each(numbers)
