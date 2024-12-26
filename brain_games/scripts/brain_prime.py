import random
import prompt

from brain_games.cli import welcome_user


def main():
	print('Welcome to the Brain Games!')
	name = welcome_user()
	print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
	count = 0
	while count < 3:
		if play(name):
			count += 1
		else:
			count = 0
	print(f'Congratulations, {name}!')


def is_prime(number: int) -> bool:
	if number == 1: 
		return False
	if number <= 3:
		return True
	for i in range (2, number):
		if number % i == 0:
			return False
	print('prime')
	return True

def play(name: str) -> bool:
	random_number = random.randint(1, 1000)
	print(f"Question: {random_number}")
	answer = prompt.string("Your answer: ")
	if is_prime(random_number) and answer == 'yes' or \
        not(is_prime(random_number)) and answer == 'no':
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
    main()