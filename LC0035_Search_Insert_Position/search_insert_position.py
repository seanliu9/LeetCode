from typing import List

class Solution:
    # Both start and end are inclusive.
    def rBinarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return self.rBinarySearch(nums, target, mid + 1, end)
            else:
                return self.rBinarySearch(nums, target, start, mid - 1)
        return start

    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # trivial cases
        if target < nums[0]:
            return 0
        if target > nums[n - 1]:
            return n
        
        # Perform binary search to find the index of target, or where target should be inserted.
        return self.rBinarySearch(nums, target, 0, n - 1)