#!/usr/bin/python2

from __future__ import print_function

from ..dict_manager import DictManager
from os.path import dirname, join
from math import sqrt

manager = DictManager(join(dirname(__file__), 'is_prime.csv'), int,
                      lambda s: True if s == 'True' else False)


def is_prime(n):
    """Calculate if n is prime or not"""
    if n < 2:
        return False

    try:
        return manager.get(n)
    except KeyError:
        pass  # Continue on to the rest of the function

    value = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            value = False
            break
    manager.add(n, value)
    return value

if __name__ == '__main__':
    for range_value in range(10000):
        print('{}\t: {}'.format(range_value, is_prime(range_value)))
