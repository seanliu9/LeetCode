from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.successor_val = 0

    def rDeleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return
        elif key < root.val:
            root.left = self.rDeleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.rDeleteNode(root.right, key)
            return root
        else: 
            # Case 1: root is a leaf
            if root.left == None and root.right == None:
                return None

            # Case 2: root has only one child
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            
            # Case 3: root has two children
            # Find the successor of root
            root.right = self.rSuccessor(root.right)
            root.val = self.successor_val
            return root

    def rSuccessor(self, root: TreeNode) -> TreeNode:
        if root.left == None:
            self.successor_val = root.val
            return root.right
        else:
            root.left = self.rSuccessor(root.left)
            return root
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        else:
            return self.rDeleteNode(root, key)