import random


def generate_numbers(high):
    """
    >>> len(generate_numbers(0))
    5
    >>> all(n in [25, 50, 75, 100] for n in generate_numbers(4)[:3])
    True
    """
    assert high <= 4

    high_numbers = [25, 50, 75, 100]
    random.shuffle(high_numbers)

    output_numbers = high_numbers[:high]

    low_numbers = list(range(1, 11)) * 5
    output_numbers += low_numbers[:5 - high]

    return output_numbers


def generate_target():
    """
    >>> generate_target() < 1000
    True
    >>> generate_target() >= 100
    True
    """
    return random.randint(100, 999)
