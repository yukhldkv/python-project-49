from typing import Callable

from brain_games.cli import welcome_user

MAX_ATTEMPTS = 3


def launch_game(question: str, run_logic: Callable[[], bool]):
	name = welcome_user()
	play_game(name, question, run_logic)


def play_game(name: str, question: str, run_logic: Callable[[], bool]):
	print(question)
	run_game_loop(name, run_logic)
    

def run_game_loop(name: str, run_logic: Callable[[], bool]):
    count = 0
    while count < MAX_ATTEMPTS:
        if run_check(name, run_logic):
            count += 1
        else:
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    

def run_check(name: str, run_logic: Callable[[], bool]) -> bool:
	return run_logic()