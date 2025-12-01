# Note: This solution does not use global variables for inorder and postorder, but instead creates a new subarray for each recursive call.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rBuildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # base cases
        if len(inorder) == 0:
            return None
        elif len(inorder) == 1:
            return TreeNode(inorder[0])
        else: # recursive case
            # root
            root_val = postorder[-1]
            result = TreeNode(root_val)
            # Determine the inorder inputs to the recursive calls
            # Find the index of root_val in inorder
            root_index = 0
            while inorder[root_index] != root_val:
                root_index += 1
            left_inorder = inorder[0: root_index]
            right_inorder = inorder[root_index + 1:]
            # Determine the preorder inputs to the recursive calls
            left_postorder = postorder[0: len(left_inorder)]
            right_postorder = postorder[len(left_inorder): -1]
            # Create left and right subtrees
            result.left = self.rBuildTree(left_inorder, left_postorder)
            result.right = self.rBuildTree(right_inorder, right_postorder)
            return result

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.rBuildTree(inorder, postorder)