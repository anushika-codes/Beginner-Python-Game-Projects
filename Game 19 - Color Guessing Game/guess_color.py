import random

# List of possible colors
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'black', 'white']

# Randomly select a color
secret_color = random.choice(colors)

print("Welcome to the Color Guessing Game!")
print("Guess the color I'm thinking of...")
print("Hint: Choose from these colors:", ", ".join(colors))
print("You have 5 attempts. Good luck!\n")

# Number of allowed guesses
attempts = 5

while attempts > 0:
    guess = input("Enter your guess: ").lower()

    if guess == secret_color:
        print("Congratulations! You guessed it right.")
        break
    else:
        attempts -= 1
        print(f"Wrong guess. Attempts left: {attempts}")

if attempts == 0:
    print(f"\n Sorry, you've run out of attempts. The correct color was '{secret_color}'.")

