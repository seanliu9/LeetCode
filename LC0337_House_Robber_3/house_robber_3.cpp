#include <unordered_map>
#include <algorithm>
using namespace std;

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
    // tracks max amount of money we can rob in the subtree rooted at each node, if we do rob the node
    unordered_map<TreeNode*, int> max_rob; 

    // tracks max amount of money we can rob in the subtree rooted at each node, if we do NOT rob the node
    unordered_map<TreeNode*, int> max_no_rob;


    bool isLeaf(const TreeNode* const node) const
    {
        return node != nullptr && node->left == nullptr && node->right == nullptr;
    }

    void rRob(TreeNode* root)
    {
        if (root == nullptr)
        {
            return;
        }
        if (this->isLeaf(root)) // base case
        {
            this->max_rob[root] = root->val;
            this->max_no_rob[root] = 0;
        }
        else // recursion
        {
            this->rRob(root->left);
            this->rRob(root->right);
            int a = root->left == nullptr ? 0 : this->max_rob[root->left];
            int b = root->right == nullptr ? 0 : this->max_rob[root->right];
            int c = root->left == nullptr ? 0 : this->max_no_rob[root->left];
            int d = root->right == nullptr ? 0 : this->max_no_rob[root->right];
            
            // If we rob root, then we cannot rob either of its children.
            this->max_rob[root] = root->val + c + d;

            // If we don't rob root, then we consider robbings its children.
            this->max_no_rob[root] = max(a, c) + max(b, d);
        }
    }

    int rob(TreeNode* root) {
        this->rRob(root);
        return max(this->max_rob[root], this->max_no_rob[root]);
    }
};