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
        question = random.randrange(max_random_number)
        if is_even(question):
            answer = "yes"
        else:
            answer = "no"
        questions.append([question, answer])
    game_cycle(questions, 'Answer "yes" if the number is even, '
                          'otherwise answer "no".')
