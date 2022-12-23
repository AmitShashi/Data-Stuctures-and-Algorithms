'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0
'''
class Solution(object):
    def threeSum(self, nums):
        target = 0 # given in question
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l +=1 
                elif s > target:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r])) # one solution found
                    while l < r and nums[l] == nums[l+1]:   # skip duplicate
                        l += 1
                    while l < r and nums[r] == nums[r-1]:   # skip duplicate
                        r -= 1
                    l += 1; r -= 1                          # find another triplet
        return res
