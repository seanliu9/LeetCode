import java.util.HashMap;
class Solution {
    // max we can rob from the subtree rooted at a given node, if we rob this node
    private HashMap<TreeNode, Integer> max_rob;

    // max we can rob from the subtree rooted at a given node, if we DON'T rob this node
    private HashMap<TreeNode, Integer> max_no_rob;

    public Solution()
    {
        this.max_rob = new HashMap<TreeNode, Integer>();
        this.max_no_rob = new HashMap<TreeNode, Integer>();
    }

    public boolean isLeaf(TreeNode node)
    {
        return (node != null) && (node.left == null) && (node.right == null);
    }

    public void rRob(TreeNode root)
    {
        if (root == null)
        {
            return;
        }
        if (this.isLeaf(root))
        {
            this.max_rob.put(root, root.val);
            this.max_no_rob.put(root, 0);
        }
        else
        {
            this.rRob(root.left);
            this.rRob(root.right);
            int a = root.left == null ? 0 : this.max_rob.get(root.left);
            int b = root.right == null ? 0 : this.max_rob.get(root.right);
            int c = root.left == null ? 0 : this.max_no_rob.get(root.left);
            int d = root.right == null ? 0 : this.max_no_rob.get(root.right);
            this.max_rob.put(root, root.val + c + d);
            this.max_no_rob.put(root, Math.max(a, c) + Math.max(b, d));
        }
    }

    public int rob(TreeNode root) {
        this.rRob(root);
        return Math.max(this.max_rob.get(root), this.max_no_rob.get(root));
    }
}
