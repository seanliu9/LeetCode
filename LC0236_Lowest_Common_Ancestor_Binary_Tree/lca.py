# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rLCA(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or p == root or q == root:
            return root
        # Determine whether p or q exist in the subtree rooted at root.
        left = self.rLCA(root.left, p, q)
        right = self.rLCA(root.right, p, q)
        if left and right:
            # If we find both p and q in the subtree rooted at root, then root is the answer.
            return root
            
        return left or right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.rLCA(root, p, q)