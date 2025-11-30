# The method that is being inherited by child class might not have behave in same way.
# There is a way when we change the effect from parent class.

class Employee:
    def working_hours(self):
        return 45

class Intern(Employee):
    def working_hours(self):
        return 30

# Working hours not overriden
i1 = Intern()
print(i1.working_hours()) # 45

# Woking hours overriden
print(i1.working_hours())
