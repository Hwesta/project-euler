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
        # Check if number is prime

        # ~7 sec, because primes gets up to 1000 primes, that's a lot to check
        # if all( number % prime != 0 for prime in primes):

        # ~3 sec, fewer primes to check, but multiplication is still expensive
        # and it has to iterate over all 1000 primes to check that they're not 
        # too big
        # if all( number % prime != 0 for prime in primes if prime * prime <= number):


        # ~.8 sec, fewer primes to check, and doesn't iterate over the entire list
        # to check what's prime, just until we hit something too big, since we 
        # know the list is sorted
        # But not pythonic
        # test_primes = []
        # for prime in primes:
        #     if prime * prime <= number:
        #         test_primes.append(prime)
        #     else:
        #         break
        # if all( number % prime != 0 for prime in test_primes):

        # ~.4 sec, xrange is fast to generate, so even though doing more numbers,
        # still doing less work overall
        if all( number % prime != 0 for prime in range(3, square_root, 2)):
            primes.append(number)

    print(number)


first_try(10001)
