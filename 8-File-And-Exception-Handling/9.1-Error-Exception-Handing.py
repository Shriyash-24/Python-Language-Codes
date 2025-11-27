"""
Compile time error => Syntax error and indentation error.
"""

age = 24
print(age # SyntaxError: '(' was never closed.

age = 24
if age >=18:
print("You are old enough") # IndentationError

"""
Exceptions ==> Errors during execution. Syntax/Indentation is correct.
"""

print(10/0) # ZeroDivisionError
x = 100
result = x + y # NameError: 'y' not defined.

# Built-in errors are exceptions, how to handle these?
# We use try and except.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

try: # code tries to run
    result = num1 / num2
    print(result)
except: # if there is an exception, this runs..
    print("The denominator shouldn't be zero.")

# 2 exceptions

try:
    num9 = int(input("Enter a number: "))
    num10 = int(input("Enter another number: "))
    result = num9 / num10
    print(result)
except ZeroDivisionError:
    print("The denominator shouldn't be zero.")
except ValueError:
    print("Input should only be digits.")