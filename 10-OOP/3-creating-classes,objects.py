# Creating a class - Use cap-word convention.

# Empty Class
class MyClass:
    pass

# Creating an object
obj1 = MyClass()
obj2 = MyClass()

# obj1 and obj2 are objects of the class.
l1 = [10,20,30]
print(type(l1)) # <class 'list'>

print(type(obj1)) # <class '__main__.MyClass'>
# main is dunder, double underscore start/end.

# Any function that is defined in class are methods.

# Calling methods using objects?
# obj1.method(arg1, arg2, ...)

class Student:
    """
    This is a class Student to manage student information and activities.
    """
    pass

s1 = Student()
s2 = Student()

# Doc-Strings - Documentation or the details about the class.
# __doc__
print(Student.__doc__) # This is a class Student to manage student information and activities.
print(help(Student)) # Provides help for the class.

