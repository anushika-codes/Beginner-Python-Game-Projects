import random

print("🎉 Welcome to the Truth and Dare Game! 🎉")
name = input("Enter your name: ")

truths = [
    "What is your most embarrassing moment?",
    "Have you ever lied to your best friend?",
    "What’s a secret you’ve never told anyone?",
    "Who was your first crush?",
    "Have you ever cheated in an exam?",
    "What is one thing you hate but pretend to like?",
    "Have you ever stalked someone on social media?",
    "What’s the weirdest thing you’ve ever eaten?",
    "Have you ever had a crush on a teacher?",
    "What is the biggest lie you've told your parents?",
    "What’s something you’re afraid of but haven’t told anyone?",
    "If you could switch lives with someone for a day, who would it be?",
    "What’s the most childish thing you still do?",
    "Who do you text the most?",
    "Have you ever lied about your age?",
    "What’s one thing you would never do even for ₹1 crore?",
    "Have you ever been caught lying?",
    "Who is your secret crush right now?",
    "What’s the last lie you told?",
    "What is the most awkward thing you’ve ever done in public?"
]

dares = [
    "Do 10 jumping jacks!",
    "Sing your favorite song loudly!",
    "Text your crush 'I like you...'",
    "Do an impression of your favorite celebrity!",
    "Dance without music for 30 seconds!",
    "Post an embarrassing selfie on your story!",
    "Speak in a funny accent for the next 2 minutes.",
    "Try to lick your elbow.",
    "Do a fake proposal to someone nearby (or pretend).",
    "Eat a spoonful of ketchup/salt.",
    "Balance a book on your head for 30 seconds.",
    "Pretend you're a cat for 1 minute.",
    "Say the alphabet backwards.",
    "Do 5 push-ups right now.",
    "Call a friend and sing a Bollywood song.",
    "Pretend your hand is a phone and talk to it.",
    "Act like a baby for 1 minute.",
    "Write 'I am silly' 5 times and read it loudly.",
    "Walk like a model for 1 minute.",
    "Pretend to cry for 20 seconds."
]

while True:
    print(f"\n{name}, it's your turn!")
    choice = input("Type 'truth', 'dare', or 'exit': ").lower()

    if choice == 'truth':
        question = random.choice(truths)
        print(f"🧠 TRUTH: {question}")

    elif choice == 'dare':
        task = random.choice(dares)
        print(f"🔥 DARE: {task}")

    elif choice == 'exit':
        print("Thanks for playing! Goodbye!")
        break

    else:
        print("Invalid input. Please type 'truth', 'dare', or 'exit'.")
