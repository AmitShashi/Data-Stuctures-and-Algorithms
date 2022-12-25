'''
Given an array arr[] of n integers, construct a Product Array prod[] (of same size) 
such that prod[i] is equal to the product of all the elements of arr[] except arr[i]. 
Solve it without division operator in O(n) time.

Example : 

Input: arr[]  = {10, 3, 5, 6, 2}
Output: prod[]  = {180, 600, 360, 300, 900}
3 * 5 * 6 * 2 product of other array 
elements except 10 is 180
10 * 5 * 6 * 2 product of other array 
elements except 3 is 600
10 * 3 * 6 * 2 product of other array 
elements except 5 is 360
10 * 3 * 5 * 2 product of other array 
elements except 6 is 300
10 * 3 * 6 * 5 product of other array 
elements except 2 is 900
'''

    def productExceptSelf(self, nums, n):
        # Base case
        if n == 1:
            #print(0)
            return [1]
    
        i, temp = 1, 1
    
        # Allocate memory for the product array
        prod = [1 for i in range(n)]
    
        # Initialize the product array as 1
    
        # In this loop, temp variable contains product of
        # elements on left side excluding arr[i]
        for i in range(n):
            prod[i] = temp
            temp *= arr[i]
    
            # Initialize temp to 1 for product on right side
        temp = 1
    
        # In this loop, temp variable contains product of
        # elements on right side excluding arr[i]
        for i in range(n - 1, -1, -1):
            prod[i] *= temp
            temp *= arr[i]
            
        return prod
