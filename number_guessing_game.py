# WW, Number Guessing Game
import random

number = random.randint(1, 100)
count = 0

print("I am thinking of a number between 1 and 100, you have six tries to guess it.")

while count < 6:
    count += 1
    guess = int(input("Guess #" + str(count) + ": "))

    if guess > number:
        print("Too high, try again.")
    elif guess < number:
        print("Too low, try again.")
    else:
        print("You got it in " + str(count) + " tries!")
        break

if guess != number:
    print("You're out of guesses! The number was " + str(number) + ".")