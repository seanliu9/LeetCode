from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rTrimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return
        if low <= root.val <= high: # root is within boundaries
            root.left = self.rTrimBST(root.left, low, high)
            root.right = self.rTrimBST(root.right, low, high)
            return root
        else: # root is NOT within boundaries, and must be removed
            # Case 1: root is a leaf
            if (not root.left) and (not root.right):
                return None

            # Case 2: root has only one child
            if not root.left:
                return self.rTrimBST(root.right, low, high)
            if not root.right:
                self.rTrimBST(root.left, low, high)
                
            # Case 3: root has both children
            # Observation: If root.val < low, then its left subtree definitely must be removed (but we might keep its right subtree).
            # Conversely, if root.val > high, then its right subtree definitely must be removed (but we might keep its left subtree).
            if root.val < low:
                return self.rTrimBST(root.right, low, high)
            elif root.val > high:
                return self.rTrimBST(root.left, low, high)
            else:
                return None

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.rTrimBST(root, low, high)