# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # trivial cases
        if not node:
            return None
        elif node.neighbors == []:
            return Node(1)
        
        new_start_node = Node(1)
        #new_adj = 
        nodes = {1: new_start_node} # maps node value to the actual Node object
        stack = deque()
        stack.append(node)
        
        while len(stack) > 0:
            curr_node = stack.pop()
            # Push node's neighbors onto the stack
            for nbr in curr_node.neighbors:
                if nbr.val not in nodes.keys():
                    # Create new node for this neighbor
                    new_node = Node(nbr.val)
                    nodes[nbr.val] = new_node
                    stack.append(nbr)
                    nodes[curr_node.val].neighbors.append(new_node)
                else:
                    # if a new node for nbr has already been created
                    nodes[curr_node.val].neighbors.append(nodes[nbr.val])
        
        return new_start_node
                



        
        
                
       
            
