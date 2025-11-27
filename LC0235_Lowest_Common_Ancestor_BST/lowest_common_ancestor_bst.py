# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        while lca:
            if p.val > lca.val and q.val > lca.val:
                # Go right if both p and q are greater than lca
                lca = lca.right
            elif p.val < lca.val and q.val < lca.val :
                # Go left if both p and q are smaller than lca
                lca = lca.left
            else: 
                # if one of p and q is greater than lca but the other is smaller than lca
                # OR if one of p and q equals lca
                return lca
        return lca
        