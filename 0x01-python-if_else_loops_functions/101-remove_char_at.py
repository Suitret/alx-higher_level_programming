#!/usr/bin/python3
def remove_char_at(string, n):
    result = ""
    i = 0
    for c in string:
        if i != n:
            result += c
        i += 1
    return result
