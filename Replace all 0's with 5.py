'''
You are given an integer N. You need to convert all zeroes of N to 5.

Example 1:

Input:
N = 1004
Output: 1554
Explanation: There are two zeroes in 1004
on replacing all zeroes with "5", the new
number will be "1554".
Example 2:

Input:
N = 121
Output: 121
Explanation: Since there are no zeroes in
"121", the number remains as "121".
'''
import math
def convertFive(n):
    # Code here
    temp=0
    while(n>0):
        
        rem=n%10
        if rem==0:
            rem=5
            
        n=n//10
        
        temp=temp*10+rem
        num=temp
    
    temp=0
    while(num>0):
        
        rem=num%10
        num=num//10
        temp=temp*10+rem
    
    return temp
