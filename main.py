from rich.prompt import Prompt
from rich.console import Console
from random import choice
from words import word_list

SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE [/]\n'
PLAYER_INSTRUCTIONS = "You may start guessing\n"
GUESS_STATEMENT = "\nEnter your guess"
ALLOWED_GUESSES = 6


def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def check_guess(guess, answer):
    guessed = []  # list of guessed letters
    wordle_pattern = []  # Rich formatting for guesses
    # enumerate gives you a list of indexes and item at each index
    for i, letter in enumerate(guess):
        # Task 1: Check if the letter is in the correct place and update guessed with correct_place(letter)
        # HINT: you will also need to update wordle_pattern with the correct formatting for the guess! use the SQUARES dictionary

        # Task 2: Check if the letter is in the answer but not in the correct place and update guessed with correct_letter(letter)

        # Task 3: If the letter is not in the answer, update guessed with incorrect_letter(letter)


def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        # Task 4: Add a check to make sure the guess is a 5 letter word or has already been guessed

           else:
                console.print('[red]Please enter a 5-letter word!!\n[/]')
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        # Task 5: End the game if the guess is correct or if the player has used all their ALLOWED_GUESSES

    # Task 6: Check if the player has used all their guesses AND the guess is incorrect
    


# Don't change this
if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    game(console, chosen_word)
