#include <cmath>

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
    int r_left_height(const TreeNode* const node) const
    {
        if (node == nullptr)
        {
            return 0;
        }
        else
        {
            return 1 + this->r_left_height(node->left);
        }
    }

    int r_right_height(const TreeNode* const node) const
    {
        if (node == nullptr)
        {
            return 0;
        }
        else
        {
            return 1 + this->r_right_height(node->right);
        }
    }

    int rCountNodes(const TreeNode* const node) const
    {
        int l_height = this->r_left_height(node);
        int r_height = this->r_right_height(node);
        if (l_height == r_height)
        {
            // Use property of perfect binary tree.
            return pow(2, l_height) - 1;
        }
        else
        {
            return 1 + this->rCountNodes(node->left) + this->rCountNodes(node->right);
        }
    }

    int countNodes(TreeNode* root) {
        return this->rCountNodes(root);
    }
};