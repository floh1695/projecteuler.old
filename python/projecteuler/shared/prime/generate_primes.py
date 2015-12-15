#!/usr/bin/python2

from __future__ import print_function
import is_prime as ip


def generate_primes(start=2, end=0):
    while True:
        if end and start > end:
            break
        if ip.is_prime(start):
            yield start
        start += 1

if __name__ == '__main__':
    for prime in generate_primes(end=1000):
        print(prime)
