from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [0] * n
        forward[0] = 1
        backward = [0] * n
        backward[n - 1] = 1
        result = [0] * n
        
        # Populate forward
        for i in range(1, n):
            forward[i] = forward[i - 1] * nums[i - 1]
        
        # Populate backward
        for i in range(n - 2, -1, -1):
            backward[i] = backward[i + 1] * nums[i + 1]
        
        # Compute result
        for i in range(n):
            result[i] = forward[i] * backward[i]
        
        return result