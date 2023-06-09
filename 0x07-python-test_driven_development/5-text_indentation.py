#!/usr/bin/python3
"""Module which contains text_indentation
   function
"""


def text_indentation(text):
    """function that prints a text
    with special indentation for
    '.', ':' and '?'

    Args:
        text : the text
    Returns:
        void
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        print()
        return

    punctuation_chars = ['.', '?', ':']
    result = ""

    for char in text:
        result += char
        if char in punctuation_chars:
            result += "\n\n"

    print('\n'.join(x.strip() for x in text.split('\n')), end="")
