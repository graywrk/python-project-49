import random
import math
from brain_games.game_engine import game_cycle


def game():
    questions = []
    questions_num = 3
    max_random_number = 100
    random.seed()
    for _ in range(questions_num):
        first = random.randrange(max_random_number)
        second = random.randrange(max_random_number)
        answer = math.gcd(first, second)
        question = f"{first} {second}"
        questions.append([question, answer])
    game_cycle(questions, 'Find the greatest common divisor of given numbers.')