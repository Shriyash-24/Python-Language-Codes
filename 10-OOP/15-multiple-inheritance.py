# Single Level Inheritance

class A:
    def state_1(self):
        print("State_1 present")

    def state_2(self):
        print("State_2 present")

    def state_3(self):
        print("State_3 present")

class B:
    def state_4(self):
        print("State_4 present")

    def state_5(self):
        print("State_5 present")

# Multiple Level Inheritance
class C(A,B):
    def state_6(self):
        print("State_6 present")

a = A()
a.state_2() # state_2 present

b = B()
b.state_4() # state_4 present

c = C()
# We have all the methods.
c.state_3() # state_3 present
c.state_1() # state_1 present

