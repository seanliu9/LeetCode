from typing import List

class Solution:
    # arr must be in non-increasing order
    # Find the maximum index j such that arr[j] >= target
    def rBinarySearch(self, arr: List[int], target: int, left: int, right: int) -> int:
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # For each index i in nums1, find the furthest right index j in nums2 such that nums2[j] >= nums1[i]
        max_pair_dist = 0
        for i in range(len(nums1)):
            if i >= len(nums2) or nums2[i] < nums1[i]:
                continue
            # Perform binary search to find such maximum index j in nums2.
            max_nums2_idx = self.rBinarySearch(nums2, nums1[i], 0, len(nums2) - 1)
            max_pair_dist = max(max_pair_dist, max_nums2_idx - i)
        return max_pair_dist