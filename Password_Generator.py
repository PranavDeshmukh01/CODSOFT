import random
import string

def generate_password(length):
     
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    password_characters = random.sample(all_characters, length)

    password = ''.join(password_characters)

    return password

try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()


password = generate_password(length)
print("Generated Password:", password)
