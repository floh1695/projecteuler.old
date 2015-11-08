#!/usr/bin/python2
"""
Summation of primes
===================
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from __future__ import print_function
from shared import generate_primes

def run():
    print('10\t: {}'.format(sum(generate_primes(end=2000000))))

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)
