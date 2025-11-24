# ==, >=, <=, >, <, !=
# Syntax of if
# Indentation ~ Spaces to create block in python. 4 spaces in block.

"""
if condition:
    statement1
    statement2
    ...
    statementN
statementM
"""

age = float(input("Enter your age: "))
if age >= 18:
    print("Congrats! You are an adult. You can now cast vote.")
print("Program end.")

# if-else
"""
if condition:
    # Block of code to be executed when condition is True
else:
    # Block of code to be executed when condition is False
"""

age = float(input("Enter your age: "))
if age >= 18:
    print("Congrats! You can now cast vote.")
else:
    print("You can not cast vote.")
print("Program end.")

# WAP to print if a number (int) is odd or even.
# Even when number is divisible by 2.
# Odd when number is not divisible by 2, remainder is not 0.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# WAP to print if a number is negative or positive.
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive.")
else:
    print(f"{num} is negative.")
