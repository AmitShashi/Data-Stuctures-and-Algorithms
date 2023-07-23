class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first] #swap
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first] #swap
                
        n = len(nums)
        output = []
        backtrack(0)
        return output
