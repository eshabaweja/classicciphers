import numpy as np

def encrypt(plaintext, key):
    """
    Encrypts a plaintext using the Hill cipher with the given key.

    Parameters:
        plaintext (str): The plaintext to be encrypted.
        key (numpy.ndarray): An n x n matrix representing the key of the Hill cipher.

    Returns:
        str: The ciphertext resulting from the encryption.
    """
    n = key.shape[0]
    # Convert the plaintext to a numpy array of integers
    plaintext = np.array([ord(c) - ord('a') for c in plaintext.lower() if c.isalpha()])
    # Pad the plaintext with zeros if necessary
    if len(plaintext) % n != 0:
        num_pad = n - len(plaintext) % n
        plaintext = np.append(plaintext, [0] * num_pad)
    # Reshape the plaintext as a matrix of column vectors
    plaintext = plaintext.reshape(-1, n)
    # Apply the Hill cipher encryption formula
    ciphertext = np.dot(plaintext, key) % 26
    # Convert the ciphertext to a string of letters
    ciphertext = ''.join([chr(c + ord('a')) for c in ciphertext.flatten()])
    return ciphertext

def decrypt(ciphertext, key):
    """
    Decrypts a ciphertext using the Hill cipher with the given key.

    Parameters:
        ciphertext (str): The ciphertext to be decrypted.
        key (numpy.ndarray): An n x n matrix representing the key of the Hill cipher.

    Returns:
        str: The plaintext resulting from the decryption.
    """
    n = key.shape[0]
    # Convert the ciphertext to a numpy array of integers
    ciphertext = np.array([ord(c) - ord('a') for c in ciphertext.lower() if c.isalpha()])
    # Reshape the ciphertext as a matrix of column vectors
    ciphertext = ciphertext.reshape(-1, n)
    # Compute the inverse of the key matrix
    key_inv = np.linalg.inv(key)
    # Apply the Hill cipher decryption formula
    plaintext = np.dot(ciphertext, key_inv) % 26
    # Convert the plaintext to a string of letters
    plaintext = ''.join([chr(c + ord('a')) for c in plaintext.flatten()])
    return plaintext