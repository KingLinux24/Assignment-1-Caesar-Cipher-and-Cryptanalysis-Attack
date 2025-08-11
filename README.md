Cryptography Labs
Welcome to the Cryptography Labs repository! This repository serves as a collection of my practical implementations and exercises in the field of cryptography. It includes various ciphers, cryptographic algorithms, and cryptanalysis techniques explored during my studies.

Assignment 1: Caesar Cipher and Cryptanalysis Attack
This directory contains the implementation for Assignment 1, focusing on the classic Caesar Cipher and its Brute Force Cryptanalysis.

1.1 Problem Description
The assignment required the implementation of the Caesar Cipher, a simple substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. Key aspects included:

Taking plaintext and a numerical key from the user to generate ciphertext.

Implementing a decryption algorithm for the Caesar Cipher.

Developing a cryptanalysis attack (Brute Force Attack) to find the key from a given ciphertext by trying all possible shifts.

1.2 Implemented Features
encrypt_caesar(plaintext, key): Encrypts the given plaintext using the Caesar Cipher with the specified key.

Handles both uppercase and lowercase letters.

Preserves non-alphabetic characters (e.g., spaces, numbers, punctuation).

Supports keys greater than 26 by applying modulo 26 arithmetic.

decrypt_caesar(ciphertext, key): Decrypts the given ciphertext using the Caesar Cipher with the specified key.

Reuses the encrypt_caesar function by negating the key for inverse shifting.

brute_force_attack(ciphertext): Attempts to decrypt the ciphertext by trying all 26 possible Caesar cipher keys (0 through 25).

Prints all 26 possible plaintexts, allowing the user to identify the correct message.

Interactive Menu: A command-line interface (main() function) allowing users to choose between encryption, decryption, and brute-force attack.

1.3 How to Run
Clone the repository:

Bash

git clone https://github.com/KingLinux24/Assignment-1-Caesar-Cipher-and-Cryptanalysis-Attack.git
cd Cryptography-Labs/Assignment_1_Caesar_Cipher # Adjust if you put it in a subfolder
Run the Python script:

Bash

python caesar_cipher.py
Follow the on-screen menu prompts to encrypt, decrypt, or perform a brute-force attack.

1.4 Code Structure
caesar_cipher.py: Contains the main implementation of the Caesar cipher functions (encrypt_caesar, decrypt_caesar, brute_force_attack) and the interactive main menu.

1.5 Examples
Encryption Example:
Caesar Cipher Menu:
1. Encrypt
2. Decrypt
3. Brute Force Attack
4. Exit
Enter your choice (1-4): 1
Enter plaintext: Hello, World!
Enter key (integer): 3
Ciphertext: KHOOR, ZRUOG!
Decryption Example:
Caesar Cipher Menu:
1. Encrypt
2. Decrypt
3. Brute Force Attack
4. Exit
Enter your choice (1-4): 2
Enter ciphertext: KHOOR, ZRUOG!
Enter key (integer): 3
Plaintext: Hello, World!
Brute Force Attack Example:
Caesar Cipher Menu:
1. Encrypt
2. Decrypt
3. Brute Force Attack
4. Exit
Enter your choice (1-4): 3
Enter ciphertext for brute force attack: KHOOR, ZRUOG!
Brute Force Attack Results:
Key 0: KHOOR, ZRUOG!
Key 1: JGNNQ, YQTNF!
Key 2: IFMMP, XPSME!
Key 3: HELLO, WORLD!  <- This is the readable plaintext!
Key 4: GDKKN, VNKRC!
... (and so on for all 26 keys)
General Setup
Programming Language: Python 3.x

Dependencies: No external libraries required for Assignment 1. Future assignments may list specific dependencies in their respective directories or in a requirements.txt file at the root.

Future Labs/Assignments
This repository will be updated with implementations of other cryptographic concepts, including but not limited to:

Vigenere Cipher

Affine Cipher

Substitution Ciphers (Frequency Analysis)

Symmetric-key algorithms (AES, DES - conceptual or basic implementation)

Asymmetric-key algorithms (RSA - conceptual or basic implementation)

Hashing Functions (SHA, MD5)

Digital Signatures

Steganography (basic)
