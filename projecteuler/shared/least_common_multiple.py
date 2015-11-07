#!/usr/bin/python2

from fractions import gcd


def least_common_multiple(a, b):
    return a * b // gcd(a, b)
