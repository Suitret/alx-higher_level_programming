#!/usr/bin/python3

def multiple_returns(sentence):
    len_str = len(sentence)
    if len_str > 0:
        return len_str, sentence[0]
    else:
        return len_str, None
