from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rMinDepth(self, root: TreeNode) -> int:
        if root == None:
            return float('inf')
        elif root.left == None and root.right == None:
            # base case: if root is a leaf
            return 1
        else:
            return 1 + min(self.rMinDepth(root.left), self.rMinDepth(root.right))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.rMinDepth(root)