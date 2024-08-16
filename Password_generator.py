import secrets  # Importing the secrets module for secure random number generation
import string   # Importing the string module for string constants

def generate_password(length):
    # Define the set of characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password by randomly choosing characters from 'characters' set
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

# Prompt the user to input the desired length of the password
length = int(input("Enter the desired length of the password: "))

# Generate and display the password of the specified length
print("Generated Password : ", generate_password(length))
