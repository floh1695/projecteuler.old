#!/usr/bin/python2

from __future__ import print_function
from generate_primes import generate_primes


def factorize(number):
    arr = []
    gen = generate_primes()
    prime = next(gen)
    while number >= prime:
        if number % prime == 0:
            arr.append(prime)
            number /= prime
            continue
        else:
            prime = next(gen)
    return arr

if __name__ == '__main__':
    for i in range(100000):
        print('{}\t: {}'.format(i, factorize(i)))
