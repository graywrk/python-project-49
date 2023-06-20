import random
from brain_games.game_engine import game_cycle


def is_even(number):
    return number % 2 == 0


def game():
    questions = []
    questions_num = 3
    max_random_number = 100
    random.seed()
    for _ in range(questions_num):
        first = random.randrange(max_random_number)
        second = random.randrange(max_random_number)
        op = random.randrange(2)
        if op == 0:
            op = "+"
            answer = first + second
        elif op == 1:
            op = "-"
            answer = first - second
        else:
            op = "*"
            answer = first * second
        question = f"{first} {op} {second}"
        questions.append([question, answer])
    game_cycle(questions, 'What is the result of the expression?')
