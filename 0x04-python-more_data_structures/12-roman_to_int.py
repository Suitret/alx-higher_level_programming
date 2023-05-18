#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or not isinstance(roman_string, str):
        return 0

    unit = ["IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]
    tens = ["XC", "LXXX", "LXX", "LX", "L", "XL", "XXX", "XX", "X"]
    cent = ["CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C"]
    thou = ["MMM", "MM", "M"]

    my_list = [unit, tens, cent, thou]
    year, pos = 0, 0

    for section in my_list:
        pos += 1
        for str_ in section:
            if str_ in roman_string and pos < 4:
                year += (9 - section.index(str_))*(10**(pos-1))
                break
            elif str_ in roman_string and pos == 4:
                year += (3 - section.index(str_))*(10**(pos-1))
                break
    return year
