#Dice Duel
'''
You and the computer will roll a dice.
Highest number wins the round.
Best of 5 rounds wins the game.
'''

import random

you_score = 0
computer_score = 0
rounds = 0

while rounds < 5:
    input("Press Enter to roll the dice...")

    your_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("You rolled:", your_roll)
    print("Computer rolled:", computer_roll)

    if your_roll > computer_roll:
        print("You win this round!\n")
        you_score += 1
    elif your_roll < computer_roll:
        print("Computer wins this round!\n")
        computer_score += 1
    else:
        print("It's a draw!\n")

    rounds += 1

print("Final Score:")
print("You:", you_score)
print("Computer:", computer_score)

if you_score > computer_score:
    print("Congratulations! You won the game!")
elif computer_score > you_score:
    print("Computer won the game! Better luck next time!")
else:
    print("It's a tie! Well played.")
