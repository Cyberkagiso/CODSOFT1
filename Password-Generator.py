import string
import random

def generate_password(length, complexity):
    password_characters = string.ascii_letters + string.digits
    if complexity == 1:
        password_characters = string.ascii_letters
    elif complexity == 2:
        password_characters = string.digits
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password
while True:
    length = int(input("Enter the length of the password: "))
    complexity = int(input("Enter the complexity of the password (1: letters only, 2: numbers only, 3: mixed): "))
    if complexity == 3:
        password = generate_password(length, 0)
    else:
        password = generate_password(length, complexity)
    print("Generated password:",password)