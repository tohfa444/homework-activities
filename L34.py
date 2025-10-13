import random
import string

def generate_password(length=10):
    # Characters to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    # Combine all characters
    all_chars = lowercase + uppercase + digits

    # Randomly choose characters
    password = [random.choice(all_chars) for _ in range(length)]

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Generate a random password of length 12
password = generate_password(12)
print("Random Password:", password)
