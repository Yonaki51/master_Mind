#!/bin/python3
# MasterMind
# by ICTROCN
# v1.02
# Last mod: admin auth + keuze cijfers of kleurwoorden

print("MasterMind")
import hashlib
import random

ADMIN_PASSWORD_HASH = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"
COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]

def check_Admin_Password() -> bool:
    pwd = input("Enter admin password: ")
    return hashlib.sha256(pwd.encode()).hexdigest() == ADMIN_PASSWORD_HASH

def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess)) 
    secret_Counts = {}
    guess_Counts = {}
    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1
    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    return black_Pegs, white_Pegs

def show_Secret(mystery, use_words):
    if use_words:
        print([COLORS[int(d) - 1] for d in mystery])
    else:
        print(mystery)

def parse_Guess(raw, use_words):
    if use_words:
        tokens = raw.strip().lower().split()
        if len(tokens) == 4 and all(t in COLORS for t in tokens):
            return [str(COLORS.index(t) + 1) for t in tokens]
    else:
        if len(raw.strip()) == 4 and all(c in "123456" for c in raw.strip()):
            return list(raw.strip())
    return None

def play_Mastermind():
    print("Welcome to Mastermind!")

    mode = ""
    while mode not in ("1", "2"):
        mode = input("Do you want to guess with (1) digits or (2) color words? ").strip()
    use_words = mode == "2"

    if use_words:
        print(f"Use 4 color words per guess: {', '.join(COLORS)}")
        print("Example: red blue green yellow")
    else:
        print("Guess the 4-digit code. Each digit is from 1 to 6.")

    print("You have 10 attempts.")
    secret_Code = generate_Code()

    for attempt in range(1, 11):
        parsed = None
        while parsed is None:
            raw = input(f"Attempt {attempt}: ").strip()

            if raw.lower() == "cheat":
                if check_Admin_Password():
                    show_Secret(secret_Code, use_words)
                else:
                    print("Incorrect password. Access denied.")
                continue

            parsed = parse_Guess(raw, use_words)
            if parsed is None:
                if use_words:
                    print(f"Invalid input. Enter 4 color words: {', '.join(COLORS)}")
                else:
                    print("Invalid input. Enter 4 digits, each from 1 to 6.")

        black, white = get_Feedback(secret_Code, parsed)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: ", end="")
            show_Secret(secret_Code, use_words)
            return

    print(f"Sorry, you've used all attempts. The correct code was: ", end="")
    show_Secret(secret_Code, use_words)

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Play again (Y/N)? ").upper()