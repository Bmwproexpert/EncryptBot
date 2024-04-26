# The Caesar cipher shifts each letter in the plaintext by a fixed number of positions down the alphabet.
# It's a basic substitution cipher where the same key (shift value) is used for both encryption and decryption.
# However, due to its simplicity, it's highly vulnerable to brute-force and frequency analysis attacks.
# This algorithm skips numbers and do not work with russian expressions
import re


def is_valid(s):
    reg_exp = re.compile(r"^[a-zA-Z0-9?><;,{}[\]\-_+=!@#$%^&*|']*$")
    return reg_exp.match(s)


def encrypt(message, key):
    assert is_valid(message)

    encrypted_message = ""
    for char in message:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift uppercase letters by the key value
            encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift lowercase letters by the key value
            encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message


def decrypt(encrypted_message, key):
    assert is_valid(encrypted_message)

    decrypted_message = ""
    for char in encrypted_message:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift uppercase letters backwards by the key value
            decrypted_char = chr((ord(char) - 65 - key) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift lowercase letters backwards by the key value
            decrypted_char = chr((ord(char) - 97 - key) % 26 + 97)
        else:
            # If the character is not a letter, leave it unchanged
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message
