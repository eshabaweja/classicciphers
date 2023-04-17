# a demo using caesar cipher
from classicciphers import caesar

plaintext = "HELLO WORLD"
key = 5

ciphertext = caesar.encrypt(plaintext, key)
print(ciphertext)

decrypted_plaintext = caesar.decrypt(ciphertext, key)
print(decrypted_plaintext)