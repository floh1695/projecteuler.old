#!/usr/bin/python2

from __future__ import print_function
from time import time

from problems import problems
from timeit import timeit

if __name__ == '__main__':
    ft = time()
    file_string = ''
    for problem in problems:
        file_string += timeit(problem)
        file_string += '\n'
    total_time = '\nTotal time: {}'.format(time() - ft)
    print(total_time)
    with open('benchmark.txt', 'w') as f:
        f.write(file_string)
        f.write(total_time)
