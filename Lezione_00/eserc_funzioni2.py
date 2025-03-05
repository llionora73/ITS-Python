def check_length(stringa):
    if len(stringa) > 10:
        print(f"{stringa} è maggiore di 10")
    elif len(stringa) < 10:
        print(f"{stringa} è minore di 10")
    else:
        print(f"{stringa}  è uguale a 10")

check_length("pappappero")


