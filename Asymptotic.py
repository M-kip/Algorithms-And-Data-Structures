#!/usr/bin/env python
'''
A simple function that describres Asymptotic
analysis using lists
'''
def find_max(data):
    '''
        Returns the maximum or the biggest element in the list
    '''
    biggest  = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,8,9,10]
    max = find_max(data)
    print("The max value is {}".format(max))
