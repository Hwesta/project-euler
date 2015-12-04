# Project Euler Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.
# Holly Becker  
# Done 2008-12-20

def first_try():
	total = 0
	for i in range(1000):
		if i%3 == 0 or i%5 == 0:
			total += i
	print(total)

# 2013-05-01

def second_try(max_val):
  multiples = [x for x in range(1000) if x%3 == 0 or x%5 == 0]
  #multiples = filter(lambda x: x%3 == 0 or x%5 == 0, range(1000))
  total = sum(multiples)
  print(total)

# He is using a clever improvisation of the formulae for arithmetic progressions. For example, to find the sum of the terms 3,6,9,12,..., you would use (n/2)(a+l), where n is the number of terms, a is the first term, and l is the last term. But to find the last term requires a bit of work. The nth term is given by a+(n-1)d, where d is the common difference. So we need to solve 3+3(n-1)=1000, giving 3(n-1)=997, and n=997/3+1=333.333... However, n must be integer, so int(333.333...)=333, and checking, 3+3(333-1)=999; this is the last term before 1000.

# In general, a+(n-1)d=x, gives n=int((x-a)/d+1). 

# But for this problem we can improve even further, as a=d we get n=int(x/d-d/d+1)=int(x/d). 

# The nth (last) term, l=a+(n-1)d=d+(int(x/d)-1)*d=d*int(x/d). 

# Combining this to find the sum, S=(n/2)(a+l)=(int(x/d)/2)*(d+d*int(x/d)). 

# Simplifying, S=d*int(x/d)*(1+int(x/d))/2. 

# As the problem asks for the sum of multiples of 3 and 5 we find the sum of each series, but as 3,6,9,... and 5,10,15,... have multiples of 15 in common, we need to subtract the series for 15,30,45,... 

# However, caution is needed. The problem states below then 1000, so we must use 999 in the formula (otherwise it would include 1000 in the sum, as a multiple of 5): 
  
# T = 3*int(999/3)*(1+int(999/3))/2 + 5*int(999/5)*(1+int(999/5))/2 - 15*int(999/15)*(1+int(999/15))/2 

# Therefore, T = 3*333*(1+333)/2 + 5*199*(1+199)/2 - 15*66*(1+66)/2 = 233168.

# a = start of series(ish), and step
# n = number of elements in series
# l = last element in series before x
# x = max_val
def sum_of_series(step, x):
    x = x-1
    a = step
    d = step
    n = int(x/a)
    l = a*n
    #print a, n, l
    #print a+l, n, n/2
    #print (a+l)*n/2, 0.5*d*int(x/d)*(1+int(x/d)), 0.5*d*x/d*(1+x/d)
    return 0.5*d*int(x/d)*(1+int(x/d))
    
def third_try(max_val):
    print(sum_of_series(3, max_val) + sum_of_series(5, max_val) - sum_of_series(15, max_val))
    
first_try()
second_try(1000)
third_try(1000)