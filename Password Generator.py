import random
import string

def generate_password(length):
    # Define the characters to be used for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def main():
    print("Welcome to the Password Generator!")

    # Prompt the user for password length
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password: " + password)


if __name__ == "__main__":
    main()
