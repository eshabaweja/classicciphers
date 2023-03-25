def encrypt(plaintext: str, key: str) -> str:
    """
    Encrypts plaintext using the Vigenere cipher with the given key.

    Args:
        plaintext: The plaintext to encrypt.
        key: The key to use for encryption.

    Returns:
        The encrypted ciphertext.
    """
    ciphertext = ""
    key_idx = 0
    for char in plaintext:
        if char.isalpha():
            key_char = key[key_idx % len(key)].lower()
            shift = ord(key_char) - ord('a')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_idx += 1
        else:
            ciphertext += char
    return ciphertext


def decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypts ciphertext using the Vigenere cipher with the given key.

    Args:
        ciphertext: The ciphertext to decrypt.
        key: The key to use for decryption.

    Returns:
        The decrypted plaintext.
    """
    plaintext = ""
    key_idx = 0
    for char in ciphertext:
        if char.isalpha():
            key_char = key[key_idx % len(key)].lower()
            shift = ord(key_char) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_idx += 1
        else:
            plaintext += char
    return plaintext
