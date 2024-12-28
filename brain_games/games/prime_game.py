import random

import prompt

from brain_games.games._engine import launch_game


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


def logic(name: str) -> bool:
	random_number = random.randint(1, 1000)
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
		print(f"'{answer}' is wrong answer ;(."
		f"Correct answer was '{correct_answer}'.")
	print(f"Let's try again, {name}!")
	return False


if __name__ == '__main__':
	play()