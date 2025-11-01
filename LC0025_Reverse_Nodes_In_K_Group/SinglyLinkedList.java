package LC25ReverseNodesInKGroup;

public class SinglyLinkedList {
    ListNode head;

    // Constructor that takes in an array of integers. The first number is the head, second number is head's next, etc.
    public SinglyLinkedList(int[] arr)
    {
        this.head = new ListNode(arr[0]);
        ListNode currNode = this.head;
        for (int i = 1; i < arr.length; i++)
        {
            currNode.setNext(new ListNode(arr[i]));
            currNode = currNode.getNext();
        }
    }

    public ListNode getHead()
    {
        return this.head;
    }

    public void setHead(ListNode h)
    {
        this.head = h;
    }

    // Reverse k nodes in the list at a time, ignoring any leftover nodes. For example, if the list has 14 nodes and k = 4, then the last 2 nodes should not be modified.
    public void reverseK(int k)
    {
        if (k == 0 || k == 1)
        {
            return;
        }
        ListNode currStart = this.getHead();
        ListNode currNode = this.getHead();
        int[] storage = new int[k]; // array to store the values of the k nodes we are currently reversing
        while (true)
        {
            // Obtain the values of the k nodes.
            for (int i = 0; i < k; i++)
            {
                if (currNode == null)
                {
                    return;
                }
                storage[i] = currNode.getVal();
                currNode = currNode.getNext();
            }
            currNode = currStart;
            // Set new values for those k nodes, effectively reversing them.
            for (int i = 0; i < k; i++)
            {
                currNode.setVal(storage[k - i - 1]);
                currNode = currNode.getNext();
            }
            currStart = currNode;
        }
    }

    // Print the elements of the list, starting with the head.
    public void display()
    {
        ListNode currNode = this.getHead();
        while (currNode != null)
        {
            System.out.print(currNode.getVal() + " -> ");
            currNode = currNode.getNext();
        }
        System.out.print('\n');
    }
}
