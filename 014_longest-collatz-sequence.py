#!/usr/bin/python

# Project Euler Problem 7
# Which starting number, under one million, produces the longest Collatz chain?
# Holly Becker

# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

#import networkx as nx
# Add numbers in a sequence to a graph, pointing to it's next neighbour

def collatz(n):
    if n % 2 == 0: # even
        return n/2
    else:
        return 3*n+1

def first_try(maximum):
    G = {}
    for current in xrange(2, maximum):
        next = collatz(current)
        while current > 1:
            # print current, "->",
            if current not in G:
                G[current] = next
                #print G.keys()
            else:
                # print next, "chain",
                break
            current, next = next, collatz(next)
        # print

    # There's a more pythonic way to do this
    longest_start, max_length = 1, 0
    for start in xrange(2, maximum):
        iterator = start
        length = 1
        while G[iterator] > 1:
            iterator = G[iterator]
            length += 1
        if length > max_length:
            longest_start, max_length = start, length
    print "Chain starting at %d is length %d." % (longest_start, max_length)


if __name__ == '__main__':
    first_try(1000000)
