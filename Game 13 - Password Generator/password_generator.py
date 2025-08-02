import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_pool = ''
    
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: No character types selected."

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password
