#!/usr/bin/python2

from __future__ import print_function


def fibonacci(n):
    """Return the fibonacci number at place n in integer form """
    if n < 0:
        # TODO: I should add negative fibonacci values
        raise ValueError('This function does not define negative'
                         'fibonacci numbers.')

    # TODO: I need to check and store tabled values

    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    for i in range(100):
        print('{}\t: {}'.format(i, fibonacci(i)))
