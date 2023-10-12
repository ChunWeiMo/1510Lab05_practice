"""
Chun-Wei, Mo
A01375071
"""


def shift_uppercase_letter(uppercase_letter, shift):
    """
    Return an uppercase letter after a Unicode shift.

    :param uppercase_letter: a string
    :param shift: an integer
    :precondition: uppercase_letter must be a single character and an uppercase letter
    :precondition: shift can be a positive or negative integer
    :postcondition: find the uppercase letter after the Unicode shift
    :return: a shifted uppercase letter

    >>> shift_uppercase_letter('Z', 3)
    'C'
    >>> shift_uppercase_letter('D', -2)
    'B'
    """
    uppercase_letter = ord(uppercase_letter)
    uppercase_letter += shift
    if uppercase_letter > 90:
        uppercase_letter -= 26
    elif uppercase_letter < 65:
        uppercase_letter += 26
    return chr(uppercase_letter)


def shift_lowercase_letter(lowercase_letter, shift):
    """
    Return a lowercase letter after a Unicode shift.

    :param lowercase_letter: a string
    :param shift: an integer
    :precondition: lowercase_letter must be a single character and a lowercase letter
    :precondition: shift can be a positive or negative integer
    :postcondition: find the lowercase letter after the Unicode shift
    :return: a shifted lowercase letter

    >>> shift_lowercase_letter('c', 3)
    'f'
    >>> shift_lowercase_letter('a', -2)
    'y'
    """
    lowercase_letter = ord(lowercase_letter)
    lowercase_letter += shift
    if lowercase_letter > 122:
        lowercase_letter -= 26
    elif lowercase_letter < 97:
        lowercase_letter += 26
    return chr(lowercase_letter)


def caesarcipher(message, encode, shift):
    """
    Encode or decode a message.

    A function encodes or decodes a message through a Unicode shift.

    :param message: a string
    :param encode: a boolean
    :param shift: an integer
    :precondition: message may be empty
    :precondition: encode must be True or False
    :precondition: shift can be a positive or negative integer
    :postcondition: encode message through the Unicode shift if encode is True
    :postcondition: decode message through the Unicode shift if encode is False
    :return: encoded or decoded message

    >>> caesarcipher('Chris', True, 2)
    'Ejtku'
    >>> caesarcipher('cat', True, 7)
    'jha'
    >>> caesarcipher('cat', True, -2)
    'ayr'
    """

    message_after_cipher = ''

    # decode
    if not encode:
        shift *= -1

    for character in message:
        # Unicode A ~ Z : 65 ~ 90
        # Unicode a ~ z : 97 ~ 122
        if 65 <= ord(character) <= 90:
            encoded_character = shift_uppercase_letter(character, shift)
        elif 97 <= ord(character) <= 122:
            encoded_character = shift_lowercase_letter(character, shift)
        else:
            encoded_character = character

        message_after_cipher += encoded_character

    return message_after_cipher


def main():
    print('G after 3 Unicode shift is', shift_uppercase_letter('G', 3))
    print('J after -2 Unicode shift is', shift_uppercase_letter('J', -2))
    print('a after 4 Unicode shift is', shift_lowercase_letter('a', 4))
    print('k after -1 Unicode shift is', shift_lowercase_letter('k', -1))
    print('Encode cat with shift 2 is', caesarcipher('cat', True, 7))
    print('Encode dOg with shift -5 is', caesarcipher('dOg', True, -5))
    print('Decode F-Z, Pr with shift 3 is', caesarcipher('F-Z, Pr', False, 3))


if __name__ == '__main__':
    main()
