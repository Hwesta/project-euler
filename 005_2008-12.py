# Project Euler Problem 5
# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
# Holly Becker  
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

def test():
	n=1
	for i in range(11,20):
		n*=i
	print n

test()



