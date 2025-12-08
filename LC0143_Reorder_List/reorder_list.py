from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            # trivial case: if the list only has 1 node
            return

        # Identify the midpoint and tail of the list
        slow_ptr = head
        fast_ptr = head
        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            if fast_ptr.next.next:
                fast_ptr = fast_ptr.next.next
            else:
                fast_ptr = fast_ptr.next
        # Now the midpoint is at slow_ptr and the tail is at fast_ptr.

        # Reverse the list from slow_ptr.next to tail (both inclusive).
        curr = slow_ptr.next
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        slow_ptr.next = None

        # Merge the two lists
        left_ptr = head
        right_ptr = prev
        while right_ptr:
            left_temp = left_ptr.next
            left_ptr.next = right_ptr
            left_ptr = right_ptr
            right_ptr = left_temp


        
