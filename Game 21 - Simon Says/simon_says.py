import random
import time

def show_sequence(sequence):
    print("\nSimon says:")
    for action in sequence:
        print(f"{action}")
        time.sleep(1)
    print("\n" * 20)  # Clear screen effect

def get_user_input(length):
    print(f"Now repeat the sequence (type the {length} actions separated by spaces):")
    return input("Your turn: ").strip().lower().split()

def main():
    actions = ["jump", "clap", "spin", "dance"]
    sequence = []
    score = 0

    print("Welcome to Simon Says: Action Edition!")
    print("Remember and repeat the sequence of actions!")
    print("Game starting...\n")
    time.sleep(2)

    while True:
        next_action = random.choice(actions)
        sequence.append(next_action)

        show_sequence(sequence)
        user_sequence = get_user_input(len(sequence))

        if user_sequence != sequence:
            print("Wrong sequence! Game Over.")
            print(f"Your final score: {score}")
            break
        else:
            score += 1
            print("Correct! Get ready for the next round...")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
