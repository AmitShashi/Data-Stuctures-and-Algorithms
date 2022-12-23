/*
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
*/
class Solution 
{
    public int firstMissingPositive(int[] nums) 
    {
        if (nums.length == 0) return 1;

        for (int i = 0; i < nums.length; i++) 
        {
            final int num = nums[i];
            final int numM1 = num - 1;

            if (num <= 0) continue;
            if (num > nums.length) continue;
            if (nums[numM1] == num) continue;

            nums[i] ^= nums[numM1];
            nums[numM1] ^= nums[i];
            nums[i] ^= nums[numM1];

            i--;
        }

        int result = 0;
        while (result < nums.length && nums[result] == result + 1) result++;

        return result + 1;
    }
}
