import random

import prompt

from brain_games.games._engine import launch_game


def play():
	question = "Answer \"yes\" if the number is even, otherwise answer \"no\"."
	launch_game(question, logic)
     

def logic(name: str) -> bool:
    random_number = random.randint(1, 1000)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    if random_number % 2 == 0 and answer == 'yes' or \
        random_number % 2 != 0 and answer == 'no':
        print('Correct!')
        return True
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f"'{answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.")
    print(f"Let's try again, {name}!")
    return False


if __name__ == '__main__':
	play()