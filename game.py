import random

print("Welcome to the guessing game!")
number = random.randint(1, 20)
guess = 0
tries = 0

while guess != number:
    guess = int(input("Guess a number between 1 and 20: "))
    tries += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number} in {tries} tries!")
