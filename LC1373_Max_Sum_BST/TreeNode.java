package LC1373MaxSumBST;

public class TreeNode {
    int val;
    TreeNode leftChild;
    TreeNode rightChild;
    
    int maxSubBSTSum;
    TreeNode maxSubBSTRoot;
    int minOffspringVal; // minimum node value of the subtree rooted at this node
    int maxOffspringVal; // maximum node value of the subtree rooted at this node
    boolean isValidBSTRoot;
    int subtreeSum; // sum of nodes of subtree rooted at this node- does NOT necessarily have to be the maximum sub-BST sum

    public TreeNode(int v)
    {
        this.val = v;
    }

    public int getVal()
    {
        return this.val;
    }

    public TreeNode getLeftChild()
    {
        return this.leftChild;
    }

    public TreeNode getRightChild()
    {
        return this.rightChild;
    }

    public int getMaxSubBSTSum()
    {
        return this.maxSubBSTSum;
    }

    public TreeNode getMaxSubBSTRoot()
    {
        return this.maxSubBSTRoot;
    }

    public int getMinOffspringVal()
    {
        return this.minOffspringVal;
    }

    public int getMaxOffspringVal()
    {
        return this.maxOffspringVal;
    }

    public boolean isValidBSTRoot()
    {
        return this.isValidBSTRoot;
    }

    public int getSubtreeSum()
    {
        return this.subtreeSum;
    }

    public void setLeftChild(int v)
    {
        this.leftChild = new TreeNode(v);
    }

    public void setRightChild(int v)
    {
        this.rightChild = new TreeNode(v);
    }

    public void setMaxSubBSTSum(int v)
    {
        this.maxSubBSTSum = v;
    }

    public void setMaxSubBSTRoot(TreeNode tn)
    {
        this.maxSubBSTRoot = tn;
    }

    public void setMinOffspringVal(int v)
    {
        this.minOffspringVal = v;
    }

    public void setMaxOffspringVal(int v)
    {
        this.maxOffspringVal = v;
    }

    public void setIsValidBSTRoot(boolean isValid)
    {
        this.isValidBSTRoot = isValid;
    }

    public void setSubtreeSum(int sum)
    {
        this.subtreeSum = sum;
    }

    public boolean isLeaf()
    {
        return this.getLeftChild() == null && this.getRightChild() == null;
    }
}
