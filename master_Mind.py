#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("MasterMind")

import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]

def generate_code(use_colors=False):
    if use_colors:
        return [random.choice(COLORS) for _ in range(4)]
    else:
        return [str(random.randint(1, 6)) for _ in range(4)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))

    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)

    return black_Pegs, white_Pegs

def show_Secret(mystery):
    print(mystery)

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Enter 4 digits (1-6) or 4 colors separated by spaces. You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = None
        while guess is None:
            raw_guess = input(f"Attempt {attempt}: ").strip()
            guess = parse_guess(raw_guess)
            if guess is None:
                print("Invalid input. Enter 4 digits (1-6) or 4 colors separated by spaces.")

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()

