import random
import string

def generate_password(length):
    # Define the character sets to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated password:", password)

if __name__ == "__main__":
    main()
