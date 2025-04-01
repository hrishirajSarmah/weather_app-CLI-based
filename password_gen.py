import random
import string

def generate_password(length):
    if length < 8:
        print("Password must be of at least 8 characters");
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))

    return password

try:
    length = int(input("Input required password length: "))
    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")
except ValueError:
    print("Invalid input, please enter a numeric value!")