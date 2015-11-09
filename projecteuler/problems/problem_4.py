#!/usr/bin/python2
"""
Largest palindrome product
==========================
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from __future__ import print_function
from itertools import product
from shared import is_palindrome


def run():
    factors = list(range(100, 1000))
    palindromes = []
    for factor_a, factor_b in product(factors, factors):
        result = factor_a * factor_b
        if is_palindrome(result):
            palindromes.append(result)
    return 4, max(palindromes)

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)
