#!/usr/bin/python2

from __future__ import print_function
from time import time

from problems import problems
from timeit import timeit

if __name__ == '__main__':
    ft = time()
    for problem in problems:
        timeit(problem)
    print('\nTotal time: {}'.format(time() - ft))
