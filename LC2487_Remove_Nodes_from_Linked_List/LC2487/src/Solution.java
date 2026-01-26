class Solution {
    private int max_right; // max value we see to the right
    
    public Solution()
    {
        this.max_right = 0;
    }

    public ListNode rRemoveNodes(ListNode curr_node, ListNode prev)
    {
        if (curr_node.next == null)
        {
            // base case
            this.max_right = curr_node.val;
            return curr_node;
        }
        else
        {
            this.rRemoveNodes(curr_node.next, curr_node);
            if (curr_node.val < this.max_right)
            {
                // Remove curr_node
                if (prev == null)
                {
                    // if we need to remove curr_node but it's the first node in the list
                    return curr_node.next;
                }
                else
                {
                    prev.next = curr_node.next;
                    return prev.next;
                }
            }
            else
            {
                // no need to remove curr_node
                this.max_right = curr_node.val;
                return curr_node;
            }
        }
    }

    public ListNode removeNodes(ListNode head) {
        return this.rRemoveNodes(head, null);
    }
}