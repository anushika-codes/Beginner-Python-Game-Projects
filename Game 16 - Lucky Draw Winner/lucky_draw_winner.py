import random
import time

# Wheel items
wheel_items = ["Prize 1", "Prize 2", "Prize 3", "Try Again", "Better Luck Next Time", "Jackpot!"]

print("🎉 Welcome to the Lucky Draw Wheel Game! 🎉")

while True:
    input("\nPress Enter to spin the wheel...")

    print("Spinning the wheel", end="")
    for i in range(5): 
        print(".", end="", flush=True)
        time.sleep(0.5)

    # Random selection
    result = random.choice(wheel_items)
    print("\n\n🎁 The wheel stopped at: ", result)

    # Spin again
    again = input("\nDo you want to spin again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break
