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

# ~5 sec
def first_try(maximum):
    # Make graph of collatz chains
    collatz_graph = {} # number: next in chain
    for current in xrange(2, maximum):
        next = collatz(current)
        # Generate chain
        while current > 1:
            if current not in collatz_graph:
                collatz_graph[current] = next
            else: # We've already calculated the rest of the chain
                break
            current, next = next, collatz(next)

    def get_length(start):
        length = 1
        while collatz_graph[start] > 1:
            # Memoize!
            if start not in collatz_length:
                length += 1
                start = collatz_graph[start]
            else: # We already know the length of the rest
                return length + collatz_length[start]
        return length

    # Find all the lengths
    collatz_length = {1: 1} # start number: length
    for start in xrange(2, maximum):
        if start not in collatz_length:
            collatz_length[start] = get_length(start)

    longest = max(collatz_length, key=collatz_length.get)
    print "Chain starting at %d is length %d." % (longest, collatz_length[longest])


if __name__ == '__main__':
    first_try(1000000)
