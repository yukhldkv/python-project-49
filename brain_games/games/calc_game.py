import operator
import random

import prompt

from brain_games.games._engine import launch_game


def play():
	question = "What is the result of the expression?"
	launch_game(question, logic)


OPERATIONS = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]


def logic(name: str) -> bool:
	first_number = random.randint(1, 100)
	second_number = random.randint(1, 100)
	operation_symbol, operation = random.choice(OPERATIONS)
	print(f"Question: {first_number} {operation_symbol} {second_number}")
	answer = prompt.string('Your answer: ')
	result = operation(first_number, second_number)
	if int(answer) != result:
		print(f"'{answer}' is wrong answer ;(." 
		f"Correct answer was '{result}'.")
		print(f"Let's try again, {name}!")
		return False
	print('Correct!')
	return True


if __name__ == '__main__':
	play()