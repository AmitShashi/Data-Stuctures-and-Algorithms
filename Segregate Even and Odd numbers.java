/*
Given an array Arr[], write a program that segregates even and odd numbers. 
The program should put all even numbers first in sorted order, 
and then odd numbers in sorted order.
*/
class Solution 
{
    void segregateEvenOdd(int arr[], int n) 
    {
        // code here
        
        ArrayList<Integer> even = new ArrayList<Integer>();
        ArrayList<Integer> odd = new ArrayList<Integer>();
        
        for(int x : arr)
        {
            if(x % 2 == 0)
            {
                even.add(x);
            }
            else
            {
                odd.add(x);
            }
        }
        
        Collections.sort(even);
        Collections.sort(odd);
        
        even.addAll(odd);
        
        int counter = 0;
        for(int x : even)
        {
            arr[counter++] = x;
        }
        
    }
}
