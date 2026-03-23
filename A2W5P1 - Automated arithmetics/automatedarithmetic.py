import random


def arithmetic_operation(arithmetic_type: str) -> dict:
    questions = {}
    if arithmetic_type == "subtraction":
        symbol = "-"
    elif arithmetic_type == "multiplication":
        symbol = "*"
    else:
        symbol = "+"

    for question_index in range(1, 11):
        firstnumber = random.randint(1, 100)
        secondnumber = random.randint(1, 100)
        questions[question_index] = f"{firstnumber} {symbol} {secondnumber} ="
    return questions


def validate_input(user_input: str) -> bool:
    return user_input.lower() in ["summation", "multiplication", "subtraction"]


def ask_questions(questions: dict, arithmetic_type: str) -> None:
    correct_answers = 0
    mistakes = []

    if arithmetic_type == "subtraction":
        symbol = "-"
    elif arithmetic_type == "multiplication":
        symbol = "*"
    else:
        symbol = "+"

    for index in range(1, 11):
        question_str = questions[index]
        parts = question_str.split(symbol)
        firstnumber = int(parts[0].strip())
        secondnumber = int(parts[1].replace("=", "").strip())

        if arithmetic_type == "summation":
            correct_answer = firstnumber + secondnumber
        elif arithmetic_type == "subtraction":
            correct_answer = firstnumber - secondnumber
        elif arithmetic_type == "multiplication":
            correct_answer = firstnumber * secondnumber

        try:
            user_input_val = input(f"{question_str} ")
            user_answer = int(user_input_val)
        except ValueError:
            user_answer = None

        if user_answer == correct_answer:
            correct_answers += 1
        else:
            mistakes.append(f"{question_str} {user_answer} (Correct was: {correct_answer})")

    incorrect_answers = 10 - correct_answers
    print(f'You had {correct_answers} correct and {incorrect_answers} incorrect answers in "{arithmetic_type}"')

    if mistakes:
        for mistake in mistakes:
            print(mistake)


if __name__ == "__main__":
    op_type = input("Arithmetic operation: ").strip().lower()
    while not validate_input(op_type):
        print("Please enter: 'summation', 'multiplication', 'subtraction'")
        op_type = input("Arithmetic operation: ").strip().lower()

    generated_questions = arithmetic_operation(op_type)
    ask_questions(generated_questions, op_type)