from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left

        self.right = right
        
class Solution:
    def rLRV(self, root: TreeNode, result: List[int]):
        if root == None:
            return
        else:
            self.rLRV(root.left, result)
            self.rLRV(root.right, result)
            result.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        else:
            result = []
            self.rLRV(root, result)
            return result