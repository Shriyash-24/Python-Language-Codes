"""
Create a simple number guessing game.
The user gets 10 chances to guess a number.
If user guesses the number before 10 chances ~ we stop and say thanks.
If user never guesses the number, ask them 10 times and end the game.
"""

# Solution by me.

print("Welcome to the number guessing game. We have a number that needs to be guessed. You have 10 chances.")
print("The secret number is between 1 and 50.")

number = 48
attempts = 10
print(f"You have {attempts} attempts left.")

while True:
    if attempts < 1:
        break
    guess = int(input("Guess the number: "))
    if guess == number:
        print("Congratulations! Your guess is correct.")
        break
    elif guess < number:
        print("Your guess is wrong. Try higher.")
        attempts = attempts - 1
        print(f"You have {attempts} attempts left.")
    elif guess > number:
        print("Your guess is wrong. Try lower.")
        attempts = attempts - 1
        print(f"You have {attempts} attempts left.")
print(f"The number was {number}. Game Over!")