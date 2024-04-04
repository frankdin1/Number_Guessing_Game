import random


def number_of_attempts():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' or 'very hard': ")
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    elif difficulty == 'very hard':
        attempts = 2
    return attempts


def make_guess():
    guess = int(input("Make a guess: "))
    return guess


def check_guess(tries_left, u_guess, target):
    while tries_left > 0:
        if u_guess == target:
            print(f"You got it. The answer was {target}")
            break
        else:
            tries_left -= 1
            if tries_left == 0:
                break
            if u_guess < target:
                print("Too low.")
            else:
                print("Too high")
            print("Guess again.")
            print(f"You have {tries_left} attempts remaining to guess the number.")
            u_guess = make_guess()

    if tries_left == 0:
        print(f"You missed it. The answer was {target}")


def play_game():
    target_number = random.choice(range(101))
    print(f"target number: {target_number}")
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    attempts_left = number_of_attempts()
    print(f"You have {attempts_left} remaining to guess the number.")
    user_guess = make_guess()
    check_guess(attempts_left, user_guess, target_number)


play_game()
