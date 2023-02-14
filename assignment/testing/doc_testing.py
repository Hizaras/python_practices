import doctest


def add(x, y):
    """ adds two numbers
    >>> add(5, 5)
    11
    >>> add(2, -6)
    9
    >>> add(1, 4)
    5
    """
    return x + y


if __name__ == "__main__":
    doctest.testmod()
