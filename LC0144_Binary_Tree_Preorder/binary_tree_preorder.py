from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # helper function for preorder traversal
    def rVLR(self, root: TreeNode, result: List[int]):
        if root == None:
            return
        else:
            result.append(root.val)
            self.rVLR(root.left, result)
            self.rVLR(root.right, result)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        else:
            result = []
            self.rVLR(root, result)
            return result