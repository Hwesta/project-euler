#!/usr/bin/python
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

def pythagorean_triple_sums_to(total=1000):
    iterate_to = total
    for a in range(1, iterate_to):
        for b in range(a + 1, iterate_to):
            # print('a', a, 'b', b)
            c = math.sqrt(a * a + b * b)
            # print(c)
            # Check if Pythagorean square
            if int(c) != c:
                break
            c = int(c)
            print('Found triple:', a, b, c, 'sum', a + b + c)
            if a + b + c == total:
                return int(a), int(b), int(c)
            # if a + b + c > total:
            #     break

def test_generate_triple():
    assert pythagorean_triple_sums_to(12) == (3, 4, 5)

if __name__ == '__main__':
    print('Pythagorean triple that sums to 1000 is', pythagorean_triple_sums_to(1000))
