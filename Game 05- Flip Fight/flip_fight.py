import random

# Mapping input
tossDict = {'h': 'Heads', 't': 'Tails'}

# Score counters
user_score = 0
computer_score = 0
rounds = 0

print("Welcome to Coin Duel - Best of 5 Rounds")
print("Type 'h' for Heads or 't' for Tails\n")

while rounds < 5:
    user_input = input(f"Round {rounds + 1} - Choose (h/t): ").lower()

    if user_input not in tossDict:
        print("Invalid input. Try again.\n")
        continue

    toss_result = random.choice(['h', 't'])
    print(f"Result: {tossDict[toss_result]}")

    if user_input == toss_result:
        user_score += 1
        print("You won this round!")
    else:
        computer_score += 1
        print("You lost this round.")

    rounds += 1
    print(f"Score => You: {user_score} | Computer: {computer_score}\n")

# Final Result
print("Final Result")
if user_score > computer_score:
    print("You WIN the game!")
elif user_score < computer_score:
    print("You LOST the game.")
else:
    print("It's a DRAW!")
