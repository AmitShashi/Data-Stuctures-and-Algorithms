class Solution
{
    //Function to find if there exists a triplet in the array A[] which sums up to X.
    public static boolean find3Numbers(int A[], int n, int X) 
    { 
    
       Arrays.sort(A);
       for(int i=0;i<n;i++)
       {
           int y=X-A[i];     
           int low=i+1, high=n-1;  
           while(low<high){
               if(A[low]+A[high]==y)
                   return true;
               else if(A[low]+A[high]>y)
                   high--;
               else if(A[low]+A[high]<y)
                   low++;
               
        }
      }
      return false;
    }
}
