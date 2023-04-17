# a demo using caesar cipher
from classicciphers import caesar, playfair
import numpy as np

plaintext = "HELLO WORLD"
key = 5

ciphertext = caesar.encrypt(plaintext, key)
print("Plaintext: ",ciphertext)

decrypted_plaintext = caesar.decrypt(ciphertext, key)
print("Ciphertext: ",decrypted_plaintext)

#################################    #################################

# demo for playfair
# Set up the key and plaintext
key = "secret"
plaintext = "MEETMEATTHEPARK"

# Encrypt the plaintext
ciphertext = playfair.encrypt(key, plaintext)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_plaintext = playfair.encrypt(key,ciphertext,False)
print(f"Decrypted plaintext:{decrypted_plaintext}")
