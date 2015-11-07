#!/usr/bin/python2

from __future__ import print_function
from projecteuler import problems
from time import time


def timeit(f):
    t = time()
    f()
    print('\t {}\n'.format(time() - t))


if __name__ == '__main__':
    timeit(problems.problem_1)
    timeit(problems.problem_2)
    timeit(problems.problem_3)
    timeit(problems.problem_4)
    timeit(problems.problem_5)
    timeit(problems.problem_6)
    timeit(problems.problem_7)
