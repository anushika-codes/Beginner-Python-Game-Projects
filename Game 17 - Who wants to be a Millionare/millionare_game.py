print("🎉 Welcome to 'Who Wants to Be a Millionaire!' 🎉")
print("Answer all 5 questions correctly to win ₹1 Crore!")
print("You have one 50-50 lifeline. Type 'lifeline' to use it during a question.\n")

# Questions: (question, options, correct_answer, lifeline_options)
questions = [
    ("What is the capital of India?",
     ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"], "B", ["B. New Delhi", "C. Kolkata"]),

    ("Which planet is known as the Red Planet?",
     ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"], "C", ["C. Mars", "A. Earth"]),

    ("Who wrote the national anthem of India?",
     ["A. Rabindranath Tagore", "B. Mahatma Gandhi", "C. Sarojini Naidu", "D. Jawaharlal Nehru"], "A", ["A. Rabindranath Tagore", "C. Sarojini Naidu"]),

    ("Which is the largest ocean in the world?",
     ["A. Indian Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Arctic Ocean"], "C", ["C. Pacific Ocean", "B. Atlantic Ocean"]),

    ("What is the square root of 144?",
     ["A. 10", "B. 11", "C. 12", "D. 14"], "C", ["B. 11", "C. 12"]),
]

prize_money = ["₹1,000", "₹10,000", "₹1 Lakh", "₹10 Lakh", "₹1 Crore"]
lifeline_used = False
earned = "₹0"

for i, (question, options, answer, lifeline_opts) in enumerate(questions):
    print(f"\nQuestion {i+1}: {question}")
    for opt in options:
        print(opt)

    while True:
        user_input = input("Enter your answer (A/B/C/D) or type 'lifeline': ").upper()

        if user_input == 'LIFELINE':
            if not lifeline_used:
                print("🆘 50-50 Lifeline Activated! Here are your options:")
                for opt in lifeline_opts:
                    print(opt)
                lifeline_used = True
            else:
                print("❌ You have already used the lifeline.")
        elif user_input in ['A', 'B', 'C', 'D']:
            if user_input == answer:
                earned = prize_money[i]
                print(f"✅ Correct! You won {earned}!")
            else:
                print("❌ Wrong answer. Game Over!")
                print(f"You won: {earned}")
                exit()
            break
        else:
            print("Invalid input. Please enter A, B, C, D or lifeline.")

print(f"\n🏆 Congratulations! You answered all questions correctly and won {earned}! 🏆")
