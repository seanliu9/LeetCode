from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_path_length = 0

    # Recursively calculate the height of each node, while also keeping track of the max path length in the overall tree.
    def rHeight(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_subtree_height = self.rHeight(root.left)
        right_subtree_height = self.rHeight(root.right)

        self.max_path_length = max(self.max_path_length, left_subtree_height + right_subtree_height)

        return 1 + max(left_subtree_height, right_subtree_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.rHeight(root)
        return self.max_path_length