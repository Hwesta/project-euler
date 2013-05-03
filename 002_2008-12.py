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

# 2013-05-01
def even_fibonacci():
    (a, b) = (0,1)
    c = a + b
    while c < 4e6:
        if c % 2 == 0:
            yield a+b
        (a, b) = (b, a + b)
        c = a + b


print sum(even_fibonacci())

# This may be a small improvement. The Fibonacci series is: 

#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610... 

#Now, replacing an odd number with O and an even with E, we get: 

#O, O, E, O, O, E, O, O, E, O, O, E, O, O, E... 

#And so each third number is even. We don't need to calculate the odd numbers. Starting from an two odd terms x, y, the series is: 

#x, y, x + y, x + 2y, 2x + 3y, 3x + 5y

def another_even_fibonacci():
    (a, b) = (1,1)
    while a+b < 4e6:
        yield a+b
        (a, b) = (a + 2*b, 2*a + 3*b)
        
print sum(another_even_fibonacci())