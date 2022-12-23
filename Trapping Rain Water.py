'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''
class Solution:
    def trap(self, arr: List[int]) -> int:
        l = [arr[0]]
        r = arr.copy()
        mini = []
        SUM=0
        n=len(arr)
        temp1=arr[0]
        temp2=arr[n-1]
        
        for i in range(1,n):
            if arr[i]<temp1:
                l.append(temp1)
            else:
                temp1=arr[i]
                l.append(arr[i])
        
        for i in range(n-2,-1,-1):
            if arr[i]<temp2:
                r[i]=temp2
            else:
                temp2=arr[i]
                r[i]=arr[i]
         
        for i in range (1,n-1):
            mini.append(min(l[i],r[i]) -arr[i])
        
        for i in range (len(mini)):
            SUM+=mini[i]
       
        return SUM
        
