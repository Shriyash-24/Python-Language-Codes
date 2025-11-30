# Class variables are defined at class level.
# Same copy of the class variables are shared among the objects.

class Student:
    college_name = "GH College"
    departments = ["Mechanical", "Civil", "CS"]
    def __init__(self, name, roll):
        print("Calling the initializer.")
        self.name = name # student1.name = "John"
        self.roll = roll # student1.roll = 1001

    def studies(self, n_hours):
        print("The students studies for {n_hours}.")

    def plays(self, sport):
        print(f"Student plays {sport}.")

student1 = Student("John", 1001)
help(Student) # Here you can see class variables.
print(student1.__dict__) # {'name': 'John', 'roll': 1001} - only shows instance variables.
print(student1.departments) # ['Mechanical', 'Civil', 'CS']
print(student1.college_name) # GH College

student2 = Student("Carol", 1002)
print(student2.departments) # Same values.
print(student2.college_name) # Same as student1.

