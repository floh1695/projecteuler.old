#!/usr/bin/python2
"""
Largest prime factor
====================
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from __future__ import print_function
from shared import factorize


def run():
    return 3, max(factorize(600851475143))

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)
