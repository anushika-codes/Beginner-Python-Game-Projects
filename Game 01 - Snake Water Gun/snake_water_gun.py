#Snake Water Gun
'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

if youstr not in youDict:
    print("Invalid input!")
else:
    you = youDict[youstr]
    print("You chose:", reverseDict[you])
    print("Computer chose:", reverseDict[computer])

    if you == computer:
        print("It's a Draw!")
    elif you == 1 and computer == -1:
        print("You Win!")
    elif you == -1 and computer == 0:
        print("You Win!")
    elif you == 0 and computer == 1:
        print("You Win!")
    elif you == -1 and computer == 1:
        print("You Lose!")
    elif you == 0 and computer == -1:
        print("You Lose!")
    elif you == 1 and computer == 0:
        print("You Lose!")
