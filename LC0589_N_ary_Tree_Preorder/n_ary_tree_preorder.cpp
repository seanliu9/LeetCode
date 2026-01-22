#include <vector>
using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};


class Solution {
private:
    vector<int> result;
public:
    // constructor
    Solution()
    {
        this->result = vector<int>();
    }

    void rPreorder(Node* root)
    {
        if (root == nullptr)
        {
            return;
        }
        this->result.push_back(root->val);
        for (Node* child : root->children)
        {
            this->rPreorder(child);
        }
    }

    vector<int> preorder(Node* root) {
        if (root == nullptr)
        {
            return vector<int>();
        }
        this->rPreorder(root);
        return this->result;
    }
};