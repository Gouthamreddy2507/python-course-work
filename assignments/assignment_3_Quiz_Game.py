questions = [
    {
        "question": "What is the default return value of a function that doesn't return anything? ",
        "options": ["0", "null", "None", "Empty string"],
        "answer": "c"
    },
    {
        "question": "Which symbol is used for floor division in Python?",
        "options": ["/", "//", "%", "**"],
        "answer": "b"
    },
    {
        "question": "What is the output of: bool('False')?",
        "options": ["False", "True", "Error", "None"],
        "answer": "b"
    },
    {
        "question": "Which function converts a number to a string?",
        "options": ["int()", "str()", "float()", "char()"],
        "answer": "b"
    },
    {
        "question": "Which keyword is used to exit a loop early?",
        "options": ["exit", "return", "stop", "break"],
        "answer": "d"
    },
    {
        "question": "What is the result of: 10 % 3?",
        "options": ["3", "1", "0", "10"],
        "answer": "b"
    },
    {
        "question": "Which of the following is a valid Python variable name?",
        "options": ["1value", "_value", "value!", "value#"],
        "answer": "b"
    },
    {
        "question": "Which of these functions returns the length of a list?",
        "options": ["count()", "size()", "length()", "len()"],
        "answer": "d"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["try", "catch", "except", "finally"],
        "answer": "c"
    },
    {
        "question": "Which operator is used to check object identity?",
        "options": ["==", "is", "=", "!is"],
        "answer": "b"
    },
    {
        "question": "What does `list(range(3))` return?",
        "options": ["[1, 2, 3]", "[0, 1, 2]", "[0, 1, 2, 3]", "[3, 2, 1]"],
        "answer": "b"
    },
    {
        "question": "Which data type is used to store key-value pairs?",
        "options": ["list", "set", "dict", "tuple"],
        "answer": "c"
    },
    {
        "question": "What does the `pass` keyword do?",
        "options": ["Exits program", "Skips code", "Does nothing", "Returns value"],
        "answer": "c"
    },
    {
        "question": "Which of the following is not a boolean value?",
        "options": ["True", "False", "None", "0"],
        "answer": "c"
    },
    {
        "question": "What is the output of: len(' ')?",
        "options": ["0", "1", "Error", "None"],
        "answer": "b"
    },
    {
        "question": "Which built-in function returns the largest item?",
        "options": ["max()", "big()", "highest()", "top()"],
        "answer": "a"
    },
    {
        "question": "What is the output of: type(3.0)?",
        "options": ["int", "float", "str", "double"],
        "answer": "b"
    },
    {
        "question": "What does `input()` return?",
        "options": ["int", "float", "bool", "str"],
        "answer": "d"
    },
    {
        "question": "What is the purpose of `continue` in a loop?",
        "options": ["Ends loop", "Skips current iteration", "Restarts loop", "Breaks loop"],
        "answer": "b"
    },
    {
        "question": "What is the result of: 2 ** 3?",
        "options": ["6", "8", "9", "5"],
        "answer": "b"
    }
]

def quiz_game():
    score = 0
    print("🎮Welcome to the Python Quiz Game!🎮\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q["question"]}")
        print(f"a) {q["options"][0]}")
        print(f"b) {q["options"][1]}")
        print(f"c) {q["options"][2]}")
        print(f"d) {q["options"][3]}")

        user_answer = input("Choose the correct answer (a/b/c/d): ").lower()

        if user_answer == q["answer"]:
            print("✅👌correct answer\n")
            score += 1
        else:
            correct_option = q["answer"]
            print(f"❌👎Wrong answer! The correct answer is {correct_option}\n ")

    print(f"your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("👏🏆Excellent! All are correct Keep it up!")
    elif score >=10:
        print("✍great job! Keep practicing!")
    else:
        print("🏋Try again. You can improve!")
        
quiz_game()
