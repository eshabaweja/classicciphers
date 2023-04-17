# a demo using caesar cipher
from classicciphers import caesar, hill
import numpy as np

plaintext = "HELLO WORLD"
key = 5

# encryption
ciphertext = caesar.encrypt(plaintext, key)
print(ciphertext)

# decryption
decrypted_plaintext = caesar.decrypt(ciphertext, key)
print(decrypted_plaintext)

######################################################

# a demo using Hill Cipher
key = np.array([[17, 17, 5],
                [21, 18, 21],
                [2, 2, 19]])

plaintext = "pay more money"

# Encrypt the plaintext message using the key matrix
ciphertext = hill.encrypt(plaintext, key)

# Print the ciphertext
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext using the key matrix
decrypted_text = hill.decrypt(ciphertext, key)

# Print the decrypted plaintext message
print("Decrypted plaintext:", decrypted_text)