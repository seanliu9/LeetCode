from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # trivial case
        if not root:
            return []
            
        # Perform level-order traversal on the tree, and the last node we see in each level is the only visible node of that level.
        answer = []
        queue = deque()
        queue.append(root)
        while queue:
            answer.append(queue[-1].val)
            n = len(queue)
            for i in range(n):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return answer