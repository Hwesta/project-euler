# Project Euler Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.
# Holly Becker  
# Done 2008-12-20

def is_palin(num):
    strnum = str(num)
    if strnum == strnum[::-1]: # list slicing list[start:stop:step]
        return True
    else:
        return False
        

    
def main():
    saved = 0
    for i in range(999,99,-1):
        for j in range(990,99,-11): # Using note below
            num = i*j
            #print num
            if num > saved and is_palin(num):
                saved=num
                break
    print "answer ", saved

if __name__ == "__main__":
    main()

#The palindrome can be written as: 
    
#abccba 

#Which then simpifies to: 

#100000a + 10000b + 1000c + 100c + 10b + a 

#And then: 

#100001a + 10010b + 1100c 

#Factoring out 11, you get: 

#11(9091a + 910b + 100c) 

#So the palindrome must be divisible by 11. Seeing as 11 is prime, at least one of the numbers must be divisible by 11.

