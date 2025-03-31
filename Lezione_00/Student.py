class Student:

# classe student (attributi classe: name, studyProgramm)

#self.name: str (attributo di tipo stringa)
#self.studyprogramm: str (attributo di tipo stringa)
#self.age: int (attributo di tipo intero)
#self.gander: str (attributo di tipo stringa)

#costruttore

    def __init__(self, name:str, studyprogram:str, age: int, gender: str):
        self.name = name
        self.studyprogram = studyprogram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"Name: {self.name}\nStudyprogram: {self.studyprogram}\nAge: {self.age}\nGender: {self.gender}")
    
    

eleonora: Student("Eleonora", "laurea", 46, "F")
eleonora.printInfo()
chiara: Student("Chiara", "diploma", 28, "F")
chiara.printInfo()
lorenzo: Student("Lorenzo", "Diploma", 35, "M")
lorenzo.printInfo()



# da rivedere:
class Student:
    def __init__(self, name: str, study_program: str, age: int, gender: str):
        """Initialize the student with name, study program, age, and gender."""
        self.name = name
        self.study_program = study_program
        self.age = age
        self.gender = gender

    def print_info(self):
        """Print student information."""
        print(f"Name: {self.name}")
        print(f"Study Program: {self.study_program}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print("-" * 30)


# Creating three student instances
student1 = Student("Alice Johnson", "Computer Science", 22, "Female")
student2 = Student("Bob Smith", "Mechanical Engineering", 23, "Male")
student3 = Student("Charlie Brown", "Electrical Engineering", 21, "Non-binary")

# Testing the print_info method
student1.print_info()
student2.print_info()
student3.print_info()