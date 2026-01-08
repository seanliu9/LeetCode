from typing import List

class Solution:
    # basic solution
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(0, curr_sum)
        
        return max_sum
    
    # DP solution
    def maxSubArray_DP(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp_A = [0] * n # dp_A[i] = max subarray sum when we MUST include nums[i]
        dp_B = [0] * n # dp_B[i] = max subarray sum when we CANNOT include nums[i]

        dp_A[0] = nums[0]
        dp_B[0] = nums[0]

        for i in range(1, n):
            dp_A[i] = max(dp_A[i - 1] + nums[i], nums[i])
            dp_B[i] = max(dp_A[i - 1], dp_B[i - 1])
        
        return max(dp_A[n - 1], dp_B[n - 1])