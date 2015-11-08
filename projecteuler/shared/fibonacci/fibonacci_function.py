#!/usr/bin/python2

from __future__ import print_function
from dict_manager import DictManager

manager = DictManager()


def fibonacci(n):
    """Return the fibonacci number at place n in integer form """
    if n < 0:
        # TODO: I should add negative fibonacci values
        raise ValueError('This function does not define negative'
                         'fibonacci numbers.')
    try:
        return manager.get(n)
    except KeyError:
        pass  # Continue on to the rest of the function

    if n in (0, 1):
        value = n
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    manager.add(n, value)
    return value

if __name__ == '__main__':
    from time import time
    t = time()
    for i in range(10000):
        print('{}\t: {}'.format(i, fibonacci(i)))
    print(time() - t)
