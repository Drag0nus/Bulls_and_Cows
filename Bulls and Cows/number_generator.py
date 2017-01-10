import random

def generate_secret_number(digit):
    secret_number = ''
    while len(secret_number) < digit:
        random_number = str(random.randint(0, 9))
        if random_number not in secret_number:
            secret_number += random_number
        else:
            continue
        if len(secret_number) == 4:
            break
    return secret_number
