import java.util.List;
import java.util.ArrayList;

// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
    private List<Integer> result; 
    public Solution() {
        this.result = new ArrayList<Integer>(); // stores the answer
    }

    public void rPreorder(Node root)
    {
        if (root == null)
        {
            return;
        }
        this.result.add(root.val);
        for (Node child : root.children)
        {
            this.rPreorder(child);
        }
    }

    public List<Integer> preorder(Node root) {
        if (root == null)
        {
            return new ArrayList<Integer>();
        }
        this.rPreorder(root);
        return this.result;
    }
}