# Project Euler Problem 2
# Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.
# Holly Becker  
# Done 2008-12-20

def main():
	a = 1
	b = 1
	c = a+b
	sum = 0
	while c<4000000:
		if c%2==0:
			sum+=c
		a=b
		b=c
		c=a+b
	print sum
		
		


main()
