import time
import random

print("Reaction Time Tester Game")
print("When you see 'GO!', press Enter as quickly as possible.")
input("Press Enter to start...")

# Random delay before showing "GO!"
delay = random.uniform(2, 5)  # Between 2 and 5 seconds
time.sleep(delay)

print("GO!")
start_time = time.time()  # Start timing
input()  # Wait for player to press Enter
end_time = time.time()  # End timing

reaction_time = end_time - start_time
print(f"Your reaction time is {reaction_time:.3f} seconds!")
