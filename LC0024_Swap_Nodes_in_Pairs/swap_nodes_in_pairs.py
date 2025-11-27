from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rSwapPairs(self, head: ListNode) -> ListNode:
        # base cases
        if head == None:
            return None
        elif head.next == None:
            return head
        # recursive cases
        # Swap head and head.next
        b = head.next
        c = b.next
        head.next = c
        b.next = head
        head.next = self.rSwapPairs(c)
        return b

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rSwapPairs(head)