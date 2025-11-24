public class LC23
{
    public static ListNode? MergeKLists(ListNode[] lists)
    {
        // trivial cases
        if (lists.Length == 0)
        {
            return null;
        }
        if (lists.Length == 1)
        {
            return lists[0];
        }

        // priority queue used to always add the smallest value
        PriorityQueue<ListNode, int> pq = new PriorityQueue<ListNode, int>();

        // Initialize the priority queue with the head of each list.
        foreach (ListNode node in lists)
        {
            if (node != null)
            {
                pq.Enqueue(node, node.val);
            }
        }

        ListNode answer = new ListNode();
        ListNode currAnswerPointer = answer;

        while (pq.Count > 0)
        {
            // Remove the node with the smallest value from pq and add it to answer.
            ListNode nodeToAdd = pq.Dequeue();
            currAnswerPointer.next = new ListNode(nodeToAdd.val);
            currAnswerPointer = currAnswerPointer.next;

            // Add nodeToAdd's next node (in lists) to pq.
            if (nodeToAdd.next != null)
            {
                pq.Enqueue(nodeToAdd.next, nodeToAdd.next.val);
            }
        }

        return answer.next;
    }

    public static ListNode createList(int[] arr)
    {
        ListNode result = new ListNode();
        ListNode curr = result;

        foreach (int x in arr)
        {
            curr.next = new ListNode(x);
            curr = curr.next;
        }

        return result.next;
    }

    public static void printList(ListNode node)
    {
        ListNode curr = node;
        while (curr != null)
        {
            if (curr.next != null)
            {
                Console.Write("{0} -> ", curr.val);
            }
            else // if curr is the last node of the list
            {
                Console.Write("{0}", curr.val);
            }
            curr = curr.next;
        }
        Console.WriteLine();
    }

    public static void test1()
    {
        Console.WriteLine("\n-----Starting test 1-----");

        // 1 -> 2 -> 3
        ListNode list1 = LC23.createList([1, 2, 3]);

        // 4 -> 5 -> 6
        ListNode list2 = LC23.createList([4, 5, 6]);

        // 7 -> 8 -> 9
        ListNode list3 = LC23.createList([7, 8, 9]);

        ListNode[] lists = { list1, list2, list3 };
        ListNode answer = MergeKLists(lists);
        LC23.printList(answer);

        Console.WriteLine("-----Finished test 1-----\n");
    }

    public static void test2()
    {
        Console.WriteLine("\n-----Starting test 2-----");

        // 1 -> 10 -> 15
        ListNode list1 = LC23.createList([1, 10, 15]);

        // 5 -> 7 -> 8 -> 17 -> 36 -> 37 -> 100
        ListNode list2 = LC23.createList([5, 7, 8, 17, 36, 37, 100]);

        // 4 -> 110 -> 122 -> 553
        ListNode list3 = LC23.createList([4, 110, 122, 553]);

        ListNode[] lists = { list1, list2, list3 };
        ListNode answer = MergeKLists(lists);
        LC23.printList(answer);

        Console.WriteLine("-----Finished test 2-----\n");
    }

    public static void test3()
    {
        Console.WriteLine("\n-----Starting test 3-----");

        // Just one list: 30 -> 45 -> 64 -> 152
        ListNode list1 = LC23.createList([30, 45, 64, 152]);

        ListNode[] lists = { list1};
        ListNode answer = MergeKLists(lists);
        LC23.printList(answer);

        Console.WriteLine("-----Finished test 3-----\n");
    }

    static void Main(string[] args)
    {
        Console.WriteLine("----------STARTING TESTS----------");

        LC23.test1();
        LC23.test2();
        LC23.test3();

        Console.WriteLine("----------FINISHED TESTS----------");
    }
}