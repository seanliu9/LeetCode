from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rIdentical(self, root_a: TreeNode, root_b: TreeNode) -> bool:
        if not root_a and not root_b:
            # both trees are null
            return True

        if not root_a or not root_b:
            # only one tree is null
            return False

        if root_a.val != root_b.val:
            return False
        
        return self.rIdentical(root_a.left, root_b.left) and self.rIdentical(root_a.right, root_b.right)

    def rVLR(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.rIdentical(root, subRoot):
            return True
        return self.rVLR(root.left, subRoot) or self.rVLR(root.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Compare the subtree rooted at each node to the tree rooted at subRoot while traversing the tree.
        return self.rVLR(root, subRoot)
                
            
