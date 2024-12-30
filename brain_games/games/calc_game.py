import operator
import random

import prompt

from brain_games.games._engine import launch_game

OPERATIONS = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
MIN_NUMBER = 1
MAX_NUMBER = 100


def play():
	question = "What is the result of the expression?"
	launch_game(question, logic)


def logic(name: str) -> bool:
	first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
	second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
	operation_symbol, operation = random.choice(OPERATIONS)
	print(f"Question: {first_number} {operation_symbol} {second_number}")
	answer = prompt.string('Your answer: ')
	result = operation(first_number, second_number)
	if int(answer) != result:
		print(f"'{answer}' is wrong answer ;(. " 
		f"Correct answer was '{result}'.")
		return False
	print('Correct!')
	return True


if __name__ == '__main__':
	play()