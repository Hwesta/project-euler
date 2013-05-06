#!/usr/bin/python

# Project Euler Problem 7
# What is the 10 001st prime number?
# Holly Becker

import math

# 2013-05-06
def first_try(nth_prime):
    primes = [2, 3]
    number = 3
    while len(primes) < nth_prime:
        number += 2
        square_root = int(math.ceil(math.sqrt(number))) + 1
        # if number is prime
        # if all( number % prime != 0 for prime in primes): # ~7 sec
        # if all( number % prime != 0 for prime in primes if prime * prime <= number): # ~3 sec
        if all( number % prime != 0 for prime in range(3, square_root, 2)): # ~.4 sec
            primes.append(number)

    print number


first_try(10001)
