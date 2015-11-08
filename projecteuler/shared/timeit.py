#!/usr/bin/python2
from time import time


def timeit(f):
    t = time()
    f()
    print('\t  {}'.format(time() - t))
