from my_abstract_class import Shape
import math


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        # Created afterwards..
    def area(self):
        return math.pi * self.radius ** 2

sq1 = Square(10)
print(sq1.area()) # 100

r1 = Rectangle(20, 30)
print(r1.area()) # 600

# Abstract class is a class that has one or more abstract methods.
c1 = Circle(10)
print(c1.area()) # Can't use so here abstract class is used.

