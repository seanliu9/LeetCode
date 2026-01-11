from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # trivial cases
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        dp = [[0] for _ in range(numRows)] # dp[i] = (i + 1)-th row of Pascal's triangle
        dp[0] = [1]
        dp[1] = [1, 1]
        for i in range(2, numRows):
            dp[i] = [1] * (i + 1)
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        
        return dp