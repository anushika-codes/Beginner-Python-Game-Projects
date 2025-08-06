def word_chain_game():
    print("Welcome to the Word Chain Game!")
    print("Rules:")
    print("- Player 1 starts with any word.")
    print("- Player 2 must say a word that starts with the last letter of the previous word.")
    print("- Repeated words are not allowed.")
    print("- Game ends if a player makes a mistake.\n")

    used_words = set()
    current_player = 1
    last_letter = None

    while True:
        word = input(f"Player {current_player}, enter a word: ").lower().strip()

        if not word.isalpha():
            print("❌ Invalid input. Use letters only.")
            continue

        if word in used_words:
            print(f"❌ '{word}' has already been used. Player {current_player} loses!")
            break

        if last_letter and word[0] != last_letter:
            print(f"❌ Word must start with '{last_letter}'. Player {current_player} loses!")
            break

        used_words.add(word)
        last_letter = word[-1]
        current_player = 2 if current_player == 1 else 1

# Run the game
word_chain_game()
