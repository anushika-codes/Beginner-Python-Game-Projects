# Rock Paper Scissors Game
'''
1 for Rock
-1 for Paper
0 for Scissors
'''

import random

# Mapping for display
youDict = {"r": 1, "p": -1, "s": 0}
compDict = {1: "Rock", -1: "Paper", 0: "Scissors"}

# Computer's choice
computer = random.choice([1, -1, 0])

# User input
youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()

# Input validation
if youstr not in youDict:
    print("Invalid input! Please enter r, p, or s.")
else:
    you = youDict[youstr]
    print(f"You chose: {compDict[you]}")
    print(f"Computer chose: {compDict[computer]}")

    # Outcome logic
    if you == computer:
        print("It's a Draw!")
    elif (you == 1 and computer == 0) or (you == -1 and computer == 1) or (you == 0 and computer == -1):
        print("You Win!")
    else:
        print("You Lose!")

