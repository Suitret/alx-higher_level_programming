#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "V"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "III"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXI"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CXXIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = 1423
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = None
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
