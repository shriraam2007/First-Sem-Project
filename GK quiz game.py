import sys

def run_quiz():
    """
    Manages the main quiz session, including questions, answers, and scoring.
    """
    questions = [
        {
            "prompt": "The total degraded land in our country is:",
            "options": {
                "a": "133 million hectares",
                "b": "130 million sq. km.",
                "c": "140 million hectares",
                "d": "130 million hectares"
            },
            "answer": "d"
        },
        {
            "prompt": "The alluvial soil consists of:",
            "options": {
                "a": "sand",
                "b": "silt",
                "c": "clay",
                "d": "all of the above"
            },
            "answer": "d"
        },
        {
            "prompt": "‘There is enough for everybody’s need and not for any body’s greed,’ who gave this statement?",
            "options": {
                "a": "Vinoba Bhave",
                "b": "Mahatma Gandhi",
                "c": "Jawaharlal Nehru",
                "d": "Atal Behari Vajpayee"
            },
            "answer": "b"
        },
        {
            "prompt": "A belief that the majority community should be able to rule a country in whichever way it wants is:",
            "options": {
                "a": "Power Sharing",
                "b": "Central Government",
                "c": "Majoritarianism",
                "d": "Community Government"
            },
            "answer": "c"
        },
        {
            "prompt": "Which of the following is a renewable resource?",
            "options": {
                "a": "Coal",
                "b": "Petroleum",
                "c": "Solar Energy",
                "d": "Natural Gas"
            },
            "answer": "c"
        },
        {
            "prompt": "What is the main purpose of the World Trade Organization (WTO)?",
            "options": {
                "a": "To provide loans to developing countries",
                "b": "To regulate international trade",
                "c": "To promote global peace",
                "d": "To manage global health crises"
            },
            "answer": "b"
        },
        {
            "prompt": "The Non-Cooperation Movement was started by Mahatma Gandhi in which year?",
            "options": {
                "a": "1919",
                "b": "1920",
                "c": "1930",
                "d": "1942"
            },
            "answer": "b"
        },
        {
            "prompt": "What is the term for the total value of all goods and services produced in a country in a year?",
            "options": {
                "a": "Gross Domestic Product (GDP)",
                "b": "Net National Product (NNP)",
                "c": "Per Capita Income",
                "d": "Human Development Index (HDI)"
            },
            "answer": "a"
        },
        {
            "prompt": "Which of these is NOT a primary sector activity?",
            "options": {
                "a": "Farming",
                "b": "Fishing",
                "c": "Banking",
                "d": "Mining"
            },
            "answer": "c"
        },
        {
            "prompt": "The power-sharing arrangement in Belgium is a good example of:",
            "options": {
                "a": "A federal government",
                "b": "A unitary government",
                "c": "A community government",
                "d": "Both (a) and (c)"
            },
            "answer": "d"
        }
    ]

    score = 0
    total_questions = len(questions)

    # Loop through each question in the list
    for i, question_data in enumerate(questions):
        print(f"\n--- Question {i + 1}/{total_questions} ---")
        print(question_data["prompt"])

        # Print the options
        for key, value in question_data["options"].items():
            print(f"({key}) {value}")

        # Get user's answer
        while True:
            user_answer = input("Your answer (a, b, c, or d): ").lower().strip()
            if user_answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Invalid input. Please enter a, b, c, or d.")

        # Check answer and provide correct feedback
        if user_answer == question_data["answer"]:
            print("Correct! Great job!.")
            score += 1
        else:
            print(f"This is not correct. The correct answer was ({question_data['answer']}).")

    # Display the final score
    print("\n--- Quiz Over! ---")
    print(f"You scored: {score}/{total_questions}")

def main():
    """
    Main function to start the quiz game.
    """
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print(" WELCOME!! WANT TO TEST YOUR G.K. WITH THIS PYTHON QUIZ GAME? ")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

    while True:
        play = input("DO YOU WANT TO PLAY? (yes/no): ").lower().strip()
        if play == "yes":
            run_quiz()
            break
        elif play == "no":
            print("Okay, catch you some other time. Take care!")
            break
        else:
            print("I don't get that. Please enter 'yes' or 'no'.")

# --- Main execution block ---
if __name__ == "__main__":
    main()
