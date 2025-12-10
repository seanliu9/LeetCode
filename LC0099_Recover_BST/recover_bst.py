from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.lvr = [] # stores Node objects visited by the LVR traversal

    def rLVR(self, root: TreeNode):
        if not root:
            return
        self.rLVR(root.left)
        self.lvr.append(root)
        self.rLVR(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Perform a LVR traversal of the tree.
        self.rLVR(root)

        # Identify the out-of-order pairs in self.LVR. There is either exactly 1 or 2 out-of-order pairs.
        suspects = []
        for i in range(len(self.lvr)):
            if i < len(self.lvr) - 1 and self.lvr[i].val > self.lvr[i + 1].val:
                # if a node has a greater value than its right element
                suspects.append(self.lvr[i])
                suspects.append(self.lvr[i + 1])
        
        # Fix the two nodes who are out-of-order.
        bad_node_1 = suspects[0]
        bad_node_2 = suspects[-1]
        bad_node_1.val, bad_node_2.val = bad_node_2.val, bad_node_1.val

                

