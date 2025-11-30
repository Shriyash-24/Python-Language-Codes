# Polymorphism Operator Overloading

a = 10
b = 20
print(a+b) # a.__add__(b) is called internally.
# So int.__add__(a,b)

s1 = "Hello"
s2 = "World"
print(s1+s2) # str.__add__(s1,s2)

class A:
    def f1(self, val):
        pass

obj = A()
obj.f1(20) # A.f1(obj,20)

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __add__(self, other):
        return self.length + other.length


r1 = Rectangle(5,3)
r2 = Rectangle(8,6)
print(r1.area())
print(r2.area())
# print(r1 + r2) # ERROR..
# r1 is Rectangle class, it doesn't have __add__ method. So, any class if they don't have __add__ defined in them.. you can't use it.
print(r1+r2) # r1.length + r2.length.
# This is called operator overload, you can overload or create your operators.
# You can decide to use your own operators.




