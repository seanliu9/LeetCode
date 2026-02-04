import java.util.HashMap;

public class Solution {
    public Node copyRandomList(Node head) {
        if (head == null)
        {
            return null;
        }

        HashMap<Node, Node> old_to_new = new HashMap<Node, Node>(); 
        Node curr_node = head;
        Node prev_node = null;

        while (curr_node != null)
        {
            Node curr_node_copy;
            if (old_to_new.containsKey(curr_node))
            {
                curr_node_copy = old_to_new.get(curr_node);
            }
            else
            {
                curr_node_copy = new Node(curr_node.val);
            }

            // Assign curr_node_copy.random (if necessary).
            if (curr_node.random != null)
            {
                if (curr_node.random == curr_node)
                {
                    curr_node_copy.random = curr_node_copy;
                }
                else
                {
                    if (old_to_new.containsKey(curr_node.random))
                    {
                        curr_node_copy.random = old_to_new.get(curr_node.random);
                    }
                    else
                    {
                        // Create a copy of curr_node.random, and set curr_node_copy.random to it.
                        Node curr_node_copy_random = new Node(curr_node.random.val);
                        curr_node_copy.random = curr_node_copy_random;
                        old_to_new.put(curr_node.random, curr_node_copy_random);
                    }
                }
            }

            old_to_new.put(curr_node, curr_node_copy);

            if (prev_node != null)
            {
                old_to_new.get(prev_node).next = curr_node_copy;
            }

            // Move to the next node in the original list.
            prev_node = curr_node;
            curr_node = curr_node.next;
        }

        return old_to_new.get(head);
    }
}
