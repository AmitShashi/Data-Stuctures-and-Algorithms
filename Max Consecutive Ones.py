'''
Question: Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans
