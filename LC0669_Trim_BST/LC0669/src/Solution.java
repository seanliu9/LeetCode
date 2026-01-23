class Solution {
    public TreeNode rTrimBST(TreeNode root, int low, int high)
    {
        if (root == null)
        {
            return null;
        }
        if (low <= root.val && root.val <= high)
        {
            root.left = this.rTrimBST(root.left, low, high);
            root.right = this.rTrimBST(root.right, low, high);
            return root;
        }
        // Now we know the root is out of bounds
        // Case 1: root is a leaf
        if (root.left == null && root.right == null)
        {
            return null;
        }
        // Case 2: root has only one child
        if (root.left == null)
        {
            return this.rTrimBST(root.right, low, high);
        }
        if (root.right == null)
        {
            return this.rTrimBST(root.left, low, high);
        }
        // Case 3: root has both children
        if (root.val < low)
        {
            return this.rTrimBST(root.right, low, high);
        }
        else if (root.val > high)
        {
            return this.rTrimBST(root.left, low, high);
        }
        return null;
    }

    public TreeNode trimBST(TreeNode root, int low, int high) {
        return this.rTrimBST(root, low, high);
    }
}