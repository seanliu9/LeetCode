# Note: This solution uses global variables for inorder and postorder.
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.inorder = []
        self.postorder = []

    def rBuildTree(self, inorder_left_bound: int, inorder_right_bound: int, postorder_left_bound: int, postorder_right_bound: int) -> TreeNode:
        # base case
        if inorder_left_bound >= inorder_right_bound or postorder_left_bound >= postorder_right_bound:
            return None
        else: # recursive case
            # root
            root_val = self.postorder[postorder_right_bound - 1]
            root = TreeNode(root_val)
            # Determine the inorder inputs to the recursive calls
            # Find the index of root_val in inorder
            root_index = inorder_left_bound
            while self.inorder[root_index] != root_val:
                root_index += 1

            left_subtree_size = root_index - inorder_left_bound
            
            # Build left and right subtrees
            root.left = self.rBuildTree(inorder_left_bound, root_index, postorder_left_bound, postorder_left_bound + left_subtree_size)
            root.right = self.rBuildTree(root_index + 1, inorder_right_bound, postorder_left_bound + left_subtree_size, postorder_right_bound - 1)
            return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.postorder = postorder
        inorder_left_bound = 0
        inorder_right_bound = len(inorder)
        postorder_left_bound = 0
        postorder_right_bound = len(postorder)
        return self.rBuildTree(inorder_left_bound, inorder_right_bound, postorder_left_bound, postorder_right_bound)