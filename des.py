# DES (Data Encryption Standard) is a symmetric block cipher algorithm. It divides data into fixed-size blocks and
# applies multiple rounds of substitutions and permutations based on a 56-bit key. Despite its historical
# significance, DES is now vulnerable to brute-force attacks due to its short key length.

from pyDes import des, PAD_PKCS5
import binascii


def encrypt(key, word):
    cipher = des(key, padmode=PAD_PKCS5)

    word_bytes = word.encode('utf-8')

    encrypted_bytes = cipher.encrypt(word_bytes)

    encrypted_hex = binascii.hexlify(encrypted_bytes)

    return encrypted_hex.decode('utf-8')


def decrypt(key, encrypted_word):
    cipher = des(key, padmode=PAD_PKCS5)

    encrypted_hex = encrypted_word

    encrypted_bytes = binascii.unhexlify(encrypted_hex)

    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    decrypted_word = decrypted_bytes.decode('utf-8')

    return decrypted_word
