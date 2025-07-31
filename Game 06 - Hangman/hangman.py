import random

# List of words and their corresponding hints
words_with_hints = [
    ("apple", "A common red or green fruit"),
    ("banana", "A yellow fruit monkeys love"),
    ("grapes", "Small round fruit, comes in bunches"),
    ("orange", "A citrus fruit and also a color"),
    ("mango", "King of fruits in summer")
]

# Choose a random word and its hint
word, hint = random.choice(words_with_hints)
hidden = ["_"] * len(word)
lives = 6

print("🎮 Welcome to Hangman!")
print(f"📏 The word has {len(word)} letters.")
print(f"💡 Hint: {hint}")
print("Word:", " ".join(hidden))

while lives > 0 and "_" in hidden:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter only one valid letter.")
        continue

    if guess in word:
        found = False
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
                found = True
        if found:
            print("✅ Correct!")
    else:
        lives -= 1
        print(f"❌ Wrong! Lives left: {lives}")

    print("Word:", " ".join(hidden))

# Final result
if "_" not in hidden:
    print("🎉 You win! The word was:", word)
else:
    print("💀 You lose! The word was:", word)

