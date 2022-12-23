'''
Given an array arr of N integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2, otherwise false.

Example 1:

Input:
N = 5
Arr[] = {3, 2, 4, 6, 5}

Output: Yes
Explanation: a=3, b=4, and c=5 forms a pythagorean triplet.
'''
  def checkTriplet(self,a, n):
    	# code here
    	for i in range(n):
    	    a[i]=a[i]*a[i]
    	
    	a.sort()
    	
    	for i in range(n-1):
    	    f=0
    	    l=n-1
    	    while(f<l):
    	        if(a[f]+a[l]==a[i]):
    	            return True
    	        else:
    	            if(a[f]+a[l]<a[i]):
    	                f=f+1
    	            else:
    	                l=l-1
        return False
