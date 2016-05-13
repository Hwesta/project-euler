# Project Euler Problem 3
# What is the largest prime factor of the number 600851475143 ?
# Holly Becker  
# Done 2008-12-20

def main(num):
	divisor = 2
	largest=0
	while largest < num/2+1:
		if num%divisor==0:
			num/=divisor
			largest=divisor
		else:
			divisor+=1
	print(largest)

if __name__ == '__main__':
	main(600851475143)
