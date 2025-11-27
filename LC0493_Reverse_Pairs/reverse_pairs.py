from typing import List

class Solution:
    def rMergeSortAndCount(self, nums: List[int], left: int, right: int):
        if left >= right:
            return 0

        mid = (left + right) // 2

        # Recursively count reverse pairs in the left and right halves
        count = self.rMergeSortAndCount(nums, left, mid)
        count += self.rMergeSortAndCount(nums, mid + 1, right)

        # Count reverse pairs and merge the two halves
        count += self.mergeAndCount(nums, left, mid, right)
        return count
    
    def mergeAndCount(self, nums: List[int], left: int, mid: int, right: int):
        count = 0
        left_ptr = left
        right_ptr = mid + 1

        # Count reverse pairs:
        # For each element in the left subarray, count how many elements in the right subarray
        # satisfy the condition nums[left] > 2 * nums[right]
        while left_ptr <= mid:
            while right_ptr <= right and nums[left_ptr] > 2 * nums[right_ptr]:
                right_ptr += 1
            count += (right_ptr - (mid + 1))
            left_ptr += 1

        # Now merge the two subarrays
        sorted = []
        left_ptr = left
        right_ptr = mid + 1

        while left_ptr <= mid and right_ptr <= right:
            if nums[left_ptr] <= nums[right_ptr]:
                sorted.append(nums[left_ptr])
                left_ptr += 1
            else:
                sorted.append(nums[right_ptr])
                right_ptr += 1

        # Add remaining elements from the left subarray
        while left_ptr <= mid:
            sorted.append(nums[left_ptr])
            left_ptr += 1

        # Add remaining elements from the right subarray
        while right_ptr <= right:
            sorted.append(nums[right_ptr])
            right_ptr += 1

        # Copy the merged result back into the original array
        for i in range(len(sorted)):
            nums[left + i] = sorted[i]

        return count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        return self.rMergeSortAndCount(nums, 0, n - 1)