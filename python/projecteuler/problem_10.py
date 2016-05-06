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
    value = 0
    for prime in generate_primes(end=2000000):
        value += prime
    return 10, value

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)
