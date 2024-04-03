
import random

# Define a list of questions, each with a question, options, correct answer, and a fun fact.
questions = [
    {
        "question": "Which cuisine is known for sushi and sashimi?",
        "options": ["A) Italian", "B) Japanese", "C) Mexican", "D) Indian"],
        "correct_answer": "B",
        "fun_fact": "Sushi is often served with pickled ginger and soy sauce."
    },
    {
        "question": "What is the primary ingredient in guacamole?",
        "options": ["A) Tomato", "B) Avocado", "C) Potato", "D) Onion"],
        "correct_answer": "B",
        "fun_fact": "Avocado is also the main ingredient in avocado toast."
    },
    {
        "question": "What cooking technique involves cooking food in a vacuum-sealed bag at a precise temperature?",
        "options": ["A) Grilling", "B) Frying", "C) Sous-vide", "D) Roasting"],
        "correct_answer": "C",
        "fun_fact": "Sous-vide cooking results in tender and evenly cooked dishes."
    }
    # Add more questions here
]

# Function to shuffle the questions randomly
def shuffle_questions(questions):
    random.shuffle(questions)

# Function to display a question and its options
def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)

# Function to check if the user's answer is correct
def is_correct(answer, question_data):
    return answer.lower() == question_data["correct_answer"].lower()

# Function to play the quiz game
def play_quiz(questions):
    shuffle_questions(questions)
    score = 0

    for question_data in questions:
        display_question(question_data)
        user_answer = input("Enter the letter of your answer (A/B/C/D): ")

        if user_answer.upper() == question_data["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        print(f"Fun Fact: {question_data['fun_fact']}\n")

    print(f"Quiz completed! Your score is {score}/{len(questions)}.")

# Main function to start the quiz
if __name__ == "__main__":
    print("Welcome to the Cuisine Quiz Game!\n")
    play_quiz(questions)
