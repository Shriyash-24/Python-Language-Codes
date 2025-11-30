# Initializers In Python

# __init__() method
# It is an instance method, used to create and initialize attributes during obj creation.

class Student:
    def __init__(self):
        print("Calling the initializer.")

    def study(self,n_hours):
        print("The students studies for {n_hours}.")
    def plays(self , sport):
        print(f"Student plays {sport}.")

student1 = Student() # Creates the object - Calling the initializer is printed.
# __init__ gets called directly by python. It's a special method because it automatically gets.
# Used to initialize attributes of the object.

# object_name.attribute_name = value
student1.name = "John"

student2 = Student()
student2.name = "Carol"

# -----------------------------------------------------
class Student:
    def __init__(self, name, roll):
        print("Calling the initializer.")
        self.name = name # student1.name = "John"
        self.roll = roll # student1.roll = 1001

    def studies(self, n_hours):
        print("The students studies for {n_hours}.")

    def plays(self, sport):
        print(f"Student plays {sport}.")

student1 = Student("John", 1001)
student2 = Student("Carol", 1002)
print(student1.name, student1.roll) # John 1001
print(student2.name, student2.roll) # Carol 1002

print(student1.__dict__) # {'name': 'John', 'roll': 1001}
print(student2.__dict__) # {'name': 'Carol', 'roll': 1002}

student1.grade = "B"
print(student1.grade)