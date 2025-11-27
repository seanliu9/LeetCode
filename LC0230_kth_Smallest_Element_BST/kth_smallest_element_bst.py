# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # helper method for LVR traversal
    def LVR(self, node, values):
        if (not node.left) and (not node.right): # base case: if node is a leaf
            values.append(node.val)
        else:
            if node.left:
                self.LVR(node.left, values)
            values.append(node.val)
            if node.right:
                self.LVR(node.right, values)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if (not root.left) and (not root.right):
            return root.val

        values = []

        self.LVR(node=root, values=values)
        # After LVR traversal, all the nodes' values are in ascending order.
        return values[k - 1]