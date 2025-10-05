# --- Interactive Quiz Application ---

#List of Dictionaries

questions = [
    {
        'question' : 'what is the capital of France?',
        'options' : ["A. London", "B. Berlin", "C. Paris", "D. Rome"],
        "answer" : "C"
    },
    {
        "question" : "which planet is known as the Red Planet?",
        "options" : ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        'answer' : "B"
    },
    {
        'question' : 'what is the result of 5 + 7?',
        'options' : ["A. 10", "B. 11", "C. 12", "D. 13"],
        'answer' : 'C'
    }

]

score = 0

print("--- Welcome to the python Quiz! ---")

for q in questions:
    print("\n----------------")
    print(q["question"])
    for option in q['options']:
        print(option)

    user_answer = input("Enter your answer (A, B, C, or D): ").upper()

    if user_answer == q['answer']:
        print("Correct! Well done")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}")

print("\n--- Quiz Over ---")

print(f"Your final score is: {score} out of {len(questions)}")