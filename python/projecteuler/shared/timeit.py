#!/usr/bin/python2

from __future__ import print_function
from time import time


def timeit(f):
    t = time()
    problem_num, result = f()
    time_string = '{}\t: {}\n\t  {}'.format(problem_num,
                                            result,
                                            time() - t)
    print(time_string)
    return time_string
