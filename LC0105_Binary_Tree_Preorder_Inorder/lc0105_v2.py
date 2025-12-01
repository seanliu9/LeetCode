# Note: This solution uses global variables for preorder and inorder.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.preorder = []
        self.inorder = []

    def rBuildTree(self, preorder_left_bound: int, preorder_right_bound: int, inorder_left_bound: int, inorder_right_bound: int) -> TreeNode:
        # base cases
        if preorder_left_bound >= preorder_right_bound or inorder_left_bound >= inorder_right_bound:
            return None
        else: # recursive case
            # root
            root_val = self.preorder[preorder_left_bound]
            root = TreeNode(root_val)
            
            # Determine the inorder inputs to the recursive calls
            # Find the index of root_val in inorder
            root_index = inorder_left_bound
            while self.inorder[root_index] != root_val:
                root_index += 1
            left_subtree_size = root_index - inorder_left_bound

            # Create left and right subtrees
            root.left = self.rBuildTree(preorder_left_bound + 1, preorder_left_bound + 1 + left_subtree_size, inorder_left_bound, root_index)
            root.right = self.rBuildTree(preorder_left_bound + 1 + left_subtree_size, preorder_right_bound, root_index + 1, inorder_right_bound)
            return root
            
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        preorder_left_bound = 0
        preorder_right_bound = len(preorder)
        inorder_left_bound = 0
        inorder_right_bound = len(inorder)
        return self.rBuildTree(preorder_left_bound, preorder_right_bound, inorder_left_bound, inorder_right_bound)