import random

# List of words to guess from
words = ["apple", "banana", "mango", "grapes", "peach"]
word = random.choice(words)

guessed = []
print("🎯 Welcome to Guess the Word!")
print("Hint: It's a fruit.")

while True:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display.strip())

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("⚠️ You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong guess!")

    # Check if all letters are guessed
    if all(letter in guessed for letter in word):
        print("\n🎉 You guessed the word:", word)
        break
