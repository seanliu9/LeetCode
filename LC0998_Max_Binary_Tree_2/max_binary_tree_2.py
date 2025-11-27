from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def rAppend(self, val: int, root: TreeNode) -> TreeNode:
        if root == None:
            return TreeNode(val)
        elif val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        else:
            root.right = self.rAppend(val, root.right)
            return root

    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.rAppend(val, root)