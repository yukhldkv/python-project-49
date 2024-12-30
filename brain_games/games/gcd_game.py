import random

import prompt

from brain_games.games._engine import launch_game

MIN_NUMBER = 1
MAX_NUMBER = 100


def play():
	question = "Find the greatest common divisor of given numbers.."
	launch_game(question, logic)


def get_gcd(first: int, second: int) -> int:
	gcd = 1
	for i in range(2, min(first, second) + 1):
		if first % i == 0 and second % i == 0:
			gcd = i
	return gcd


def logic() -> bool:
	first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
	second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
	print(f"Question: {first_number} {second_number}")
	result = get_gcd(first_number, second_number)
	answer = prompt.string("Your answer: ")
	if int(answer) != result:
		print(f"'{answer}' is wrong answer ;(. " 
		f"Correct answer was '{result}'.")
		return False
	print("Correct!")
	return True


if __name__ == '__main__':
	play()