# Project Euler Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.
# Holly Becker  
# Done 2008-12-20

def is_palin(num):
	strnum = str(num)
	if strnum == strnum[::-1]:
		return True
	else:
		return False
		

	
def main():
	saved = 0
	for i in range(1000,100,-1):
		for j in range(1000,100,-1):
			num = i*j
			#print num
			if is_palin(num) and num>saved:
				saved=num
				break
	print "answer ",saved

main()
