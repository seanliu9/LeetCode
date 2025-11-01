package LC968BinaryTreeCameras;

// Note: This class represents ANY tree (i.e. acyclic graph). It does NOT have to be a binary tree.
public class Tree {
    TreeNode root;

    public Tree(TreeNode rt)
    {
        this.root = rt;
    }

    public TreeNode getRoot()
    {
        return this.root;
    }

    // Recursively calculate the minimum number of cameras needed to monitor every node in the subtree with node as root.
    public void rCalcMinCameras(TreeNode node)
    {
        if (node.isLeaf())
        {
            node.setOffMinCameras(0);
            node.setOnMinCameras(1);
        }
        else
        {
            int offTemp = 0;
            int onTemp = 1;
            for (TreeNode child : node.getChildren())
            {
                this.rCalcMinCameras(child);
                offTemp += child.getOnMinCameras();
                onTemp += Math.min(child.getOffMinCameras(), child.getOnMinCameras());
            }
            node.setOffMinCameras(offTemp);
            node.setOnMinCameras(onTemp);
        }
    }

    public int minCameras()
    {
        this.rCalcMinCameras(this.getRoot());
        return Math.min(this.getRoot().getOffMinCameras(), this.getRoot().getOnMinCameras());
    }
}
