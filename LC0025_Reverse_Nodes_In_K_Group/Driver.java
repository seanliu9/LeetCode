package LC25ReverseNodesInKGroup;

public class Driver {
    public static void main(String[] args) {
        int[] vals = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        SinglyLinkedList sll = new SinglyLinkedList(vals);
        System.out.println("Before reversing:");
        sll.display();

        sll.reverseK(4);
        System.out.println('\n' + "After reversing (with k = 4):" + '\n');
        sll.display();

        sll.reverseK(9);
        System.out.println('\n' + "After reversing (with k = 9):" + '\n');
        sll.display();

        sll.reverseK(5);
        System.out.println('\n' + "After reversing (with k = 5):" + '\n');
        sll.display();
    }
}