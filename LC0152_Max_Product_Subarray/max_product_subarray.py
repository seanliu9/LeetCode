from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_prod, min_prod, result = nums[0], nums[0], nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(nums[i], max_prod * nums[i])
            min_prod = min(nums[i], min_prod * nums[i])
            result = max(result, max_prod)
        return result
        