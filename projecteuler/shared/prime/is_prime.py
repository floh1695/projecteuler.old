#!/usr/bin/python2

from __future__ import print_function

import generate_primes as gp
from dict_manager import DictManager
from os.path import dirname, join
from math import sqrt

manager = DictManager()


def is_prime(n):
    """Calculate if n is prime or not"""
    if n < 2:
        return False
    if n < 4:
        return True

    try:
        return manager.get(n)
    except KeyError:
        pass  # Continue on to the rest of the function

    value = True
    for i in gp.generate_primes(end=int(sqrt(n))):
        if n % i == 0:
            value = False
            break
    manager.add(n, value)
    return value

if __name__ == '__main__':
    for range_value in range(100000):
        print('{}\t: {}'.format(range_value, is_prime(range_value)))
