package LC25ReverseNodesInKGroup;

public class ListNode {
    int val;
    ListNode next;

    public ListNode(int v)
    {
        this.val = v;
    }

    public ListNode(int v, ListNode nextNode)
    {
        this.val = v;
        this.next = nextNode;
    }

    public int getVal()
    {
        return this.val;
    }

    public ListNode getNext()
    {
        return this.next;
    }

    public void setVal(int v)
    {
        this.val = v;
    }

    public void setNext(ListNode nextNode)
    {
        this.next = nextNode;
    }
}
