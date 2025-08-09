import random

# Dictionary of emojis and their names
emoji_dict = {
    "😀": "smile",
    "🐍": "snake",
    "🍕": "pizza",
    "🚗": "car",
    "⚽": "football",
    "🐱": "cat",
    "🌧️": "rain",
    "🔥": "fire",
    "📚": "books",
    "🎵": "music"
}

print("🎯 Emoji Guess Game 🎯")
print("Guess the name of the emoji!")

# To select a random emoji
emoji, name = random.choice(list(emoji_dict.items()))

# Give a hint
print(f"Here is your emoji: {emoji}")
guess = input("Your guess: ").strip().lower()

# Check the guess
if guess == name:
    print("✅ Correct! You guessed it right.")
else:
    print(f"❌ Wrong! The correct answer was '{name}'.")
