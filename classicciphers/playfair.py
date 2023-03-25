def encrypt(plaintext, key):
    """
    Encrypt plaintext using the Playfair cipher and the given key.

    The plaintext is divided into pairs of letters and each pair is encrypted
    using the 5x5 matrix generated from the key.

    Args:
        plaintext (str): The plaintext to encrypt.
        key (str): The key to use for the 5x5 matrix.

    Returns:
        str: The encrypted ciphertext.

    """
    matrix = generate_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')

    # add an 'X' to the end if the length of plaintext is odd
    if len(plaintext) % 2 == 1:
        plaintext += 'X'

    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i:i+2]

        # find the positions of the letters in the matrix
        row1, col1 = find_letter(a, matrix)
        row2, col2 = find_letter(b, matrix)

        # encrypt the pair of letters
        if row1 == row2:
            # letters are in the same row, shift right
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            # letters are in the same column, shift down
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            # letters form a rectangle, swap columns
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext


def decrypt(ciphertext, key):
    """
    Decrypt ciphertext using the Playfair cipher and the given key.

    The ciphertext is divided into pairs of letters and each pair is decrypted
    using the 5x5 matrix generated from the key.

    Args:
        ciphertext (str): The ciphertext to decrypt.
        key (str): The key to use for the 5x5 matrix.

    Returns:
        str: The decrypted plaintext.

    """
    matrix = generate_matrix(key)
    plaintext = ''

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i:i+2]

        # find the positions of the letters in the matrix
        row1, col1 = find_letter(a, matrix)
        row2, col2 = find_letter(b, matrix)

        # decrypt the pair of letters
        if row1 == row2:
            # letters are in the same row, shift left
            plaintext += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            # letters are in the same column, shift up
            plaintext += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            # letters form a rectangle, swap columns
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    # remove any trailing 'X' added during encryption
    if plaintext[-1] == 'X':
        plaintext = plaintext[:-1]

    return plaintext