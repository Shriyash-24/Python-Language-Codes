# Concept where we can create a method that can be called in different methods.
# Python doesn't support method overloading.
class A:
    def add(self, num1, num2):
        return num1 + num2

    def add(self, num1, num2, num3):
        return num1 + num2 + num3

obj = A()
print(obj.add(1, 2))# ERROR.. A.add() missing 1 required positional argument: num3.

# The latest add effect, the new effect will be take effect and will be called.

