class Solution {
    private int total;
    
    public Solution()
    {
        this.total = 0;
    }

    public boolean isLeaf(TreeNode node)
    {
        return node != null && node.left == null && node.right == null;
    }

    public void rSumOfLeftLeaves(TreeNode root)
    {
        if (root == null)
        {
            return;
        }

        if (this.isLeaf(root.left))
        {
            this.total += root.left.val;
        }
        else
        {
            this.rSumOfLeftLeaves(root.left);
        }

        if (!this.isLeaf(root.right))
        {
            this.rSumOfLeftLeaves(root.right);
        }
    }

    public int sumOfLeftLeaves(TreeNode root) {
        this.rSumOfLeftLeaves(root);
        return this.total;
    }
}