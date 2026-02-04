from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rCountNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.rCountNodes(root.left) + self.rCountNodes(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.rCountNodes(root)
        