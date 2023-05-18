#!/usr/bin/python3

def roman_to_int(roman_string):

    unit = ["IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]
    tens = ["XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X"]
    cent = ["CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C"]
    thou = ["MMM", "MM", "M"]

    my_list = [unit, tens, cent, thou]

    cp_roman = list(roman_string)
