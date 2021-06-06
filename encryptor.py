# SangTengkorak

from cryptography import fernet
from cryptography.fernet import Fernet

message = input("Please input string you want to convert : ")

# Using fernet to generate key
key = Fernet.generate_key()

# Instance the fernet class with the key
fernet = Fernet(key)

# Use fernet to hashing string
encMessage = fernet.encrypt(message.encode())

print(f"Original string : {message}")
print(f"Decrypted string : {encMessage}")

# Decrypt using fernet key
decMessage = fernet.decrypt(encMessage).decode()

print(f"Decrypted string : {decMessage}")