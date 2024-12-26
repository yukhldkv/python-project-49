import random
import prompt

from brain_games.cli import welcome_user


def main():
	print('Welcome to the Brain Games!')
	name = welcome_user()
	print("Find the greatest common divisor of given numbers.")
	count = 0
	while count < 3:
		if play(name):
			count += 1
		else:
			count = 0
	print(f'Congratulations, {name}!')


def get_lesser_number(first: int, second: int):
	return first if first <= second else second


def get_gcd(first: int, second: int) -> int:
	gcd = 1
	for i in range (2, get_lesser_number(first, second) + 1):
		if first % i == 0 and second % i == 0:
			gcd = i
	return gcd


def play(name: str) -> bool:
	first_number = random.randint(1, 100)
	second_number = random.randint(1, 100)
	print(f"Question: {first_number} {second_number}")
	result = get_gcd(first_number, second_number)
	answer = prompt.string("Your answer: ")
	if int(answer) != result:
		print(f"'{answer}' is wrong answer ;(." 
		f"Correct answer was '{result}'.")
		print(f"Let's try again, {name}!")
		return False
	print("Correct!")
	return True


if __name__ == '__main__':
	main()