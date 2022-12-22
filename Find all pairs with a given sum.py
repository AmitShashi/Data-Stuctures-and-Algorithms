'''
Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

Note: All pairs should be printed in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then
(u1,v1) should be printed first else second.
'''
class Solution:
    def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        A.sort()
        B.sort()
        i,j=0,M-1
        li=[]
        while i<N and j>=0:
            if A[i]+B[j]>X:
                j-=1
            elif A[i]+B[j]<X:
                i+=1
            else:
                li.append([A[i],B[j]])
                i+=1
                j-=1
            
        return li
