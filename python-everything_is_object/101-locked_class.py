#!/usr/bin/python3
def locked_class():
    __slots__ = ['first_name']
    return type('LockedClass', (), {'__slots__': __slots__})
