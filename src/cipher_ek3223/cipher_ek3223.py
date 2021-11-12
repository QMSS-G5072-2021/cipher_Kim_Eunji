def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    """
    Ciphers text by shifting each letter 'shift' places to the right.

    Args:
        text: A string to be altered into a ciphered version.
        shift : The number of places a letter should be moved.
        encrypt : If True will be ciphered to the right. Otherwise,
                  the string will be ciphered to the left.

    Returns:
        new_text : The ciphered string that has letters shifted 'shift'
                   places in the designated direction. For example:

        cipher('apple', 1, encyrypt=True) = 'bqqmf'
        cipher('bqqmf', 1, encrype=False) = 'apple'
    """
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
