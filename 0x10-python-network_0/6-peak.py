#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if not list_of_integers:
        return None

    length = len(list_of_integers)

    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)

    mid = length // 2
    mid_value = list_of_integers[mid]

    if (mid_value >= list_of_integers[mid - 1] and
            mid_value >= list_of_integers[mid + 1]):
        return mid_value
    if mid_value < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid_value < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
