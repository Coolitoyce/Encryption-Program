import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)

key = chars.copy()
random.shuffle(key)


# ENCRYPT
def encrypt_msg():
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print("=======")
    print(f"Original message: {plain_text}")
    print(f"Encrypted message: {cipher_text}")
    print("=======")
    main()


# DECRYPT
def decrypt_msg():
    cipher_text = input("Enter a message to decrypt: ")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    print("=======")
    print(f"Encrypted message: {cipher_text}")
    print(f"Original message: {plain_text}")
    print("=======")
    main()


# MAIN
def main():
    while True:
        action = input(
            """1. Encrypt
2. Decrypt
3. Exit
-> """
        )

        if action == "1":
            encrypt_msg()
            break

        elif action == "2":
            decrypt_msg()
            break

        elif action == "3":
            print("=======")
            print("Exitting program.")
            print("=======")
            break

        else:
            print("Please pick 1, 2, or 3.")


main()
