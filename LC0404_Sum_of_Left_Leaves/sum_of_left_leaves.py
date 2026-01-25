from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.total = 0

    def is_leaf(self, node: TreeNode) -> bool:
        return node and (not node.left) and (not node.right)

    def rSumOfLeftLeaves(self, root: TreeNode):
        if not root:
            return

        if self.is_leaf(root.left):
            self.total += root.left.val
        else:
            self.rSumOfLeftLeaves(root.left)

        if not self.is_leaf(root.right):
            self.rSumOfLeftLeaves(root.right)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.rSumOfLeftLeaves(root)
        return self.total