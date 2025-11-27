from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rConstructFBT(self, n: int) -> List[TreeNode]:
        prev_results = {} # maps n to its previously known result (if it has one)
        # base cases
        if n in prev_results:
            return prev_results[n]
        elif n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        elif n == 3:
            root = TreeNode(0)
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            return [root]
        else: 
            # recursive case
            result = []
            for i in range(1, n, 2): # Consider all possible number of nodes in left subtree of root
                j = n - 1 - i # number of nodes in right subtree of root
                left_trees = self.rConstructFBT(i)
                right_trees = self.rConstructFBT(j)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        result.append(root)
            prev_results[n] = result
            return result


    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.rConstructFBT(n)