from classicciphers import caesar, playfair, vigenere, railfence

# a demo using caesar cipher
print("\nA demo using caesar cipher.")
plaintext = "HELLO WORLD"
key = 5

ciphertext = caesar.encrypt(plaintext, key)
print("Plaintext: ",ciphertext)

decrypted_plaintext = caesar.decrypt(ciphertext, key)
print("Ciphertext: ",decrypted_plaintext)

#################################    #################################

# demo for playfair
print("\nA demo for playfair")
# Set up the key and plaintext
key = "secret"
plaintext = "MEETMEATTHEPARK"

ciphertext = playfair.encrypt(key, plaintext)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
decrypted_plaintext = playfair.encrypt(key,ciphertext,False)
print(f"Decrypted plaintext:{decrypted_plaintext}")


#################################    #################################

# demo for vignere
print("\nA demo for Vignere")
print(f"Plaintext: {plaintext}")
ciphertext = vigenere.encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted plaintext:{vigenere.decrypt(ciphertext, key)}")


#################################    #################################

# demo for railfence
print("\nA demo for Railfence")
message = "hello world"
key = 3
print(f"Plaintext: {message}")
ciphertext = railfence.encrypt(message, key)
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted plaintext:{railfence.decrypt(ciphertext, key)}")
