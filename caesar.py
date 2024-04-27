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
        if char.isupper():
            encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message


def decrypt(encrypted_message, key):
    assert is_valid(encrypted_message)

    decrypted_message = ""
    for char in encrypted_message:
        if char.isupper():
            decrypted_char = chr((ord(char) - 65 - key) % 26 + 65)
        elif char.islower():
            decrypted_char = chr((ord(char) - 97 - key) % 26 + 97)
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message
