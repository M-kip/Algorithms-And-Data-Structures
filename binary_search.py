#!/usr/bin/python3
""" 
   This module contains binary search function
   for searching sorted sequences
"""


def binary_search(data, target, low, high):
    """
       Function search for target using recursion

    Parameters
    ----------
    data : sequence data type
        sequence data type for example list, linked lists
    target: sequence item
        Data type corresponeds to the sequence item type

    Returns:
       True/False if the target exists or not

    """

    mid = (low + high) // 2 # median of the list
    if low > high:
        return False
    else:
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        elif target > data[mid]:
            return binary_search(data, target, mid + 1, high)
