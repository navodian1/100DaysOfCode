import random

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5


def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_ATTEMPT
    elif level_chosen == 'hard':
        return HARD_ATTEMPT
    else:
        return


def check_answer(guessed_number1, answer1, attempt):
    if guessed_number1 < answer1:
        print("Your guess is lower")
        return attempt - 1
    elif guessed_number1 > answer1:
        print("your number is higher")
        return attempt - 1
    else:
        print(f"your guess is right ....the answer is {answer1}")


def game():
    print("let me think of a number between 1 to 50.")
    answer = random.randint(1, 50)
    level = input("choose level of difficulty...Type 'easy' or 'hard': ")
    attempt = set_difficulty(level)
    if attempt != EASY_ATTEMPT and attempt != HARD_ATTEMPT:
        print("You entered wrong difficulty level....play again")
        game()
    guessed_number = 0
    while guessed_number != answer:
        print(f"you have {attempt} attempts remaining to guess the number")
        guessed_number = int(input("guess the number: "))
        attempt = check_answer(guessed_number, answer, attempt)
        if attempt == 0:
            print("you are out of guess")
            return
        elif guessed_number != answer:
            print("Guess again..........")


game()
