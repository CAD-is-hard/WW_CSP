# WW, Number Guessing Game
import random
number = random.randint(1,101)
count = 0
print("I am thinking of a number between 1 and 100, you have six tries to guess it.")


while True:
    guess = int(input("What is your first guess:"))
    if guess > number:
        print("Too high, try again.")
    elif guess < number:
        print("Too low, Try again.")
    else:
        print("You got it!")
        break
