def encrypt(message, key):
    """
    Encrypts a message using the Substitution cipher.

    Args:
        message (str): The message to be encrypted.
        key (str): The key to use for encryption. This should be a string
            containing all 26 letters of the alphabet in some scrambled order.

    Returns:
        str: The encrypted message.

    Examples:
        >>> encrypt('HELLO', 'XPMGTDHLYONZBWEARKJUFSCIQV')
        'DSCWW'
        >>> encrypt('SECRET MESSAGE', 'KRYPTOS')
        'PEFZEA LYRYYBS'
    """
    # Create a dictionary that maps each letter to its corresponding
    # letter in the key
    letter_map = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', key))
    
    # Use the letter_map to encrypt the message
    encrypted_message = ''.join(letter_map.get(c, c) for c in message.upper())
    
    return encrypted_message

def decrypt(message, key):
    """
    Decrypts a message using the Substitution cipher.

    Args:
        message (str): The message to be decrypted.
        key (str): The key to use for decryption. This should be a string
            containing all 26 letters of the alphabet in the same order as
            used for encryption.

    Returns:
        str: The decrypted message.

    Examples:
        >>> decrypt('DSCWW', 'XPMGTDHLYONZBWEARKJUFSCIQV')
        'HELLO'
        >>> decrypt('PEFZEA LYRYYBS', 'KRYPTOS')
        'SECRET MESSAGE'
    """
    # Create a dictionary that maps each letter in the key to its
    # corresponding letter in the alphabet
    letter_map = dict(zip(key.upper(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    # Use the letter_map to decrypt the message
    decrypted_message = ''.join(letter_map.get(c, c) for c in message.upper())
    
    return decrypted_message
