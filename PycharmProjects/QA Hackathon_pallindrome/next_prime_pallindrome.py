import math
import sys
def isPrime(n):
    '''Returns 'True' if 'n' is a prime. False otherwise'''
    if n ==1:
        return False  #1 is not a prime number
    #if input is even and not 2, then it cannot be prime
    if n==2:
        return True
    if n > 2  and n % 2 ==0:
        return False
    max_divisor =math.floor(math.sqrt(n))

    for d in range (3, max_divisor + 1, 2):    # the step value helps in skipping all the even numbers after the number 2 for better time complexity.
        if n % d == 0:
            return False
        return True
def Next_smallest_Palindrome(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1] and isPrime(num):
            return i
        break


