"""
Write a program to simulate a roll of a die/dice.
"""

import random
print("Welcome to dice game: ")
while True:
    choice = input("Press 'Enter' to roll the dice or 'q' to quit.")
    choice = choice.strip()
    choice = choice.lower()
    if choice == 'q':
        print("Thank you. Good bye.")
        break
    elif choice == '':
        number = random.randint(1,6)
        print(f"Your number is {number}.")
    else:
        print("Invalid input.")

