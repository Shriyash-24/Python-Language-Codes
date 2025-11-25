import random
num = 1
print("Welcome to the number guessing game. We have a number that needs to be guessed. You have 10 attempts.")
print("The secret number is between 1 and 50.")
secret_number = random.randint(1, 50)
attempts = 10
is_guess_correct = False

while num <= 10:
    print(f"You have {attempts} attempts to guess the number.")
    user_number = int(input("Enter a number: "))
    if user_number == secret_number:
        print("You guessed the number!")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"Your guess is wrong. Try {higher_or_lower} number.")
    num = num + 1
    attempts -= 1

if is_guess_correct == False:
    print(f"Bad luck. You exhausted all the attempts. You couldn't guess the number.")
print(f"The secret number was {secret_number}, Game Over.")
