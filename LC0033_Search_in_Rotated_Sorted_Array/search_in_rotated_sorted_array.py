from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # edge case where nums is just 1 element
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        n = len(nums)
        left = 0
        right = n - 1
    
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # if the left subarray is sorted in ascending order
                if nums[left] <= target < nums[mid]: 
                    # Recurse to the left subarray if target lies in the left subarray
                    right = mid - 1
                else:
                    # Recurse to the right subarray if target lies in the right subarray
                    left = mid + 1
            else: # if the right subarray is sorted in ascending order
                if nums[mid] < target <= nums[right]:
                    # Recurse to the right subarray if target lies in the right subarray
                    left = mid + 1
                else:
                    # Recurse to the left subarray if target lies in the left subarray
                    right = mid - 1
        return -1