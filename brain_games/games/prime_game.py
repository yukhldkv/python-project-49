import random

import prompt

from brain_games.games._engine import launch_game

MIN_NUMBER = 1
MAX_NUMBER = 1000


def play():
    question = ("Answer \"yes\" if given number is prime. "
                "Otherwise answer \"no\".")
    launch_game(question, logic)
	
    
def is_prime(number: int) -> bool:
	if number == 1: 
		return False
	if number <= 3:
		return True
	for i in range(2, number):
		if number % i == 0:
			return False
	return True


def logic() -> bool:
	random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
	print(f"Question: {random_number}")
	answer = prompt.string("Your answer: ")
	if is_prime(random_number) and answer == 'yes' or \
        not (is_prime(random_number)) and answer == 'no':
		print('Correct!')
		return True
	if is_prime(random_number):
		correct_answer = 'yes'
	else:
		correct_answer = 'no'
		print(f"'{answer}' is wrong answer ;(. "
		f"Correct answer was '{correct_answer}'.")
	return False


if __name__ == '__main__':
	play()