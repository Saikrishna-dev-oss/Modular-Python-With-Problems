import random
import string

def generate_pass(length = 8):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))   

    return password

print(generate_pass(9))