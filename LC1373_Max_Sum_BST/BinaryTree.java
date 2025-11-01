package LC1373MaxSumBST;

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
        if (node.isLeaf())
        {
            node.setMaxSubBSTSum(node.getVal());
            node.setMaxSubBSTRoot(node);
            node.setMinOffspringVal(node.getVal());
            node.setMaxOffspringVal(node.getVal());
            node.setIsValidBSTRoot(true);
            node.setSubtreeSum(node.getVal());
        }
        else
        {
            int maxSubBSTSum = 0;
            TreeNode maxSubBSTRoot = null;
            int minOffSpringVal = 0; 
            int maxOffspringVal = 0; 
            boolean validBSTRoot = true; 
            int subtreeSum = node.getVal(); 

            if (node.getLeftChild() != null)
            {
                this.rTraverse(node.getLeftChild());
                validBSTRoot &= node.getLeftChild().isValidBSTRoot();
                validBSTRoot &= (node.getVal() >= node.getLeftChild().getMaxOffspringVal());
                subtreeSum += node.getLeftChild().getSubtreeSum();
                node.setMinOffspringVal(node.getLeftChild().getMinOffspringVal());
                if (node.getRightChild() == null)
                {
                    node.setMaxOffspringVal(node.getLeftChild().getMaxOffspringVal());
                }
            }
            if (node.getRightChild() != null)
            {
                this.rTraverse(node.getRightChild());
                validBSTRoot &= node.getRightChild().isValidBSTRoot();
                validBSTRoot &= (node.getVal() <= node.getRightChild().getMinOffspringVal());
                subtreeSum += node.getRightChild().getSubtreeSum();
                node.setMaxOffspringVal(node.getRightChild().getMaxOffspringVal());
                if (node.getLeftChild() == null)
                {
                    node.setMinOffspringVal(node.getRightChild().getMinOffspringVal());
                }
            }
            node.setIsValidBSTRoot(validBSTRoot);
            node.setSubtreeSum(subtreeSum);

            if (node.isValidBSTRoot())
            {
                if (node.getRightChild() == null) // if node has only a left child
                {
                    int tempSum = node.getVal() + node.getLeftChild().getMaxSubBSTSum();
                    if (tempSum >= node.getLeftChild().getMaxSubBSTSum())
                    {
                        node.setMaxSubBSTSum(tempSum);
                        node.setMaxSubBSTRoot(node);
                    }
                    else
                    {
                        node.setMaxSubBSTSum(node.getLeftChild().getMaxSubBSTSum());
                        node.setMaxSubBSTRoot(node.getLeftChild().getMaxSubBSTRoot());
                    }
                }
                else if (node.getLeftChild() == null) // if node has only a right child
                {
                    int tempSum = node.getVal() + node.getRightChild().getMaxSubBSTSum();
                    if (tempSum >= node.getRightChild().getMaxSubBSTSum())
                    {
                        node.setMaxSubBSTSum(tempSum);
                        node.setMaxSubBSTRoot(node);
                    }
                    else
                    {
                        node.setMaxSubBSTSum(node.getRightChild().getMaxSubBSTSum());
                        node.setMaxSubBSTRoot(node.getRightChild().getMaxSubBSTRoot());
                    }
                }
                else // if node has both a left child and a right child
                {
                    // If we consider a particular node, then we have to consider all of its descendants.
                    int tempSum = node.getVal() + node.getLeftChild().getSubtreeSum() + node.getRightChild().getSubtreeSum();
                    if (tempSum >= node.getLeftChild().getSubtreeSum() && tempSum >= node.getRightChild().getSubtreeSum())
                    {
                        node.setMaxSubBSTSum(tempSum);
                        node.setMaxSubBSTRoot(node);
                    }
                    else if (node.getLeftChild().getSubtreeSum() >= tempSum && node.getLeftChild().getSubtreeSum() >= node.getRightChild().getSubtreeSum())
                    {
                        node.setMaxSubBSTSum(node.getLeftChild().getSubtreeSum());
                        node.setMaxSubBSTRoot(node.getLeftChild());
                    }
                    else if (node.getRightChild().getSubtreeSum() >= tempSum && node.getRightChild().getSubtreeSum() >= node.getLeftChild().getSubtreeSum())
                    {
                        node.setMaxSubBSTSum(node.getRightChild().getSubtreeSum());
                        node.setMaxSubBSTRoot(node.getRightChild());
                    }
                }
            }
            else // if node is NOT a valid BST root
            {
                int leftMaxSubBSTSum = node.getLeftChild() == null ? (int) Double.NEGATIVE_INFINITY : node.getLeftChild().getMaxSubBSTSum();
                int rightMaxSubBSTSum = node.getRightChild() == null ? (int) Double.NEGATIVE_INFINITY : node.getRightChild().getMaxSubBSTSum();
                if (leftMaxSubBSTSum >= rightMaxSubBSTSum)
                {
                    node.setMaxSubBSTSum(leftMaxSubBSTSum);
                    node.setMaxSubBSTRoot(node.getLeftChild().getMaxSubBSTRoot());
                }
                else
                {
                    node.setMaxSubBSTSum(rightMaxSubBSTSum);
                    node.setMaxSubBSTRoot(node.getRightChild().getMaxSubBSTRoot());
                }
            }
        }
    }

    public void displayMaxBSTValAndRoot()
    {
        this.rTraverse(this.getRoot());
        System.out.println("max BST value in the tree: " + this.getRoot().getMaxSubBSTSum());
        System.out.println("max BST's root has value " + this.getRoot().getMaxSubBSTRoot().getVal());
    }
}
