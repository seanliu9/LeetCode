from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        dp_A = [1] * n # dp_A[i] = length of longest increasing subsequence in nums up to i if we do NOT include nums[i]
        dp_B = [1] * n # dp_B[i] = length of longest increasing subsequence in nums up to i if we include nums[i]
        dp_A[0] = 0
        dp_B[0] = 1

        for i in range(1, n):
            dp_A[i] = max(dp_A[i - 1], dp_B[i - 1])
            # To calculate dp_B[i], consider all the values from nums[0] to nums[i - 1] that can be the value immediately before nums[i]
            x = float('-inf')
            for j in range(0, i):
                if nums[j] < nums[i] and nums[i] - nums[j] <= k:
                    x = max(x, dp_B[j] + 1)
            dp_B[i] = max(x, 1)
        
        return max(dp_A[n - 1], dp_B[n - 1])