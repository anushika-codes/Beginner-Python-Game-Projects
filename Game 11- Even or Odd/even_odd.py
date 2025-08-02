import random

print("Welcome to the Even-Odd Game!")
print("You and computer will pick a number from 0 to 9.")

# User enters a number
user_number = int(input("Enter your number (0–9): "))

# Computer randomly picks a number
computer_number = random.randint(0, 9)

# Total
total = user_number + computer_number

print(f"\nYou chose {user_number}, computer chose {computer_number}. Total is {total}.")

# Check even or odd
if total % 2 == 0:
    print("🔵 The result is EVEN!")
else:
    print("🟡 The result is ODD!")

