#!/usr/bin/env python3
'''
    implements an arrary based stack using adapter pattern
    the internal data type uses the inbuilt list class
'''
class Empty(Exception):
    ''' Implements a custom exception class '''
    pass

class ArrayStack:
    ''' implements an array based stack using inbuilt list datatype'''

    def __init__(self):
        ''' Create an empty stack.'''
        self._data = []

    def __len__(self):
        ''' returns the length of the stack '''
        return len(self._data)

    def is_empty(self):
        ''' Checks if the stack is empty '''
        return len(self._data) == 0

    def push(self,e):
        ''' Push data into the stack '''
        self._data.append(e)

    def top(self):
        ''' Return (but do not remove) the element at the top of the stack
            Raise Empty exception if the stack is empty
        '''
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        ''' Remove and return the top most element of the stack

            Raise Empty exception if the stack is empty
        '''
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()
