import random

# Function to generate a random math question
def generate_question():
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(operators)

    # Avoid division by zero and ensure clean division
    if operator == '/':
        num1 = num1 * num2  # Make sure num1 is divisible by num2

    question = f"{num1} {operator} {num2}"
    correct_answer = eval(question)
    
    if operator == '/':
        correct_answer = round(correct_answer, 2)  # round to 2 decimals

    return question, correct_answer

# Main function
def math_quiz():
    score = 0
    total_questions = 5
    print("🎯 Welcome to the Math Quiz Game!")
    print(f"You'll be asked {total_questions} questions.\n")

    for i in range(total_questions):
        question, answer = generate_question()
        print(f"Q{i+1}: What is {question}?")
        try:
            user_input = float(input("Your answer: "))
            if abs(user_input - answer) < 0.01:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was {answer}\n")
        except ValueError:
            print(f"Invalid input! The correct answer was {answer}\n")

    print(f"Quiz Over! Your score: {score}/{total_questions}")

# Run the quiz
math_quiz()

