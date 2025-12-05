from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rHasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root.left == None and root.right == None:
            # if root is a leaf
            if root.val == targetSum:
                return True

        # Check if there is a valid root-to-leaf path in root's left subtree.
        left_success = False
        if root.left:
            left_success = self.rHasPathSum(root.left, targetSum - root.val)
        if left_success: 
            # We can prematurely return True if we find a valid root-to-leaf path in root's left subtree.
            return True

        # Check if there is a valid root-to-leaf path in root's right subtree.
        right_success = False
        if root.right:
            right_success = self.rHasPathSum(root.right, targetSum - root.val)

        return left_success or right_success

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        return self.rHasPathSum(root, targetSum)