import random

import prompt

from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        if define_even(name):
            count += 1
        else:
            count = 0
    print(f'Congratulations, {name}!')


def define_even(name: str) -> bool:
    random_number = random.randint(1, 1000)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    if random_number % 2 == 0 and answer == 'yes' or \
        random_number % 2 != 0 and answer == 'no':
        print('Correct!')
        return True
    else:
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False


if __name__ == '__main__':
	main()