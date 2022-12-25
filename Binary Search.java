/*
Problem: Given a sorted array arr[] of n elements, write a function to search a given element x in arr[] and return the index of x in the array.
*/
class Solution {
    int binarysearch(int arr[], int n, int k) {
        int low = 0;
        int high = n-1;
        
        while(low<=high){
            int mid = (low +high) /2;
            if(arr[mid] == k) return mid;
            if(k > arr[mid]) low = mid+1;
            if(k < arr[mid]) high = mid-1;
        }
        return -1;
    }
}
