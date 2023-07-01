class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1][:] # Copy last row to dp array

        for i in range(n - 2, -1, -1):  # Start from second last row
            for j in range(i + 1):  # Traverse all elements of the row
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])  # Choose the minimum path

        return dp[0]  # Minimum path sum is at the top of the triangle (dp[0])
