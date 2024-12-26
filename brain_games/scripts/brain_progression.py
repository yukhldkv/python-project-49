import random
import prompt

from brain_games.cli import welcome_user


def main():
	print('Welcome to the Brain Games!')
	name = welcome_user()
	print("What number is missing in the progression?")
	count = 0
	while count < 3:
		if play(name):
			count += 1
		else:
			count = 0
	print(f'Congratulations, {name}!')


def play(name: str) -> bool:
	step = random.randint(1, 100)
	size = random.randint(5, 15)
	progression = []
	number = random.randint(0, 100)
	for i in range (0, size + 1):
		progression.append(number)
		number += step
	random_index = random.randint(0, len(progression))
	quiz_progression = []
	for i in range (0, len(progression)):
		if i == random_index:
			quiz_progression.append('..')
			continue
		quiz_progression.append(progression[i])
	print(quiz_progression)
	answer = prompt.string("Your answer: ")
	result = progression[random_index]
	if int(answer) != result:
		print(f"'{answer}' is wrong answer ;(." 
		f"Correct answer was '{result}'.")
		print(f"Let's try again, {name}!")
		return False
	print("Correct!")
	return True


if __name__ == '__main__':
    main()