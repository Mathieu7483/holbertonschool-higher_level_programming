#!/usr/bin/python3
""" Module that define a Myint class"""


class MyInt(int):
    """
    Une classe qui hérite de 'int' et inverse les opérateurs
    d'égalité (==) et d'inégalité (!=).
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
