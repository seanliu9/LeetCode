from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # returns root node for binary tree from begin_index to end_index (both inclusive)
    def rConstructMaxBinaryTree(self, nums: List[int], begin_index: int, end_index: int) -> TreeNode:
        # base case
        if begin_index > end_index:
            return None
        if begin_index == end_index:
            return TreeNode(nums[begin_index])
        # Find max in nums from begin to end
        max_val = nums[begin_index]
        max_idx = begin_index
        for i in range(begin_index + 1, end_index + 1):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i
        root = TreeNode(max_val)
        # Recursive call on left subarray of max_idx
        root.left = self.rConstructMaxBinaryTree(nums, begin_index, max_idx - 1)
        # Recursive call on right subarray of max_idx
        root.right = self.rConstructMaxBinaryTree(nums, max_idx + 1, end_index)
        return root

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        # trivial case
        if n == 1:
            return TreeNode(nums[0])
        return self.rConstructMaxBinaryTree(nums, 0, n - 1)