#!/usr/bin/env python3

import prompt
import random
import sys
import prompt


def welcome_user():
    print("Welcome to Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, ", name, "!")
    return name

def is_even(number):
    return number % 2 == 0


def main():
    username = welcome_user()
    questions = []
    questions_num = 3
    max_random_number = 100
    random.seed()
    for _ in range(questions_num):
        questions.append(random.randrange(max_random_number))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for question in questions:
        print("Question:", question)
        answer = prompt.string("Your answer: ")
        if is_even(question):
            if answer == "yes":
                print("Correct!")
                continue
            else:
                print(f"'{answer}' is wrong answer ;(. \
                      Correct answer was 'yes'")
                print(f"Let's try again, {username}!")
                sys.exit(0)
        else:
            if answer == "no":
                print("Correct!")
                continue
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'")
                print(f"Let's try again, {username}!")
                sys.exit(0)

    print(f"Contgratulations, {username}!")


if __name__ == '__main__':
    main()
