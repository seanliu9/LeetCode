package LC968BinaryTreeCameras;

public class Driver {

    public static void test1()
    {
        System.out.println("-----STARTING TEST 1-----");

        TreeNode node1 = new TreeNode();
        TreeNode node2 = new TreeNode();
        TreeNode node3 = new TreeNode();
        TreeNode node4 = new TreeNode();
        node1.addChild(node2);
        node1.addChild(node3);
        node1.addChild(node4);
        TreeNode node5 = new TreeNode();
        TreeNode node6 = new TreeNode();
        TreeNode node7 = new TreeNode();
        node3.addChild(node5);
        node3.addChild(node6);
        node3.addChild(node7);
        TreeNode node8 = new TreeNode();
        TreeNode node9 = new TreeNode();
        node6.addChild(node8);
        node6.addChild(node9);

        Tree myTree = new Tree(node1);
        int minCameras = myTree.minCameras();
        System.out.println("minimum number of cameras needed: " + minCameras);

        System.out.println("-----FINISHED TEST 1-----\n");
    }

    public static void test2()
    {
        System.out.println("-----STARTING TEST 2-----");

        TreeNode node1 = new TreeNode();
        TreeNode node2 = new TreeNode();
        TreeNode node3 = new TreeNode();
        TreeNode node4 = new TreeNode();
        TreeNode node5 = new TreeNode();
        node1.addChild(node2);
        node1.addChild(node3);
        node1.addChild(node4);
        node1.addChild(node5);
        TreeNode node6 = new TreeNode();
        TreeNode node7 = new TreeNode();
        node2.addChild(node6);
        node2.addChild(node7);
        TreeNode node8 = new TreeNode();
        node3.addChild(node8);
        TreeNode node9 = new TreeNode();
        node4.addChild(node9);
        TreeNode node10 = new TreeNode();
        TreeNode node11 = new TreeNode();
        TreeNode node12 = new TreeNode();
        TreeNode node13 = new TreeNode();
        TreeNode node14 = new TreeNode();
        node5.addChild(node10);
        node5.addChild(node11);
        node5.addChild(node12);
        node5.addChild(node13);
        node5.addChild(node14);

        Tree myTree = new Tree(node1);
        int minCameras = myTree.minCameras();
        System.out.println("minimum number of cameras needed: " + minCameras);

        System.out.println("-----FINISHED TEST 2-----\n");
    }

    public static void test3()
    {
        System.out.println("-----STARTING TEST 3-----");

        TreeNode node1 = new TreeNode();
        TreeNode node2 = new TreeNode();
        TreeNode node3 = new TreeNode();
        TreeNode node4 = new TreeNode();
        TreeNode node5 = new TreeNode();
        node1.addChild(node2);
        node2.addChild(node3);
        node3.addChild(node4);
        node4.addChild(node5);

        Tree myTree = new Tree(node1);
        int minCameras = myTree.minCameras();
        System.out.println("minimum number of cameras needed: " + minCameras);

        System.out.println("-----FINISHED TEST 3-----\n");
    }

    public static void test4()
    {
        System.out.println("-----STARTING TEST 4-----");

        TreeNode node1 = new TreeNode();
        TreeNode node2 = new TreeNode();
        TreeNode node3 = new TreeNode();
        TreeNode node4 = new TreeNode();
        TreeNode node5 = new TreeNode();
        TreeNode node6 = new TreeNode();
        TreeNode node7 = new TreeNode();
        node1.addChild(node2);
        node1.addChild(node3);
        node1.addChild(node4);
        node1.addChild(node5);
        node1.addChild(node6);
        node1.addChild(node7);

        Tree myTree = new Tree(node1);
        int minCameras = myTree.minCameras();
        System.out.println("minimum number of cameras needed: " + minCameras);

        System.out.println("-----FINISHED TEST 4-----\n");

    }
    public static void main(String[] args) {
        test1();
        test2();
        test3();
        test4();
    }
}
