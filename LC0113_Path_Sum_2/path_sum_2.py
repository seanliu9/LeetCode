from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = []
        self.running_path = []    

    def rPathSum(self, root: TreeNode, targetSum: int):
        if root is None:
            return

        self.running_path.append(root.val)

        if root.left == None and root.right == None:
            # if root is a leaf
            if root.val == targetSum:
                self.answer.append(list(self.running_path))

        # Check if there is a valid root-to-leaf path in root's left subtree.
        if root.left:
            self.rPathSum(root.left, targetSum - root.val)

        # Check if there is a valid root-to-leaf path in root's right subtree.
        if root.right:
            self.rPathSum(root.right, targetSum - root.val)

        self.running_path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        self.rPathSum(root, targetSum)
        return self.answer