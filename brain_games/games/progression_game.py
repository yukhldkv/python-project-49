import random

import prompt

from brain_games.games._engine import launch_game

MIN_STEP = 1
MAX_STEP = 100
MIN_SIZE = 5
MAX_SIZE = 15
MIN_NUMBER = 1
MAX_NUMBER = 100


def play():
	question = "What number is missing in the progression?"
	launch_game(question, logic)
	

def logic(name: str) -> bool:
	progression = []
	step = random.randint(MIN_STEP, MAX_STEP)
	size = random.randint(MIN_SIZE, MAX_SIZE)
	element = random.randint(MIN_NUMBER, MAX_NUMBER)
	for i in range(0, size):
		progression.append(element)
		element += step
	random_index = random.randint(0, len(progression) - 1)
	question_prompt = "Question: "
	for i in range(0, len(progression)):
		if i == random_index:
			question_prompt += '.. '
			continue
		question_prompt += str(progression[i])
		question_prompt += " "
	print(question_prompt)
	answer = prompt.string("Your answer: ")
	result = progression[random_index]
	if int(answer) != result:
		print(f"'{answer}' is wrong answer ;(. " 
		f"Correct answer was '{result}'.")
		return False
	print("Correct!")
	return True


if __name__ == '__main__':
    play()