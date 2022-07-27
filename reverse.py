#!/usr/bin/env python3
import sys
from ArrayStack import ArrayStack

'''
   The module implements a function that reverses the data sequence of a data structure 
   or a file 
'''

def reverse_file(filename):
    ''' The function reverses the contents of a file '''
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()
