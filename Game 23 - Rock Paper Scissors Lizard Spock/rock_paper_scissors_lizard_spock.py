import random

# Define possible choices
choices = {
    0: "Rock",
    1: "Paper",
    2: "Scissors",
    3: "Lizard",
    4: "Spock"
}
# Each key beats the list of values
rules = {
    0: [2, 3],  # Rock crushes Scissors and crushes Lizard
    1: [0, 4],  # Paper covers Rock and disproves Spock
    2: [1, 3],  # Scissors cuts Paper and decapitates Lizard
    3: [1, 4],  # Lizard eats Paper and poisons Spock
    4: [0, 2]   # Spock vaporizes Rock and smashes Scissors
}

# Display choices
print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
print("Choices:")
for key in choices:
    print(f"{key}: {choices[key]}")

# Get user input
user_choice = int(input("Enter your choice (0-4): "))
if user_choice not in choices:
    print("Invalid choice. Please enter a number between 0 and 4.")
    exit()

# Computer makes a choice
computer_choice = random.randint(0, 4)

print(f"\nYou chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif computer_choice in rules[user_choice]:
    print("You win!")
else:
    print("Computer wins!")
