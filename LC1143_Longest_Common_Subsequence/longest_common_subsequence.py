class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # dp[i][j] = length of longest common subsequence between text1's substring from 0 to i 
        # and text2's substring from 0 to j
        dp = [[0] * m for _ in range(n)] 

        # base cases
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        # Populate leftmost column of dp
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] if text1[i] != text2[0] else 1

        # Populate topmost row of dp
        for j in range(1, m):
            dp[0][j] = dp[0][j - 1] if text1[0] != text2[j] else 1

        # Populate rest of dp
        for i in range(1, n):
            for j in range(1, m):
                if text1[i] != text2[j]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        
        return dp[n - 1][m - 1]