#Number Guessing Game
'''
Computer will choose a number from 1 to 100
You have to guess it
You keep guessing until you get it right.
'''

import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it right.")

