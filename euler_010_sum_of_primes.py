#!/usr/bin/python

# Project Euler Problem 10
# Find the sum of all the primes below two million.
# Holly Becker

import math


def generate_prime():
    yield 2
    yield 3
    number = 3
    while True:
        number += 2
        square_root = int(math.ceil(math.sqrt(number))) + 1
        # if number is prime
        # if all( number % prime != 0 for prime in primes): # ~7 sec
        # if all( number % prime != 0 for prime in primes if prime * prime <= number): # ~3 sec
        if all( number % prime != 0 for prime in range(3, square_root, 2)): # ~.4 sec
            yield number

def first_try(n): # ~20 sec
    total = 0
    for next_prime in generate_prime():
        if next_prime < n:
            total += next_prime
        else:
            print(total)
            return

# Holy cow this is faster than I expected!
def sieve(maximum):
    sieve = [True]*maximum
    primes = [2]
    for num in range(3, int(math.sqrt(maximum)), 2):
        if sieve[num]: # num is prime
            primes.append(num)
            for not_prime in range(num, maximum, num):
                sieve[not_prime] = False
    return primes

def second_try(maximum): # < 1 sec
    print((sum(sieve(int(maximum)))))

if __name__ == '__main__':
    # first_try(2e6)
    second_try(2e6)
