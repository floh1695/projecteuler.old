#!/usr/bin/python2
"""
Smallest Multiple
=================
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

from __future__ import print_function
from shared import least_common_multiple as lcm

def run():
    print('5\t: {}'.format(reduce(lcm, range(1, 21))))

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)
