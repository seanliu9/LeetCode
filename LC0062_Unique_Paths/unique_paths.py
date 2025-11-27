class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        T = [[1] * n for _ in range(m)] # Initialize T to be a mxn array of all 1's
        for i in range(1, m):
            for j in range(1, n):
                T[i][j] = T[i - 1][j] + T[i][j - 1]
        
        return T[m - 1][n - 1]