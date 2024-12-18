import prompt


def welcome_user() -> str:
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name