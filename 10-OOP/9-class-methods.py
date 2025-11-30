# Class Methods - Methods defined inside the class that are bound to the class .
# To create class method, we use decorator called, classmethod

class Welcome:
    # Write classmethod on top of it. We use cls as standard method.
    @classmethod
    def greet(cls):
        print(cls)
        print("Hello")

w1 = Welcome()
w1.greet() # O/P -->
# <class '__main__.Welcome'>
# Hello

print(Welcome) # <class '__main__.Welcome'>

class Student:
    college_name = "GH College"
    departments = ["Mechanical", "Civil", "CS"]
    def __init__(self, name, roll):
        print("Calling the initializer.")
        self.name = name # student1.name = "John"
        self.roll = roll # student1.roll = 1001

    def studies(self, n_hours):
        print(self)
        print(f"The students studies for {n_hours}.")

    def plays(self, sport):
        print(f"Student plays {sport} in {self.college_name}.")

    @classmethod
    def greet(cls):
        print(cls)
        print(f"Welcome to {cls.college_name}.")

    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.college_name} are: ")
        for department in cls.departments:
            print(department)

student1 = Student("John", 1001)
student1.studies(3) # <__main__.Student object at 0x000002070B0F06E0>, The students studies for 3.
student1.greet() # <class '__main__.Student'>, Welcome to GH college.

# Class Methods are used to use class variables.

student1.plays("Football") # Student plays Football in GH College.
student1.get_departments()
# Mechanical
# Civil
# CS







