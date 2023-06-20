import random
import math
from brain_games.game_engine import game_cycle


def game():
    questions = []
    questions_num = 3
    max_random_number = 10
    random.seed()
    for _ in range(questions_num):
        progression_length = 9
        first = random.randrange(max_random_number)
        step = random.randrange(max_random_number)
        blank_num = random.randrange(progression_length)
        question = f"{first}"
        for i in range(1, progression_length):
            num = first + step * i
            if i == blank_num:
                answer = num
                question += " .."
            else:
                question += f" {num}"
        questions.append([question, answer])
    game_cycle(questions, 'What number is missing in the progression?')