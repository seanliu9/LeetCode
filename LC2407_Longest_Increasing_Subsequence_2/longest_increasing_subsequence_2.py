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
        lis = {nums[0]: 1} # key = nums[i], value = dp_B[i]

        for i in range(1, n):
            dp_A[i] = max(dp_A[i - 1], dp_B[i - 1])
            # To calculate dp_B[i], consider all the values from nums[i] - k to nums[i] - 1 (both inclusive)
            x = float('-inf')
            for j in range(k, 0, -1):
                if nums[i] - j in lis:
                    x = max(x, lis[nums[i] - j] + 1)
            dp_B[i] = max(1, x)
            lis[nums[i]] = dp_B[i]
        
        return max(dp_A[n - 1], dp_B[n - 1])