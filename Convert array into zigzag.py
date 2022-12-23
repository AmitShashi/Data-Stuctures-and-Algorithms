'''
Given an array arr of distinct elements of size N, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 

NOTE: If your transformation is correct, the output will be 1 else the output will be 0. 

Example 1:

Input:
N = 7
Arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: 3 7 4 8 2 6 1
Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1
'''
def zigZag(self,a, n):
        # code here
        flag=True
        for i in range(n-1):
            
            if flag is True:
                if a[i]>a[i+1]:
                    a[i],a[i+1]=a[i+1],a[i]
                    
            if flag is False:
                if a[i]<a[i+1]:
                    a[i],a[i+1]=a[i+1],a[i]
            flag=not(flag)
                    
                
