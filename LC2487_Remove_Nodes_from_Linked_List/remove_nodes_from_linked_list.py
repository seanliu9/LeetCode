from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.max_right = 0; # largest value we see to the right

    def rRemoveNodes(self, curr_node: ListNode, prev: ListNode) -> ListNode:
        if not curr_node.next: # base case
            self.max_right = curr_node.val
            return curr_node
        else:
            self.rRemoveNodes(curr_node.next, curr_node)
            if curr_node.val < self.max_right:
                # Remove curr_node if necessary.
                if not prev:
                    # if we need to delete curr_node but it's the first node of the list
                    return curr_node.next
                else:
                    prev.next = curr_node.next
                    return prev.next
            else:
                # no need to remove curr_node
                self.max_right = curr_node.val
                return curr_node

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rRemoveNodes(head, None)