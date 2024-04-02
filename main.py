import random


def number_of_attempts():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    return attempts


def make_guess():
    guess = int(input("Make a guess: "))
    return guess
def play_game():
    target_number = random.choice(range(101))
    print(f"target number: {target_number}")
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    attempts_left = number_of_attempts()
    print(f"You have {attempts_left} remaining to guess the number.")
    user_guess = make_guess()

    while(attempts_left > 0):
        if user_guess == target_number:
            print(f"You got it. The answer was {target_number}")
            break
        else:
            attempts_left -= 1
            if attempts_left == 0:
                break
            print(f"You have {attempts_left} attempts remaining to guess the number.")
            user_guess = make_guess()


    if attempts_left == 0:
        print(f"You missed it. The answer was {target_number}")


play_game()
