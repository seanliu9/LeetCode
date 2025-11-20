from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        result = []
        n = len(q)
        while n != 0:
            temp = []
            for i in range(n):
                new_node = q.popleft()
                temp.append(new_node.val)
                if new_node.left:
                    q.append(new_node.left)
                if new_node.right:
                    q.append(new_node.right)
            result.append(temp)
            n = len(q)
        return result