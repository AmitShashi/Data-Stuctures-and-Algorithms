'''
You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

Example 1:

Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2

Output: 1
Explanation: x = 1 and y = 2. There are
two distances between x and y, which are
1 and 3 out of which the least is 1.
'''
    def minDist(self, arr, n, x, y):
        
        idx1=-1
        idx2=-1
        min_dist = 9999999
        
        for i in range(n):
            
           if(arr[i]==x):
              idx1=i;
              
           if(arr[i]==y):
              idx2=i;

           if(idx1!=-1 and idx2!=-1):
               min_dist=min(min_dist,abs(idx1-idx2));

        
        if(idx1==-1 or idx2==-1):
            return -1;
        else:
            return min_dist;
