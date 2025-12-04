from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rHeight(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.rHeight(root.left), self.rHeight(root.right))

    def rIsBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            left_height = self.rHeight(root.left)
            right_height = self.rHeight(root.right)
            return abs(left_height - right_height) <= 1 and self.rIsBalanced(root.left) and self.rIsBalanced(root.right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            return self.rIsBalanced(root)