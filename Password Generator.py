import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for i in range(length))
    return password

#Example usage:
password_length = 14 #can adjust length of the password as needed
random_password = generate_password(password_length)
print("Random Password:", random_password)