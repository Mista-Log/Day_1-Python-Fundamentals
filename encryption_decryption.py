import random

def encrypt(message, key):
  encrypted_message = ""
  for char in message:
    encrypted_char = chr(ord(char) + key)
    encrypted_message += encrypted_char
  return encrypted_message

def decrypt(encrypted_message, key):
  decrypted_message = ""
  for char in encrypted_message:
    decrypted_char = chr(ord(char) - key)
    decrypted_message += decrypted_char
  return decrypted_message

def main():
  print("Welcome to the Encryption/Decryption Game!")

  while True:
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      message = input("Enter the message to encrypt: ")
      key = random.randint(1, 25)  # Generate a random key between 1 and 25
      encrypted_message = encrypt(message, key)
      print("Encrypted message:", encrypted_message)

    elif choice == "2":
      encrypted_message = input("Enter the encrypted message to decrypt: ")
      key = random.randint(1, 25)  # Generate a random key between 1 and 25
      decrypted_message = decrypt(encrypted_message, key)
      print("Decrypted message:", decrypted_message)

    elif choice == "3":
      print("Exiting the game...")
      break

    else:
      print("Invalid choice. Please enter 1, 2, or 3.")


