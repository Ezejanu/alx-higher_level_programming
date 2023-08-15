#!/usr/bin/python3
"""This is a class MyInt, that inherits from int"""


class MyInt(int):
    """This class inherits from int, but has inverted the != and == operands"""


    def __ne__(self, other):
        return (super().__eq__(other))

    def __eq__(self, other):
        return (super().__ne__(other))
