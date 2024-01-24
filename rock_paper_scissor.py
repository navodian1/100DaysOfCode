# we will program this tomorrow
"""
rock wins against scissor
scissor wins against paper
paper wins against rock

I have tried validation here using try and except block and compare user input range by if condition
used Enum also
"""
import random
import sys
from enum import Enum


class Rps(Enum):
    ROCK = 1
    SCISSOR = 2
    PAPER = 3
"""

in spite of creating class we can do this by creating a function also

def get_choice_string(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Scissor"
    elif choice == 3:
        return "Paper"
    else:
        return "Invalid choice"

"""

try:
    userInput = int(input("Enter your choice:\n1.Rock\n2.Scissor\n3.Paper\n:"))
except ValueError:
    sys.exit("Invalid input, enter only integers")  # as exit() is command line only function,
    # better to use sys.exit() in program
if userInput not in [1, 2, 3]:
    sys.exit("you must enter number 1,2 and 3 only")
compChoice = int(random.choice("123"))
if userInput == compChoice:
    print("it's a tie 🤝")
elif (userInput, compChoice) in [(1, 2), (2, 3), (3, 1)]:
    print("user win! 🏆")
else:
    print("computer win 💻")

print(f"you chose:{str(Rps(userInput)).replace('Rps.', '')}, computer chose:{str(Rps(compChoice)).replace('Rps.', '')}")
