# Project Euler Problem 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Holly Becker  
# Done 2008-12-25

def main(max):
	squaresum=(max*(max+1)/2)**2
	
	sumsquare=0	
	for i in range(max+1):
		sumsquare+=i**2
	
	difference = squaresum-sumsquare
	print(difference)
	
main(100)
