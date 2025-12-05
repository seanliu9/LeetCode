from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.new_right = None

    def rFlatten(self, root: TreeNode):
        if root == None:
            return None
        self.rFlatten(root.right)
        self.rFlatten(root.left)
        root.right = self.new_right
        root.left = None
        self.new_right = root

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        else:
            self.rFlatten(root)
        
        