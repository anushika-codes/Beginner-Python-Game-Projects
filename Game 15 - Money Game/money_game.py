import random

print("Money Guessing Game")
print("--------------------")

# Difficulty level
print("Choose difficulty level:")
print("1. Easy (1–50)")
print("2. Medium (1–100)")
print("3. Hard (1–500)")

level = input("Enter 1, 2, or 3: ")

if level == '1':
    max_value = 50
elif level == '2':
    max_value = 100
elif level == '3':
    max_value = 500
else:
    print("Invalid choice. Defaulting to Medium.")
    max_value = 100

# To ask number of rounds
rounds = int(input("\nHow many rounds do you want to play? "))
score = 0

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}")
    
    hidden_amount = random.randint(1, max_value)
    guess = int(input(f"Guess the hidden amount (₹1 to ₹{max_value}): "))

    difference = abs(guess - hidden_amount)

    if guess == hidden_amount:
        print("Exact match! You win ₹100 bonus!")
        score += 100
    elif difference <= 5:
        print(f"Very close! The actual amount was ₹{hidden_amount}. You win ₹20.")
        score += 20
    elif difference <= 15:
        print(f"Not bad! The amount was ₹{hidden_amount}. You win ₹10.")
        score += 10
    else:
        print(f"Too far! The hidden amount was ₹{hidden_amount}. No reward this time.")

# Final results
print("\nGame Over")
print("----------")
print(f"Your Total Score: ₹{score}")

if score == rounds * 100:
    print("Excellent! Perfect guessing!")
elif score >= rounds * 20:
    print("Good job!")
elif score > 0:
    print("Not bad. Keep improving!")
else:
    print("Better luck next time!")
