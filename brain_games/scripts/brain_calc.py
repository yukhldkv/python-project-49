import operator
import random

import prompt

from brain_games.cli import welcome_user

name = ''


def main():
	print('Welcome to the Brain Games!')
	name = welcome_user()
	print("What is the result of the expression?")
	count = 0
	while count < 3:
		if play(name):
			count += 1
		else:
			count = 0
	print(f'Congratulations, {name}!')
	

OPERATIONS = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]


def play(name: str) -> bool:
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
	main()