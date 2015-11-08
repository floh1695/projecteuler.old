#!/usr/bin/python2
"""

"""

from __future__ import print_function


def run():
    print('0\t: {}'.format(None))

if __name__ == '__main__':
    from timeit import timeit
    timeit(run)
