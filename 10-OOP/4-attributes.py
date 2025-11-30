# Attributes

class Student:
    pass

student1 = Student()
student2 = Student()

student1.name = "John"
student1.roll = 1001
print(student1.name) # John
print(student1.roll) # 1001

# print(student2.name) # ERROR
help(Student)
# We get __dict__ which contains all instance variables ~ the variables that are associated with the instance or the object.
print(student1.__dict__) # {'name': 'John', 'roll': 1001}
# We get dictionary of all the variables associated with it.
print(student2.__dict__) # {}
