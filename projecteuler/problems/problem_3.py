#!/usr/bin/python2
"""
Largest prime factor
====================
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from __future__ import print_function
from ..shared.prime import factorize
from operator import itemgetter

def run():
    value = max(factorize(600851475143))
    print('3\t: {}'.format(value))

if __name__ == '__main__':
    run()
