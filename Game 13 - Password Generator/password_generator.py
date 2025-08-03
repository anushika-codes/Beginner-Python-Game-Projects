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
    
def check_strength(length, use_upper, use_lower, use_digits, use_symbols):
    score = 0
    if length >= 8:
        score += 1
    if use_upper:
        score += 1
    if use_lower:
        score += 1
    if use_digits:
        score += 1
    if use_symbols:
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

print("Advanced Password Generator")
print("----------------------------")

# Ask for number of passwords
count = int(input("How many passwords do you want to generate? "))

for i in range(count):
    print(f"\nGenerating password #{i+1}")

    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    
    if "Error" in password:
        print(password)
    else:
        strength = check_strength(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"Generated Password: {password}")
        print(f"Password Strength: {strength}")

