from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {} # maps a node in the original list to its copy in the new list

        # Iterate through the original list, creating a copy of each node if it doesn't already exist.
        curr_node = head
        prev_node = None
        while curr_node:
            if curr_node not in old_to_new:
                curr_node_copy = Node(curr_node.val)
            else:
                curr_node_copy = old_to_new[curr_node]

            # Assign curr_node.random (if necessary).
            if curr_node.random:
                if curr_node.random == curr_node:
                    curr_node_copy.random = curr_node_copy
                else:
                    if curr_node.random not in old_to_new:
                        # Create a copy of curr_node.random and set curr_node_copy.random to it.
                        curr_node_copy_random = Node(curr_node.random.val)
                        curr_node_copy.random = curr_node_copy_random
                        old_to_new[curr_node.random] = curr_node_copy_random
                    else:
                        curr_node_copy.random = old_to_new[curr_node.random]

            old_to_new[curr_node] = curr_node_copy
            
            if prev_node:
                old_to_new[prev_node].next = curr_node_copy

            # Move to the next node in the original list.
            prev_node = curr_node
            curr_node = curr_node.next
        
        return old_to_new[head]
