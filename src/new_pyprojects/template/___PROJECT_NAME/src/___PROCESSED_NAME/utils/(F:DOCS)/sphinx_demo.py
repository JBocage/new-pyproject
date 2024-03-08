"""
Demo for sphinx documentation
"""


def foo():
    """
    A function that does nothing
    """
    pass


class Baz:
    """
    A class that does nothing
    """

    def __init__(self, value: int) -> None:
        """
        Initializes the class

        :param value: The value to be stored
        :type value: int
        """
        self.value = value

    def get_value(self) -> int:
        """
        Returns the value

        :return: The value
        :rtype: int
        """
        return self.value


def bar(first_integer: int, second_integer: int) -> Baz:
    """
    A function that adds two integers

    :param first_integer: The first integer

        Can be anythings
    :type first_integer: int

    :param second_integer: The second integer
    :type second_integer: int

    :return: The sum of the two integers, in a Baz object
    :rtype: Baz
    """
    return Baz(first_integer + second_integer)


class DummyException(Exception):
    """
    A dummy exception
    """

    pass


def oux_raises_exception():
    """
    A function that raises an exception

    :raises DummyException: This is a dummy exception
    """
    raise DummyException("This is a dummy exception")
