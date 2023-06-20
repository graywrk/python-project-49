import prompt
import sys

def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name

def print_question(question_string):
    print(f"Question: {question_string}")

def get_answer():
    answer = prompt.string("Your answer: ")
    return answer

def check_answer(username, given, correct):
    if str(given) == str(correct):
        print("Correct!")
        return True
    else:
        print(f"'{given}' is wrong answer ;(. Correct answer was '{correct}'")
        print(f"Let's try again, {username}!")
        return False

def game_cycle(questions, game_description):
    username = welcome_user()
    print(f"{game_description}")
    for item in questions:
        print_question(item[0])
        answer = get_answer()
        if check_answer(username, answer, item[1]):
            continue
        else:
            sys.exit(0)
    
    print(f"Contgratulations, {username}!")
