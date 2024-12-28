import random

import prompt

from brain_games.games._engine import launch_game


def play():
	question = "What number is missing in the progression?"
	launch_game(question, logic)
	

def logic(name: str) -> bool:
	step = random.randint(1, 100)
	size = random.randint(5, 15)
	progression = []
	number = random.randint(0, 100)
	for i in range(0, size + 1):
		progression.append(number)
		number += step
	random_index = random.randint(0, len(progression))
	quiz_progression = []
	for i in range(0, len(progression)):
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
    play()