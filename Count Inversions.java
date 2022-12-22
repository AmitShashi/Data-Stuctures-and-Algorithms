/*
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
*/
class Solution
{
    // arr[]: Input Array
    // N : Size of the Array arr[]
    //Function to count inversions in the array.
    static long inversionCount(long arr[], long N)
    {
        // Brute Force Method
        int inv = 0;
        for(int i = 0; i<N; i++)
        {
            for(int j = i+1; j<N; j++)
            {
                if(arr[i]>arr[j])
                    inv++;
            }
        }
        return inv;
    }
}
