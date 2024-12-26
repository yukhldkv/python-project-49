import operator
import random

import prompt

from brain_games.cli import welcome_user


def main():
	print('Welcome to the Brain Games!')
	name = welcome_user()
	print("What is the result of the expression?")
	count = 0
	while count < 3:
		if calc(name):
			count += 1
		else:
			count = 0
	print(f'Congratulations, {name}!')
	

def calc(name: str) -> bool:
	first = random.randint(1, 100)
	second = random.randint(1, 100)
	operations = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
	symbol, operation = random.choice(operations)
	print(f"Question: {first} {symbol} {second}")
	answer = prompt.string('Your answer: ')
	result = operation(first, second)
	if int(answer) != result:
		print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
		print(f"Let's try again, {name}!")
		return False
	print('Correct!')
	return True


if __name__ == '__main__':
	main()