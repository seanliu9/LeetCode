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
    
    # D&C solution
    # Finds the max subarray sum in the subarray of nums from start to end (both inclusive)
    def rMaxSubArray(self, nums: List[int], start: int, end: int):
        # base case
        if start == end:
            return (nums[start], nums[start], nums[start], nums[start])
            
        mid = (start + end) // 2
        left_total, left_start, left_end, left_overall = self.rMaxSubArray(nums, start, mid)
        right_total, right_start, right_end, right_overall = self.rMaxSubArray(nums, mid + 1, end)

        # When merging, we must consider the case of the answer crossing the boundary.
        total = left_total + right_total
        start_max = max(left_start, left_total + right_start)
        end_max = max(right_end, right_total + left_end)
        overall_max = max(left_overall, right_overall, left_end + right_start)

        return total, start_max, end_max, overall_max

    def maxSubArray_DC(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        return self.rMaxSubArray(nums, 0, n - 1)[3]