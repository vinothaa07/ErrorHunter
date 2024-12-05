# Program to Generate a Random Password
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(length))

length = int(input("Enter password length: "))
print(generate_password(length))
