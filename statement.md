# Statement.md  
**Project Title:** Online Python Quiz Game  
**Course:** Introduction to Problem Solving & Programming   

---

## 1. Purpose or Goal of the Project  
The goal was to develop a simple quiz game that runs in the command line using Python. It tests the player's general knowledge by presenting ten multiple-choice questions one by one, checking the answers, giving instant feedback, and showing the final score at the end.  

---

## 2. Requirements  
The task was to design a simple, interactive quiz program that uses basic programming concepts such as:  
- Handling user input  
- Using lists and dictionaries for data storage  
- Implementing loops and conditional logic  
- Structuring code into reusable functions  

---

## 3. System Design  
- **Data Structure:**  
  A list of dictionaries stores the quiz questions. Each dictionary contains:  
  - The question prompt  
  - A set of options (`a`, `b`, `c`, `d`)  
  - The correct answer  

---

## 4. Top-Down Design / Modularization  
To ensure proper design the program was divided into functions:  
- `main()`: It is the entry point of the program. It handles the welcome message, start prompt, and calls the quiz function.  
- `run_quiz()`: It handles the initialization of the question set, the main game loop, input validation, and scoring.

This modular approach separates the quiz logic from the overall program flow.  

---

## 5. Algorithm Development  
- **Program Flow:**  
  1. Display a greeting and ask the user if they wish to start the quiz.  
  2. Begin only if the user says “yes.” If “no,” exit.  
  3. Present 10 multiple-choice questions, one at a time.  
  4. Prompt the user to enter an answer (`a`, `b`, `c`, or `d`).  
  5. Validate the answer and give immediate feedback (Correct/Incorrect).  
  6. Maintain a running score.  
  7. Show the final score at the end of the quiz.  

---

## 6. Implementation  
- **Language:** Python 3  
- **Input Handling:** User input is converted to lowercase and whitespace removed so inputs like 'Yes,' ' yes,' or 'A' are recognized correctly.

---

## 7. Testing and Refinement  
The application was tested manually to confirm all requirements were met:  
- **Start Prompt:** Tested with “yes,” “no,” “YES,” “ no ”, and invalid inputs.  
- **Answer Validation:** Checked with correct answers, incorrect answers, and invalid inputs (e.g., “e,” “hello”).  
- **Scoring:** Verified by completing the quiz.  
- **Refinement:** Improved feedback messages by showing the correct answer when the user was wrong.  

---

## 8. Conclusion  
This project successfully demonstrates the application of basic programming principles in Python. The quiz game is interactive, user-friendly, and meets all specified requirements.  

---

## 9. Future Enhancements  
Potential improvements include:  
- Loading questions from external files (JSON/CSV).  
- Adding topic selection (e.g., Science, History, Geography).  
- Introducing difficulty levels.  
- Creating a graphical interface (GUI).  


