# Snake Water Gun Game
'''
1 for Snake
-1 for Water
0 for Gun
'''

import random

# Mapping input letters to numbers
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Take user input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Validate input
if youstr not in youDict:
    print("Invalid input. Choose from 's', 'w', or 'g'.")
else:
    you = youDict[youstr]
    computer = random.choice([-1, 0, 1])

    # Show choices
    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    # Determine result
    if you == computer:
        print("It's a Draw!")
    elif (you == 1 and computer == -1) or \
         (you == -1 and computer == 0) or \
         (you == 0 and computer == 1):
        print("You Win!")
    else:
        print("You Lose!")
