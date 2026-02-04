struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int rCountNodes(const TreeNode* const node) const
    {
        if (node == nullptr)
        {
            return 0;
        }
        return 1 + this->rCountNodes(node->left) + this->rCountNodes(node->right);
    }

    int countNodes(TreeNode* root) {
        return this->rCountNodes(root);
    }
};