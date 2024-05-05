import os
import random
import string
import time
import sys

def generate_password(length=15):
    special_characters = '&%$#@!'
    characters = string.ascii_letters + special_characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def write_to_file(password):
    file_path = r"C:\Users\Dymaxion\Desktop\Justin's Docs\Random Coding Projects\BF PasswordGuess\passwords.txt"
    with open(file_path, "a") as file:
        file.write(password + "\n")

def main():
    print("Welcome to the Potential Password Generator!")
    print("Press Enter to generate a new password or type 'quit' to exit.")

    file_path = r"C:\Users\Dymaxion\Desktop\Justin's Docs\Random Coding Projects\BF PasswordGuess\passwords.txt"
    if not os.path.exists(file_path):
        open(file_path, 'a').close()  # Create the file if it doesn't exist

    # Setting to specify the number of passwords to generate
    num_passwords = int(input("Enter the number of passwords to generate: "))
    print(f"Generating {num_passwords} passwords...")

    # Progress bar
    bar_length = 30
    for _ in range(num_passwords):
        sys.stdout.write("[")
        for i in range(bar_length):
            if i < (_ * bar_length) // num_passwords:
                sys.stdout.write("=")
            else:
                sys.stdout.write(" ")
        sys.stdout.write("] %d%%" % ((_ * 100) // num_passwords) + "\r")
        sys.stdout.flush()

        # Generate password
        password_length = random.randint(7, 15)
        password = generate_password(password_length)
        write_to_file(password)
        print(f"Password '{password}' written to passwords.txt")
        time.sleep(0.5)  # Pause for 0.5 seconds between generating passwords

    print("\nPassword generation complete!")

if __name__ == "__main__":
    main()
