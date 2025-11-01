package LC124BinaryTreeMaxPathSum;

public class TreeNode {
    int val;
    TreeNode leftChild;
    TreeNode rightChild;
    int maxLeftBranchVal;
    int maxRightBranchVal;
    int maxSubtreePathVal;
    TreeNode maxSubtreePathPivot;

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

    public int getMaxLeftBranchVal()
    {
        return this.maxLeftBranchVal;
    }

    public int getMaxRightBranchVal()
    {
        return this.maxRightBranchVal;
    }

    public int getMaxSubtreePathVal()
    {
        return this.maxSubtreePathVal;
    }

    public TreeNode getMaxSubtreePathPivot()
    {
        return this.maxSubtreePathPivot;
    }

    public void setLeftChild(int v)
    {
        this.leftChild = new TreeNode(v);
    }

    public void setRightChild(int v)
    {
        this.rightChild = new TreeNode(v);
    }

    public void setMaxLeftBranchVal(int mlbv)
    {
        this.maxLeftBranchVal = mlbv;
    }

    public void setMaxRightBranchVal(int mrbv)
    {
        this.maxRightBranchVal = mrbv;
    }

    public void setMaxSubtreePathVal(int mspv)
    {
        this.maxSubtreePathVal = mspv;
    }

    public void setMaxSubtreePathPivot(TreeNode pivot)
    {
        this.maxSubtreePathPivot = pivot;
    }

    public boolean isLeaf()
    {
        return this.getLeftChild() == null && this.getRightChild() == null;
    }
}

