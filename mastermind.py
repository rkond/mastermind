#!/usr/bin/python3
"""
A simple implementation fof Mastermind game, written as a tech evaluation assignment for a job application.
(c) 2022 Rostislav Kondartenko
"""
from typing import List, Tuple
from random import choices

import argparse

# Defaults
N_LETTERS = 6
CODE_LENGTH = 4
MAX_GUESSES = 12
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def get_matches(code: List[str], guess: List[str]) -> Tuple[int, int]:
    code_length = len(code)
    correct_position = 0
    correct_letter = 0
    # Copy the code so we can discard the letters we already matched
    code_copy = list(code)

    for index in range(code_length):
        if code_copy[index] == guess[index]:
            correct_position += 1
            code_copy[index] = ""  # So that we don't match it with repeats in other position
    for index in range(code_length):
        if code[index] != guess[index] and guess[index] in code_copy:
            correct_letter += 1
            code_copy[code_copy.index(guess[index])] = ""  # So that we don't match it with repeats in other position
    return correct_position, correct_letter


def run_game(n_letters: int, code_length: int, max_guesses: int) -> None:
    letters = ALPHABET.upper()[:n_letters]
    rules = f"""
    The goal of the game is to guess the code, set by the game.
    The code is {code_length} letters long and consists of letters:
    {', '.join(letters)}
    Letters may repeat.
    You will be given {max_guesses} to do so. After each guess the game will tell you two numbers:
    1. Number of letters in your guess that match the code by value and position
    2. Number of letters in your guess that match letter in the code in some other postion

    N.B. each letter in the code will me matched only once with some letter in your guess, i.e.
    if the code is "A A B B", and guess is "A A A B", 3 letters are correct and 0 match a letter in
    a different position.
    """

    code = choices(letters, k=code_length)
    n_guesses = 0
    guess: List[str] = []

    while n_guesses < max_guesses:
        try:
            guess_str = input("Your guess (Ctrl+C to exit, ? for help): ").upper()
            print('\033[1A\033[K')
        except KeyboardInterrupt:
            print("\nGood bye!")
            return
        if guess_str == '?':
            print(rules)
            continue
        guess = []
        for char in guess_str:
            if char in letters:
                guess.append(char)
            if len(guess) == code_length:
                break
        if len(guess) != code_length:
            print("Not enough letters in your guess, try again")
            continue
        n_guesses += 1
        if guess == code:
            print(f"Congradulations! The code was {' '.join(guess)}")
            return
        correct_position, correct_letter = get_matches(code, guess)
        print(f"Guess {n_guesses} of {max_guesses}: {' '.join(guess)}. {correct_position} correct, {correct_letter} in different position")  # noqa: E501
    print(f"No more guesses. You lost. The code was {' '.join(code)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mastermind game')
    parser.add_argument('--letters', dest='n_letters', action='store', type=int, default=N_LETTERS, help=f"How many letters to choose from (default {N_LETTERS})")  # noqa: E501
    parser.add_argument('--length', dest='code_length', action='store', type=int, default=CODE_LENGTH, help=f"Code length (default {CODE_LENGTH})")  # noqa: E501
    parser.add_argument('--guesses', dest='max_guesses', action='store', type=int, default=MAX_GUESSES, help=f"Maximum number of guesses (default {MAX_GUESSES})")  # noqa: E501
    args = parser.parse_args()
    parameters_ok = True
    if not (2 <= args.n_letters <= len(ALPHABET)):
        print("Invalid value for --n_letters: shoul be between 2 and 26")
        parameters_ok = False
    if not (2 <= args.code_length <= 12):
        print("Invalid value for --code_length: shoul be between 2 and 12")
        parameters_ok = False
    if not (1 <= args.max_guesses <= 999):
        print("Invalid value for --guesses: shoul be between 1 and 999")
        parameters_ok = False
    if parameters_ok:
        run_game(args.n_letters, args.code_length, args.max_guesses)
