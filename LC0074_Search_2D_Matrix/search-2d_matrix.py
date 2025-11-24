from typing import List

class Solution:
    # Use binary search to determine which row target would belong to (if it exists).
    # Return -1 if target cannot exist in matrix.
    def r_search_row(self, matrix: List[List[int]], target: int, top: int, bottom: int) -> int:
        if target < matrix[top][0] or target > matrix[bottom][-1]:
            return -1
        if top >= bottom:
            return top
        while top <= bottom:
            mid = (top + bottom) // 2
            # Compare leftmost element of mid-th row to target
            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                return mid
            elif target > matrix[mid][-1]:
                return self.r_search_row(matrix, target, mid + 1, bottom)
            else:
                return self.r_search_row(matrix, target, top, mid - 1)

    # Perform binary search to determine if target exists in an array.
    def r_binarySearch(self, arr: List[int], target: int, left: int, right: int) -> bool:
        if target < arr[0] or target > arr[-1]:
            return False

        if left > right:
            return False

        while left <= right:
            mid = (left + right) // 2
            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                return self.r_binarySearch(arr, target, left, mid - 1)
            else:
                return self.r_binarySearch(arr, target, mid + 1, right)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Determine which row target must be in (if it exists)
        m = len(matrix)
        n = len(matrix[0])
        row = self.r_search_row(matrix, target, 0, m - 1)
        if row == -1:
            return False
        else:
            # Binary search for target in that row
            return self.r_binarySearch(matrix[row], target, 0, n - 1)