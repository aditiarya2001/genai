class Student:
    def __init__(self, name, grade):
        self.name = name        #attributes
        self.grade = grade

    def display(self):
        print(f"{self.name}" + " is in " + f"{self.grade}" + "th grade")


john = Student("Jonathan", 9)
john.display()

marcos = Student("Marcos", 11)
marcos.display()
