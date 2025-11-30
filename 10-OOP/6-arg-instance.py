class Student:
    def study(self, n_hours):
        print(f"The student studies for {n_hours}H/Day.")

    def plays(self, sports_name):
        print(f"The student plays {sports_name}")

student1 = Student()
print(f"The Object: {student1}") # The Object: <__main__.Student object at 0x0000022C6C760590>
student1.study(3) # The student studies for 3H/Day.

student2 = Student()
print(f"The Object: {student2}") # The Object: <__main__.Student object at 0x0000022C6C758410>
student2.study(5) # The student studies for 5H/Day.

student1.plays("Cricket") # The student plays Cricket
student2.plays("Tennis") # The student plays Tennis.

