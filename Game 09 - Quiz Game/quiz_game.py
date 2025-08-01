# Quiz Game 

# List of questions with options and answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": ["A. Mahatma Gandhi", "B. Subhash Chandra Bose", "C. Rabindranath Tagore", "D. Jawaharlal Nehru"],
        "answer": "C"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 6", "B. 8", "C. 7", "D. 9"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Control Program Unit", "C. Central Programming Unit", "D. Computer Processing Unit"],
        "answer": "A"
    }
]

# Start quiz
def start_quiz():
    score = 0
    print("Welcome to the Quiz Game!\n")

    for i, q in enumerate(questions):
        print(f"Q{i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Quiz completed. Your final score: {score}/{len(questions)}")

# Run the game
start_quiz()

