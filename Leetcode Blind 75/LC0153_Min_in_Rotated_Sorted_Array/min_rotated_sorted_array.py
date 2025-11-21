from typing import List

class Solution:
    def rFindMin(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            # base case 1
            return nums[start]
        elif end == start + 1:
            # base case 2
            return min(nums[start], nums[end])
        else:
            mid = (start + end) // 2
            if nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
                # base case 3: mid is a valley 
                return nums[mid]
            else:
                return min(self.rFindMin(nums, start, mid - 1), self.rFindMin(nums, mid + 1, end))

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        return self.rFindMin(nums, 0, n - 1)