import random
from brain_games.game_engine import game_cycle


def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True


def game():
    questions = []
    questions_num = 3
    max_random_number = 100
    random.seed()
    for _ in range(questions_num):
        question = random.randrange(max_random_number)
        if is_prime(question):
            answer = "yes"
        else:
            answer = "no"
        questions.append([question, answer])
    game_cycle(questions, 'Answer "yes" if given number is prime. '
                          'Otherwise answer "no".')
