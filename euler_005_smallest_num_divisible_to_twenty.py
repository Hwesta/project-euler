# Project Euler Problem 5
# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
# Holly Becker  
# Started 2008-12-20

import operator
from functools import reduce

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
		print(test)
		for i in range(11,max):
			if (test%i) !=0:
				trigger=False
				break
	
	print(("ans ",test))

def first_try():
	n=1
	for i in range(11,20):
		n*=i
	print(n)

# 2013-05-05

# Programmatic solution initially too slow, much better with some tweaks from 
# the solution thread
def second_try():
    factors = list(range(11, 21)) # 1-10 are factors of numbers in 11-20
    maximum = reduce(operator.mul, factors) # largest 'minimum'
    for number in range(20, maximum, 20):
        if all( number % factor == 0 for factor in factors ):
            print(number)
            break

# Prime factors under 20: 2 3 5 7 11 13 17 19

# LCM stuff http://www.math.com/school/subject1/lessons/S1U3L3DP.html

# Factors
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

# Max number of times each number shows up
# 2 = 4x
# 3 = 2x
# 5 = 1x
# 7 = 1x
# 11 = 1x
# 13 = 1x
# 17 = 1x
# 19 = 1x
def lcm():
    LCM = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
    print(LCM)

if __name__ == '__main__':
    second_try()
