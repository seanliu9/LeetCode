package LC1373MaxSumBST;

public class Driver {
    public static void test1()
    {
        System.out.println("-----STARTING TEST 1-----");
        TreeNode node1 = new TreeNode(4);
        node1.setLeftChild(-3);
        node1.setRightChild(8);
        node1.getRightChild().setLeftChild(2);
        node1.getRightChild().setRightChild(21);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 1-----\n");
    }

    public static void test2()
    {
        System.out.println("-----STARTING TEST 2-----");
        TreeNode node1 = new TreeNode(10);
        node1.setLeftChild(6);
        node1.setRightChild(15);
        node1.getLeftChild().setLeftChild(8);
        node1.getLeftChild().setRightChild(9);
        node1.getRightChild().setLeftChild(13);
        node1.getRightChild().setRightChild(19);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 2-----\n");
    }

    public static void test3()
    {
        System.out.println("-----STARTING TEST 3-----");
        TreeNode node1 = new TreeNode(10);
        node1.setLeftChild(5);
        node1.setRightChild(18);
        node1.getLeftChild().setLeftChild(-2);
        node1.getLeftChild().getLeftChild().setLeftChild(-3);
        node1.getRightChild().setLeftChild(7);
        node1.getRightChild().setRightChild(20);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 3-----\n");
    }

    public static void test4()
    {
        System.out.println("-----STARTING TEST 4-----");
        TreeNode node1 = new TreeNode(4);
        node1.setLeftChild(2);
        node1.setRightChild(5);
        node1.getLeftChild().setLeftChild(1);
        node1.getLeftChild().setRightChild(3);
        node1.getRightChild().setRightChild(6);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 4-----\n");
    }

    public static void test5()
    {
        System.out.println("-----STARTING TEST 5-----");
        TreeNode node1 = new TreeNode(50);
        node1.setLeftChild(8);
        node1.setRightChild(100);
        node1.getLeftChild().setLeftChild(-10);
        node1.getLeftChild().setRightChild(10);
        node1.getLeftChild().getLeftChild().setLeftChild(-15);
        node1.getLeftChild().getLeftChild().setRightChild(-5);
        node1.getLeftChild().getRightChild().setLeftChild(9);
        node1.getLeftChild().getRightChild().setRightChild(11);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 5-----\n");
    }

    public static void test6()
    {
        System.out.println("-----STARTING TEST 6-----");
        TreeNode node1 = new TreeNode(7);
        node1.setLeftChild(5);
        node1.getLeftChild().setLeftChild(4);
        node1.getLeftChild().getLeftChild().setLeftChild(2);
        node1.getLeftChild().getLeftChild().getLeftChild().setLeftChild(-5);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 6-----\n");
    }

    public static void test7()
    {
        System.out.println("-----STARTING TEST 7-----");
        TreeNode node1 = new TreeNode(20);
        node1.setLeftChild(14);
        node1.setRightChild(27);
        node1.getLeftChild().setLeftChild(-6);
        node1.getLeftChild().setRightChild(13);
        node1.getLeftChild().getRightChild().setLeftChild(5);
        node1.getLeftChild().getRightChild().setRightChild(-6);
        node1.getRightChild().setLeftChild(24);
        node1.getRightChild().setRightChild(26);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 7-----\n");
    }

    public static void test8()
    {
        System.out.println("-----STARTING TEST 8-----");
        TreeNode node1 = new TreeNode(5);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 8-----\n");
    }

    public static void test9()
    {
        System.out.println("-----STARTING TEST 9-----");
        TreeNode node1 = new TreeNode(50);
        node1.setLeftChild(25);
        node1.setRightChild(80);
        node1.getLeftChild().setLeftChild(-20);
        node1.getLeftChild().setRightChild(40);
        node1.getLeftChild().getLeftChild().setLeftChild(-10);
        node1.getLeftChild().getLeftChild().setRightChild(20);
        node1.getLeftChild().getLeftChild().getRightChild().setLeftChild(10);
        node1.getLeftChild().getLeftChild().getRightChild().setRightChild(30);
        node1.getLeftChild().getRightChild().setLeftChild(38);
        node1.getLeftChild().getRightChild().setRightChild(45);
        node1.getRightChild().setLeftChild(60);
        node1.getRightChild().setRightChild(100);
        node1.getRightChild().getRightChild().setLeftChild(90);
        node1.getRightChild().getRightChild().setRightChild(120);
        node1.getRightChild().getRightChild().getRightChild().setLeftChild(85);
        node1.getRightChild().getRightChild().getRightChild().setRightChild(130);
        BinaryTree tree = new BinaryTree(node1);
        tree.displayMaxBSTValAndRoot();
        System.out.println("-----FINISHED TEST 9-----\n");
    }

    public static void main(String[] args) {
        test1();
        test2();
        test3();
        test4();
        test5();
        test6();
        test7();
        test8();
        test9();
    }
}
