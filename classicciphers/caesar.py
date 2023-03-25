def encrypt(message, key):
    """
    Encrypts a message using the Caesar cipher with a given key.

    Parameters:
    message (str): The message to be encrypted.
    key (int): The number of positions to shift each letter in the message.

    Returns:
    str: The encrypted message.
    """
    encrypted = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + key
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def decrypt(message, key):
    """
    Decrypts a message using the Caesar cipher with a given key.

    Parameters:
    message (str): The message to be decrypted.
    key (int): The number of positions to shift each letter in the message.

    Returns:
    str: The decrypted message.
    """
    return encrypt(message, -key)