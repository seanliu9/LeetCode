# Problem: https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # trivial cases
        if not head:
            return None
        if head.next == None: # if the list only has 1 node
            return head
        
        # Get the values of list and store them in values.
        values = []
        curr_node = head
        while curr_node:
            values.append(curr_node.val)
            curr_node = curr_node.next
        n = len(values)

        # Now reverse the values of the original list
        curr_node = head
        for i in range(n):
            curr_node.val = values[n - 1 - i]
            curr_node = curr_node.next

        return head