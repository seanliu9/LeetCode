package LC968BinaryTreeCameras;

import java.util.LinkedList;

public class TreeNode {
    static int number = 1;
    int label;
    LinkedList<TreeNode> children;
    int offMinCameras; // minimum number of cameras required to monitor every node when this node has a camera on it
    int onMinCameras; // minimum number of cameras required to monitor every node when this node does NOT have a camera on it

    public TreeNode()
    {
        // First TreeNode has number 1, second TreeNode has number 2, etc.
        this.label = number;
        this.children = new LinkedList<TreeNode>();
        number++; 
    }

    public int getLabel()
    {
        return this.label;
    }

    public LinkedList<TreeNode> getChildren()
    {
        return this.children;
    }

    public int getOffMinCameras()
    {
        return this.offMinCameras;
    }

    public int getOnMinCameras()
    {
        return this.onMinCameras;
    }

    public void addChild(TreeNode child)
    {
        this.getChildren().add(child);
    }

    public void setOffMinCameras(int numCameras)
    {
        this.offMinCameras = numCameras;
    }

    public void setOnMinCameras(int numCameras)
    {
        this.onMinCameras = numCameras;
    }

    public boolean isLeaf()
    {
        return this.getChildren().isEmpty();
    }
}
