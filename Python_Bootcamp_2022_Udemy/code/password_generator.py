import random
import string

def generate_password():
    # Create a list of allowed characters for the password
    characters = string.ascii_letters + string.digits + "@#$%"
    # Generate a random password of length 8 using the allowed characterS
    password = 'H@rd$hell' + ''.join(random.choice(characters) for i in range(8))
    return password
# Generate a new password.
password = generate_password()
print(password)