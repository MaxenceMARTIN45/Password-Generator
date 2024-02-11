# Importing the random module for generating random values
import random

# Definition of lists for possible characters
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['~', '`', '!', '@', '#', '$', ' ', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ',', ':', ';', '%', "'", '<', '>', '.', '?', '/', '\\']
all_characters = [lowercase_letters, uppercase_letters, numbers, special_characters]

# Function to generate a random password
def generate(length):
    password = ''
    for _ in range(0, length):
        # Choosing a character type randomly
        type_index = random.randint(0, 3)  # inclusive bounds
        size = len(all_characters[type_index])
        # Choosing a character of that type randomly
        character_index = random.randint(0, size - 1)  # inclusive bounds
        character = all_characters[type_index][character_index]
        # Adding the character to the password
        password += character
    return password

# Calling the generate function with a password length of 40 characters
print(generate(40))
