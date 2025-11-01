package LC124BinaryTreeMaxPathSum;

import java.util.LinkedList;

public class Driver {

    public static void printPath(LinkedList<TreeNode> path)
    {   
        System.out.print("max path: ");
        for (TreeNode node : path) 
        {
            System.out.print(node.getVal() + " -> ");
        }
        System.out.print('\n');
    }

    public static void main(String[] args) {
        System.out.println("-----STARTING TEST 1-----");

        TreeNode root1 = new TreeNode(10);
        root1.setLeftChild(-3);
        root1.setRightChild(5);
        root1.getLeftChild().setLeftChild(16);
        root1.getLeftChild().setRightChild(27);

        BinaryTree tree1 = new BinaryTree(root1);
        LinkedList<TreeNode> maxPath1 = new LinkedList<TreeNode>();
        tree1.findMaxPath(maxPath1);
        System.out.println("max path sum: " + tree1.getRoot().getMaxSubtreePathVal());
        Driver.printPath(maxPath1);

        System.out.println("-----FINISHED TEST 1-----\n");

        System.out.println("-----STARTING TEST 2-----");

        TreeNode root2 = new TreeNode(-7);
        root2.setLeftChild(-9);
        root2.setRightChild(-2);

        BinaryTree tree2 = new BinaryTree(root2);
        LinkedList<TreeNode> maxPath2 = new LinkedList<TreeNode>();
        tree2.findMaxPath(maxPath2);
        System.out.println("max path sum: " + tree2.getRoot().getMaxSubtreePathVal());
        Driver.printPath(maxPath2);


        System.out.println("-----FINISHED TEST 2-----\n");

        System.out.println("-----STARTING TEST 3-----");

        TreeNode root3 = new TreeNode(5);
        root3.setLeftChild(12);
        root3.setRightChild(-49);
        root3.getLeftChild().setLeftChild(-1);
        root3.getLeftChild().setRightChild(-4);
        root3.getLeftChild().getRightChild().setLeftChild(-3);
        root3.getLeftChild().getRightChild().getLeftChild().setRightChild(8);
        root3.getRightChild().setRightChild(40);

        BinaryTree tree3 = new BinaryTree(root3);
        LinkedList<TreeNode> maxPath3 = new LinkedList<TreeNode>();
        tree3.findMaxPath(maxPath3);
        System.out.println("max path sum: " + tree3.getRoot().getMaxSubtreePathVal());
        Driver.printPath(maxPath3);

        System.out.println("-----FINISHED TEST 3-----\n");

        System.out.println("-----STARTING TEST 4-----");

        TreeNode root4 = new TreeNode(-6);
        root4.setLeftChild(-3);
        root4.getLeftChild().setLeftChild(45);
        root4.getLeftChild().setRightChild(-1);
        root4.getLeftChild().getLeftChild().setRightChild(-4);
        root4.getLeftChild().getLeftChild().getRightChild().setLeftChild(19);
        root4.getLeftChild().getLeftChild().getRightChild().setRightChild(62);
        root4.setRightChild(8);

        BinaryTree tree4 = new BinaryTree(root4);
        LinkedList<TreeNode> maxPath4 = new LinkedList<TreeNode>();
        tree4.findMaxPath(maxPath4);
        System.out.println("max path sum: " + tree4.getRoot().getMaxSubtreePathVal());
        Driver.printPath(maxPath4);

    }
}