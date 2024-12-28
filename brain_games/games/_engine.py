from typing import Callable

import prompt


def launch_game(question: str, run_logic: Callable[[str], bool]):
	name = welcome_user()
	play_game(name, question, run_logic)


def welcome_user() -> str:
	print('Welcome to the Brain Games!')
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	return name


def play_game(name: str, question: str, run_logic: Callable[[str], bool]):
	print(question)
	run_game_loop(name, run_logic)
    

def run_game_loop(name: str, run_logic: Callable[[str], bool]):
    count = 0
    while count < 3:
        if run_check(name, run_logic):
            count += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    

def run_check(name: str, run_logic: Callable[[str], bool]) -> bool:
	return run_logic(name)