"""
Static method - method defined inside a class which is neither bound to the object nor to the class.
to create a static method, we use staticmethod decorator.
"""

class Student:
    college_name = "GH College"
    departments = ["Mechanical", "Civil", "CS"]
    def __init__(self, name, roll):
        self.name = name # student1.name = "John"
        self.roll = roll # student1.roll = 1001

    def studies(self, n_hours):
        print(self)
        print(f"{self.name} studies for {n_hours}.")

    def plays(self, sport):
        print(f"Student plays {sport} in {self.college_name}.")

    @staticmethod
    def greet():
        print(f"Welcome.")

    @classmethod
    def get_departments(cls):
        print(f"Departments in {cls.college_name} are: ")
        for department in cls.departments:
            print(department)

# Static methods don't need anything at all.
student1 = Student("Kyle", 567) # Creates object student1.
student1.studies(3)
student1.get_departments()
student1.greet() # Welcome.

student2 = Student("Alice", 34)
student2.studies(2)


