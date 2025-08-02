import time

print("Typing Speed Game")
print("------------------")
print("Type the following sentence as fast and accurately as you can:")

sentence = "The quick brown fox jumps over the lazy dog"
print("\nYour sentence is:")
print(f"{sentence}")

input("\nPress Enter when you're ready to start...")

# Start timer
start_time = time.time()

# User types the sentence
typed = input("\nStart typing: ")

# End timer
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

# Check accuracy
if typed == sentence:
    print("\nPerfect typing.")
else:
    print("\nThere were some mistakes in your typing.")

# Words per minute (WPM)
words = len(sentence.split())
wpm = (words / time_taken) * 60

print(f"\nTime taken: {round(time_taken, 2)} seconds")
print(f"Your typing speed: {round(wpm, 2)} words per minute")

