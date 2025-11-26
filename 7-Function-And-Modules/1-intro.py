# Can we create functions of our own? ~ User defined functions
# Built-in functions are available to us automatically.
# Some functions require us to import module.

# User defined functions - Syntax
"""
def function_name(arg1, arg2, arg3,..argN):
    statement1
    statement2
    ...
    statementN
"""

def greeting_someone():
    print("Hello, Good Morning")
    print("It's a beautiful day.")

# To call a function - you have to write that function name.
greeting_someone() # O/P - Hello, Good Morning...It's a beautiful day.

# You can call this multiple times as well..

def greet(name):
    print(f"Hello {name}, Good Morning")
    print("It's a beautiful day.")

# greet() # ERROR - We need to pass value of the argument.
greet("Shriyash")

def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(10) # Even
even_or_odd(5) # Odd

def add(num1,num2):
    result = num1 + num2
    print(f"Result: {result}")

add(10,20) # 30
add(9,-4) # 5

