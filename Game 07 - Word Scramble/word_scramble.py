import random

# Word dictionary with levels and complicated hints
words_by_level = {
    "easy": [
        ("apple", "This entity often experiences gravitational attention."),
        ("mango", "Known in royalty as the monarch of summer edibles."),
        ("grape", "Often compressed into a fermented celebratory fluid.")
    ],
    "medium": [
        ("planet", "A celestial body in orbital servitude around a luminous giant."),
        ("jungle", "A densely packed biosphere teeming with biodiversity."),
        ("guitar", "A resonant string manipulator with frets and vibes.")
    ],
    "hard": [
        ("dilemma", "A cognitive gridlock between binary conundrums."),
        ("cryptic", "Conveyed in a form resistant to direct interpretation."),
        ("paradox", "A statement that defies logic by being self-negating.")
    ]
}

# Ask user to choose level
print("🎮 Welcome to Word Scramble!")
level = input("Choose difficulty (easy / medium / hard): ").lower()

# Validate level
if level not in words_by_level:
    print("Invalid level. Defaulting to easy.")
    level = "easy"

# Select a random word and hint from the chosen level
word, hint = random.choice(words_by_level[level])

# Scramble the word
scrambled = list(word)
random.shuffle(scrambled)
scrambled_word = "".join(scrambled)

# Set number of attempts
attempts = 3

# Start game
print(f"\n🧩 Scrambled Word: {scrambled_word}")
print(f"💡 Complicated Hint: {hint}")

while attempts > 0:
    guess = input("Your guess: ").lower()
    if guess == word:
        print("🎉 Correct! You unscrambled the word.")
        break
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

if attempts == 0:
    print(f"💀 You lost! The correct word was: {word}")

