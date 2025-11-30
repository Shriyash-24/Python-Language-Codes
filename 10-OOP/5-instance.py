# Instance Methods -  Methods that are associated with objects or instances.
# Defined inside a class which is bound to/or associated with instance/object.

class Student:
    """
    This is class Student to manage student info and activities.
    """
    def study():
        return "The student studies for 3 hours a day."

student1 = Student()
print(student1) #<__main__.Student object at 0x000001EA8A3C0590>
# Basically shows where student1 object is created.

#student1.study() # TypeError: Student.study() takes 0 positional arguments but 1 was given.
# "but 1 was given" ~ What is this?
# study is a method, something gets passed internally by python.

def studies():
    return "The student studies for 3 hours a day."


class Stu:
    def studies(self):
        print(f"Self: {self}") # Self: <__main__.Stu object at 0x0000027DBA5C06E0>
        print("The student studies for 3 hours a day.")

student1 = Stu()
print(f"The object: {student1}") # The object: <__main__.Student object at 0x000001E2D37B06E0>
student1.studies() # The student studies for 3 hours a day.

# When we call an instance method using object/instance of the class, python pases the object itself,
# as the first argument to that method. By standard 1st argument is self.

# The student1 is passed as an object to the studies function, and then self is same as student1.





