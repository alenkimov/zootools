import random
import string


def generate_string(length):
    characters = string.ascii_lowercase + string.digits
    return random.choice(string.ascii_lowercase) + ''.join(random.choice(characters) for _ in range(length))


def generate_email(domain='gmail.com'):
    username = generate_string(random.randint(8, 16))
    return f"{username}@{domain}"
