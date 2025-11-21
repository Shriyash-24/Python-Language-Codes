"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name. - Welcome John Doe! Welcome to the python program.
"""

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
concat = first_name + " " + last_name
print("Hello!", concat, "~ Welcome to the python program.")
