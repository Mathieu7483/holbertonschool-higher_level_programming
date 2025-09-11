#!/usr/bin/python3
'''
Module that define a print of text
'''


def text_indentation(text):
    '''
    function that define a print of a text
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    x = ""
    for i in text:
        x += i
        if i in ".?:":
            print(x.strip())
            print()
            x = ""
    if x.strip():
        print(x.strip(), end=" ")
