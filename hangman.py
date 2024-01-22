
# Hangman game involves choosing a word, displaying underscores for each letter in the word, and allowing the player
# to guess letters until they either correctly guess the word or run out of attempts. here is implementation

# using random function, input, list, loop, conditional statement, len, lower

import random
import hangman_stages
import word_file


chosen_word = random.choice(word_file.word_list)
print(chosen_word)
display = []
lives = 6
game_over = False
for i in range(len(chosen_word)):
    display += '_'
print(display)
while not game_over:
    guessed_input = input("Guess a letter:").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_input:
            display[position] = guessed_input
    print(display)
    if guessed_input not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")
    if '_' not in display:
        print("you won")
    print(hangman_stages.stages[lives])