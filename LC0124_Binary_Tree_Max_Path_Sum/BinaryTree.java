package LC124BinaryTreeMaxPathSum;

import java.util.LinkedList;

// Note: This binary tree can be ANY binary tree. We CANNOT assume that is a binary search tree, balanced or complete tree, max/min heap, etc.
public class BinaryTree {
    TreeNode root;

    public BinaryTree(TreeNode rt)
    {
        this.root = rt;
    }

    public TreeNode getRoot()
    {
        return this.root;
    }

    public void rTraverse(TreeNode node)
    {
        if (node == null)
        {
            return;
        }

        // Calculate node's maxLeftBranchVal
        if (node.getLeftChild() != null)
        {
            this.rTraverse(node.getLeftChild());
            node.setMaxLeftBranchVal(Math.max(node.getLeftChild().getVal() + Math.max(node.getLeftChild().getMaxLeftBranchVal(), node.getLeftChild().getMaxRightBranchVal()), 0));
        }
        else
        {
            node.setMaxLeftBranchVal(0);
        }

        // Calculate node's maxRightBranchVal
        if (node.getRightChild() != null)
        {
            this.rTraverse(node.getRightChild());
            node.setMaxRightBranchVal(Math.max(node.getRightChild().getVal() + Math.max(node.getRightChild().getMaxLeftBranchVal(), node.getRightChild().getMaxRightBranchVal()), 0));
        }
        else
        {
            node.setMaxRightBranchVal(0);
        }
        
        // Set node's maxSubtreePathVal and maxSubtreePathPivot
        int tempMaxSubtreePathVal = node.getVal() + node.getMaxLeftBranchVal() + node.getMaxRightBranchVal();
        int leftMaxSubtreePathVal = Math.max(node.getLeftChild() == null ? 0 : node.getLeftChild().getMaxSubtreePathVal(), 0);
        int rightMaxSubtreePathVal = Math.max(node.getRightChild() == null ? 0 : node.getRightChild().getMaxSubtreePathVal(), 0);

        if (tempMaxSubtreePathVal >= leftMaxSubtreePathVal && tempMaxSubtreePathVal >= rightMaxSubtreePathVal)
        {
            node.setMaxSubtreePathVal(tempMaxSubtreePathVal);
            node.setMaxSubtreePathPivot(node);
        }
        else if ((tempMaxSubtreePathVal <= leftMaxSubtreePathVal && leftMaxSubtreePathVal <= rightMaxSubtreePathVal) 
                || (leftMaxSubtreePathVal <= tempMaxSubtreePathVal && tempMaxSubtreePathVal <= rightMaxSubtreePathVal))
        {
            node.setMaxSubtreePathVal(rightMaxSubtreePathVal);
            node.setMaxSubtreePathPivot(node.getRightChild() == null ? null : node.getRightChild().getMaxSubtreePathPivot());
        }
        else if ((tempMaxSubtreePathVal <= rightMaxSubtreePathVal && rightMaxSubtreePathVal <= leftMaxSubtreePathVal)
                || (rightMaxSubtreePathVal <= tempMaxSubtreePathVal && tempMaxSubtreePathVal <= leftMaxSubtreePathVal))
        {
            node.setMaxSubtreePathVal(leftMaxSubtreePathVal);
            node.setMaxSubtreePathPivot(node.getLeftChild() == null ? null : node.getLeftChild().getMaxSubtreePathPivot());
        }
    }

    // Reconstruct the max path (i.e. return list of nodes that make up the max path, in the order they should be visited).
    // Note: Before calling this function, rTraverse() should already have been called, and maxPath should be an empty list.
    // The variable addToFront denotes if we add a node to the front of maxPath or to the back of maxPath.
    public void rReconstructMaxPath(TreeNode node, LinkedList<TreeNode> maxPath, boolean addToFront)
    {
        if (addToFront)
        {
            maxPath.addFirst(node);
        }
        else
        {
            maxPath.addLast(node);
        }
        if (node.getMaxLeftBranchVal() > 0 && node.getMaxLeftBranchVal() >= node.getMaxRightBranchVal())
        {
            this.rReconstructMaxPath(node.getLeftChild(), maxPath, addToFront);
        }
        else if (node.getMaxRightBranchVal() > 0 && node.getMaxRightBranchVal() > node.getMaxLeftBranchVal())
        {
            this.rReconstructMaxPath(node.getRightChild(), maxPath, addToFront);
        }
    }

    // Traverse the tree and then (recursively) reconstruct the max path in the tree.
    public void findMaxPath(LinkedList<TreeNode> maxPath)
    {
        this.rTraverse(this.getRoot());
        TreeNode maxPathPivot = this.getRoot().getMaxSubtreePathPivot();
        if (maxPathPivot == null)
        {
            return;
        }
        maxPath.add(maxPathPivot);
        if (maxPathPivot.getMaxLeftBranchVal() > 0)
        {
            this.rReconstructMaxPath(maxPathPivot.getLeftChild(), maxPath, true);
        }
        if (maxPathPivot.getMaxRightBranchVal() > 0)
        {
            this.rReconstructMaxPath(maxPathPivot.getRightChild(), maxPath, false);
        }
    }
}
