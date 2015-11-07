#!/usr/bin/python2

from __future__ import print_function
from projecteuler.problems import problems
from time import time


def timeit(f):
    t = time()
    f()
    print('\t  {}'.format(time() - t))


if __name__ == '__main__':
    ft = time()
    for problem in problems:
        timeit(problem)
    print('\nTotal time: {}'.format(time() - ft))
