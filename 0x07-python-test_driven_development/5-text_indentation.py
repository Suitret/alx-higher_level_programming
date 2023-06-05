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

    if not isinstance(text, str)
        raise TypeError("text must be a string")

    for char in text:
        if char == '.' or char == ':' or char == '?':
            print(char, end="")
            print("\n")
        else:
            print(char, end="")
