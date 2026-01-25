from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        # maps node to max amount of money we can make from robbing the subtree rooted at the node, if we do rob this node
        self.max_rob = {} 
        # maps node to max amount of money we can make from robbing the subtree rooted at the node, if we do NOT rob this node
        self.max_no_rob = {} 

    def is_leaf(self, node: TreeNode) -> bool:
        return node and (not node.left) and (not node.right)

    def rRob(self, root: TreeNode):
        if not root:
            return
        if self.is_leaf(root):
            self.max_rob[root] = root.val
            self.max_no_rob[root] = 0
        else:
            self.rRob(root.left)
            self.rRob(root.right)
            a = self.max_no_rob[root.left] if root.left else 0
            b = self.max_no_rob[root.right] if root.right else 0
            c = self.max_rob[root.left] if root.left else 0
            d = self.max_rob[root.right] if root.right else 0

            # If we rob root, then we cannot rob either of its children.
            self.max_rob[root] = root.val + a + b

            # If we don't rob root, then we have the choice of either robbing or not robbing either of its children.
            self.max_no_rob[root] = max(a, c) + max(b, d)

    def rob(self, root: Optional[TreeNode]) -> int:
        self.rRob(root)
        return max(self.max_rob[root], self.max_no_rob[root])