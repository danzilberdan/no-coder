import secrets
import string
import os


LENGTH = 32


def gen_secret():
    if os.path.exists("secret.key"):
        print("Warning: secret.key already exists. Do you want to override it? (y/n)")
        response = input().lower()
        if response != 'y':
            print("Operation cancelled.")
            return

    alphabet = string.ascii_letters + string.digits + string.punctuation
    secure_string = ''.join(secrets.choice(alphabet) for _ in range(LENGTH))

    with open("secret.key", "w") as f:
        f.write(secure_string)

    print("Secure string has been saved to secret.key")
