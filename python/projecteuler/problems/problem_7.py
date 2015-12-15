#!/usr/bin/python2
"""
10001st prime
=============
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""

from __future__ import print_function
from shared import generate_primes

def run():
    gen = generate_primes()
    for _ in xrange(10000):
        next(gen)
    return 7, next(gen)

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)
