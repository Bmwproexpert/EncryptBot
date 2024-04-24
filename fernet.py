from cryptography.fernet import Fernet

# Barbie wants to encrypt her messages using Fernet symmetric encryption
def encrypt(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Barbie decrypts a message using the hardcoded key
def decrypt(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message
