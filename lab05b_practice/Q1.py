"""
Chun-Wei, Mo
A01375071
"""


def prime(number):
    """
    Verify whether this positive integer is a prime number.

    :param number: a positive integer
    :precondition: number must be a positive integer greater than 1
    :postcondition: verify whether this positive integer is a prime number
    :return: a boolean True if number is prime, or a boolean False if number is not prime

    >>> prime(7)
    True
    >>> prime(21)
    False
    """

    divisor = 2
    is_prime = True
    if number == 1:
        is_prime = False
    elif number == 2:
        is_prime = True
    else:
        while divisor < number:
            if number % divisor == 0:
                is_prime = False
                break
            else:
                is_prime = True
            divisor += 1

    return is_prime


def main():
    print("2 is prime:", prime(2))
    print("53 is prime:", prime(53))
    print("81 is prime:", prime(81))


if __name__ == "__main__":
    main()
