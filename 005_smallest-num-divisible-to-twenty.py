# Project Euler Problem 5
# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
# Holly Becker  
# Started 2008-12-20

import operator

# Started 2008-12-20
def main(max):
	#smallest divided by ever number 1 to max evenly
	# start at 2
	# while test number not divisible by all
	#	increment test number
	#	test if divisible
	
	test=2520
	trigger=False
	while not trigger:
		trigger=True
		test+=max
		print test
		for i in range(11,max):
			if (test%i) !=0:
				trigger=False
				break
	
	print "ans ",test

def first_try():
	n=1
	for i in range(11,20):
		n*=i
	print n

# 2013-05-05

# Works but too slow
def second_try():
    factors = range(2, 21)
    #factors = [2, 3, 5, 7, 11, 13, 17, 19]
    print factors
    maximum = reduce(operator.mul, factors) # largest 'minimum'
    print maximum
    maximum = int(1e9)
    print maximum
    for number in xrange(2, maximum, 2):
        if all( number % factor == 0 for factor in factors ):
            print number
            break

# Prime factors under 20: 2 3 5 7 11 13 17 19

# LCM stuff http://www.math.com/school/subject1/lessons/S1U3L3DP.html

# 2 = 2
# 3 = 3
# 4 = 2 x 2
# 5 = 5
# 6 = 2 x 3
# 7 = 7
# 8 = 2 x 2 x 2
# 9 = 3 x 3
# 10 = 2 x 5
# 11 = 11
# 12 = 2 x 2 x 3
# 13 = 13
# 14 = 2 x 7
# 15 = 3 x 5
# 16 = 2 x 2 x 2 x 2
# 17 = 17
# 18 = 2 x 3 x 3
# 19 = 19
# 20 = 2 x 2 x 5

# 2 = 4x
# 3 = 2x
# 5 = 1x
# 7 = 1x
# 11 = 1x
# 13 = 1x
# 17 = 1x
# 19 = 1x

LCM = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
print LCM

