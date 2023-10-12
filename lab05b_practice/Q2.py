"""
Chun-Wei, Mo
A01375071
"""


def base_convert(base_10_number, destination_base):
    """
    Convert a base 10 number to destination base.

    :param base_10_number: a decimal integer
    :param destination_base: a positive integer
    :precondition: base_10_number must be a decimal and positive integer
    :precondition: destination_base must be inclusive and within range of 2 to 10
    :postcondition: convert base_10_number to a number with destination_base
    :return: a number with destination_base

    >>> base_convert(13, 2)
    1101
    >>> base_convert(1988, 5)
    30423
    """

    converted_number = ""
    while base_10_number != 0:
        digit_to_concatenate = base_10_number % destination_base
        converted_number = str(digit_to_concatenate) + converted_number
        base_10_number //= destination_base

    return int(converted_number)


def main():
    print("9487 convert to base 7: ", base_convert(9487, 7))
    print("54088 convert to base 3: ", base_convert(54088, 3))
    print("617 convert to base 9: ", base_convert(617, 9))


if __name__ == "__main__":
    main()
