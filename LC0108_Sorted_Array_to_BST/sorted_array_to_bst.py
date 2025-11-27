from math import ceil
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rConstructBST(self, nums: List[int], start_index: int, end_index: int) -> TreeNode:
        # base cases
        if start_index > end_index:
            return None
        elif start_index == end_index:
            return TreeNode(nums[start_index])
        else:
            median = ceil((start_index + end_index) / 2)
            root = TreeNode(nums[median])
            # Recurse on the subarray to the left of median
            root.left = self.rConstructBST(nums, start_index, median - 1)
            root.right = self.rConstructBST(nums, median + 1, end_index)
            return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        return self.rConstructBST(nums, 0, n - 1)