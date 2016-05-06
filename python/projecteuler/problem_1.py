#!/usr/bin/python2
"""
Multiples of 3 and 5
====================
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from __future__ import print_function

def run():
    value = 0
    for i in range(1000):
        if i % 3 is 0 or i % 5 is 0:
            value += i
    return 1, value

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)

