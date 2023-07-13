class Solution(object):
    def wordBreak(self, s, wordDict):

        # Convert the word dictionary into a set for efficient lookups
        wordDict = set(wordDict)

        # Initialize the dp array
        dp = [False] * (len(s) + 1)

        # The empty string can be segmented into a sequence of dictionary words
        dp[0] = True

        # Iterate over the string
        for i in range(1, len(s) + 1):
            # Try all possible word endings at the current position
            for j in range(i):
                # If the substring s[j:i] is in the word dictionary and the substring s[0:j] can be segmented,
                # then the substring s[0:i] can also be segmented
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    # No need to check other possibilities once we found a valid segmentation
                    break

        # Return whether the entire string can be segmented
        return dp[len(s)]
