# Note: This solution does not use global variables for preorder and inorder, but instead creates a new subarray for each recursive call.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rBuildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # base case
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            # root
            root_val = preorder[0]
            result = TreeNode(root_val)
            # Determine the inputs to the left subtree call
            # Find the index of preorder[0] in inorder
            root_index = 0
            while inorder[root_index] != root_val:
                root_index += 1
            left_inorder = inorder[0:root_index]
            right_inorder = inorder[root_index + 1:]
            # Determine the preorder inputs to the recursive calls
            left_preorder = preorder[1: 1 + len(left_inorder)]
            right_preorder = preorder[len(left_inorder) + 1:]
            # Create left and right subtrees
            result.left = self.rBuildTree(left_preorder, left_inorder)
            result.right = self.rBuildTree(right_preorder, right_inorder)
            return result
            
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.rBuildTree(preorder, inorder)