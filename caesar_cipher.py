# Choose a number between 1 and 25. This will be your “shift” value.
# Write down the letters of the alphabet in order, from a to z
# do not enter only numbers to encrypt or decrypt
# Shift each letter of the alphabet by the “shift” value.


import string
import sys

ALPHABET_SIZE = 26
alpha = sorted(set(string.ascii_lowercase))


def encryption(action, plaintext, shiftkey):
    cipher_text = ""
    if action == "decrypt":
        shiftkey *= -1
    for char in plaintext:
        if char in alpha:
            position = alpha.index(char)
            new_position = (position + shiftkey) % ALPHABET_SIZE
            cipher_text += alpha[new_position]
        else:
            cipher_text += char
    print(cipher_text)


def validate_message(text):
    if len(text) < 3 or text.isdigit():
        sys.exit("Condition not met, either text is too short or contains only digits")


def validate_shift_key(shift):
    try:
        shift = int(shift)
        if not (-ALPHABET_SIZE < shift < ALPHABET_SIZE):
            sys.exit("Invalid shift key. It should be within the range of -25 to 25.")
    except ValueError:
        sys.exit("Invalid shift key. Please enter an integer.")


end_program = ""
while not end_program:
    to_do = input("Type 'Encrypt' for encryption or type 'Decrypt' for decryption: ").lower()
    if to_do not in ['encrypt', 'decrypt']:
        sys.exit("Invalid Input")
    text = input("Type your message:\n")
    validate_message(text)
    shift = int(input("type shifting number:\n"))
    validate_shift_key(shift)
    encryption(to_do, plaintext=text, shiftkey=shift)

    play_again = input("Do you want to encrypt or decrypt again: Y or N").lower()
    if play_again == 'n':
        end_program = True
        print("Have a nice day!")
