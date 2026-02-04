class Solution {
    public int rCountNodes(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        return 1 + this.rCountNodes(root.left) + this.rCountNodes(root.right);
    }

    public int countNodes(TreeNode root) {
        return this.rCountNodes(root);
    }
}