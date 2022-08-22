#!/usr/bin/python
""" This module contains the factorial function """


def factorial(n):
    """
       Computes the factorial of n

    Parameters
    ----------
    n: int
      integer

    Return:
        integer
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(f"Factorial of 10 is {factorial(10)}")
    print(f"Factorial of 15 is {factorial(15)}")
    print(f"Factorial of 5 is {factorial(5)}")
