# The Fernet cipher is a symmetric encryption algorithm based on AES.
# It encrypts data using a key derived from a passphrase and includes authentication to ensure data integrity.
# Each token includes a timestamp to prevent replay attacks.
# It's easy to use and popular in Python applications due to its inclusion in the cryptography library.

from cryptography.fernet import Fernet


def encrypt(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message


def decrypt(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message
