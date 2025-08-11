# Assignment 1 : Ceaser Cipher and Cryptanalysis Attack
# Implement Classical - Caesar Cipher:
#1. Take plaintext and key inputs from the user and generate ciphertext. 
#2. Also, implement a decryption algorithm. 
#3. Implement Cryptanalysis attack: Brute Force Attack on given ciphertext and try to find the key for the same.




def encrypt_caesar(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - base + shift) % 26 + base)
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, key):
    return encrypt_caesar(ciphertext, -key)

def brute_force_attack(ciphertext):
    print("Brute Force Attack Results:")
    for key in range(26):
        decrypted_text = decrypt_caesar(ciphertext, key)
        print(f"Key {key}: {decrypted_text}")

def main():
    while True:
        print("\nCaesar Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Brute Force Attack")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            plaintext = input("Enter plaintext: ")
            key = int(input("Enter key (integer): "))
            ciphertext = encrypt_caesar(plaintext, key)
            print(f"Ciphertext: {ciphertext}")

        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            key = int(input("Enter key (integer): "))
            plaintext = decrypt_caesar(ciphertext, key)
            print(f"Plaintext: {plaintext}")

        elif choice == '3':
            ciphertext = input("Enter ciphertext for brute force attack: ")
            brute_force_attack(ciphertext)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
