# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # Count the number of paths in the subtree rooted at root whose sum is targetSum.
    def rPathSum(self, root: TreeNode, targetSum: int) -> int:
        # base case
        if not root:
            return 0

        total = self.rPathSum(root.left, targetSum - root.val) + self.rPathSum(root.right, targetSum - root.val)
        if root.val == targetSum:
            total += 1
        return total

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # trivial case
        if not root:
            return 0
            
        # We must consider both when (A) the path starts at root and (B) the path does not start at root.
        return self.rPathSum(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        