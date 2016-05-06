#!/usr/bin/python2
"""
Sum square difference
=====================
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

from __future__ import print_function


def run(last=100):
    sum_of_squares = 0
    for i in range(1, last + 1):
        sum_of_squares += i**2
    square_of_sums = sum(list(range(1, last + 1)))**2
    return 6, square_of_sums - sum_of_squares

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)
