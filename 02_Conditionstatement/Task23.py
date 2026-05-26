# 23.Create Your Own KBC Game
# Design and implement a quiz game inspired by the popular Kaun Banega Crorepati (KBC)
# game show. The aim of this assignment is to test the user's knowledge through a series of
# multiple-choice questions, track their score, and display statistics at the end of the game. The
# game also provides the flexibility to skip any question.
# Instructions:
# 1. Game Structure:
# ○ The game will consist of 5 multiple-choice questions.
# ○ The user will be asked a question with 4 options (A, B, C, D).
# ○ The user can choose to skip any question they do not want to answer.
# 2. Scoring System:
# ○ Points will be awarded for correct answers as follows:
# ■ Question 1 → 1000 points
# ■ Question 2 → 2000 points
# ■ Question 3 → 3000 points
# ■ Question 4 → 5000 points
# ■ Question 5 → 10000 points
# ○ For incorrect answers, no points will be awarded.
# ○ For skipped questions, no points will be awarded, but the game will continue.
# 3. End of Game Statistics:
# ○ At the end of the game, the following statistics will be displayed:
# ■ Total score accumulated from correct answers.
# ■ Number of correct answers provided by the user.
# ■ Number of skipped questions.
# ■ Number of wrong answers
# 4. User Experience:
# ○ At the beginning of the game, ask the user whether they would like to start or
# not the game.
# ○ Provide the option for the user to skip any question at any point..
# 5. Game Ending:
# ○ The game will end when all the questions have been answered or skipped. The
# user should receive their total score and a summary of their performance.
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },

    {
        "question": "2. Which language is used in DevOps automation?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. Paint"],
        "answer": "B"
    },

    {
        "question": "3. Who developed Python?",
        "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },

    {
        "question": "4. Which command is used to check current directory in Linux?",
        "options": ["A. ls", "B. cd", "C. pwd", "D. mkdir"],
        "answer": "C"
    },

    {
        "question": "5. What is 5 + 5 ?",
        "options": ["A. 15", "B. 20", "C. 5", "D. 10"],
        "answer": "D"
    }
]

score = 0
correct = 0
wrong = 0
skipped = 0

print("===== Welcome to KBC Game =====")

for q in questions:

    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter option (A/B/C/D) or S to Skip: ").upper()

    if user_answer == "S":
        print("Question Skipped")
        skipped += 1

    elif user_answer == q["answer"]:
        print("Correct Answer")
        score += 10
        correct += 1

    else:
        print("Wrong Answer")
        wrong += 1

print("\n===== Game Over =====")

print("Total Score :", score)
print("Correct Answers :", correct)
print("Wrong Answers :", wrong)
print("Skipped Questions :", skipped)