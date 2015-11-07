#!/usr/bin/python2
"""
Largest prime factor
====================
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from __future__ import print_function
from ..shared import factorize


def run():
    print('3\t: {}'.format(max(factorize(600851475143))))
