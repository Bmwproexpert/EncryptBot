import string

from pyDes import des, PAD_PKCS5
import binascii


def encrypt(key, word):
    # Initialize DES cipher with the key
    cipher = des(key, padmode=PAD_PKCS5)

    # Convert word to bytes
    word_bytes = word.encode('utf-8')

    # Encrypt the word
    encrypted_bytes = cipher.encrypt(word_bytes)

    # Convert encrypted bytes to hexadecimal representation
    encrypted_hex = binascii.hexlify(encrypted_bytes)

    return encrypted_hex.decode('utf-8')


def decrypt(key, encrypted_word):
    # Initialize DES cipher with the key
    cipher = des(key, padmode=PAD_PKCS5)

    # Encrypted word (hexadecimal representation)
    encrypted_hex = encrypted_word

    # Convert encrypted hexadecimal to bytes
    encrypted_bytes = binascii.unhexlify(encrypted_hex)

    # Decrypt the encrypted bytes
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # Convert decrypted bytes to string
    decrypted_word = decrypted_bytes.decode('utf-8')

    return decrypted_word
