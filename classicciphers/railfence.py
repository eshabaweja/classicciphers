def encrypt(message: str, rails: int) -> str:
    """
    Encrypts a message using the Rail Fence Cipher with the specified number of rails.

    Args:
        message (str): The message to encrypt.
        rails (int): The number of rails to use.

    Returns:
        str: The encrypted message.

    Raises:
        ValueError: If the number of rails is less than 2.
    """
    if rails < 2:
        raise ValueError("Number of rails must be at least 2.")

    fence = [''] * rails
    rail = 0
    direction = 1

    for char in message:
        fence[rail] += char
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return ''.join(fence)


def decrypt(ciphertext: str, rails: int) -> str:
    """
    Decrypts a message that has been encrypted using the Rail Fence Cipher with the specified number of rails.

    Args:
        ciphertext (str): The encrypted message.
        rails (int): The number of rails that were used to encrypt the message.

    Returns:
        str: The decrypted message.

    Raises:
        ValueError: If the number of rails is less than 2.
    """
    if rails < 2:
        raise ValueError("Number of rails must be at least 2.")

    fence = [''] * rails
    rail = 0
    direction = 1

    for i in range(len(ciphertext)):
        fence[rail] += ' '
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for i in range(rails):
        length = len(fence[i])
        fence[i] = ciphertext[index:index+length]
        index += length

    message = ''
    rail = 0
    direction = 1

    for i in range(len(ciphertext)):
        message += fence[rail][0]
        fence[rail] = fence[rail][1:]
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return message
