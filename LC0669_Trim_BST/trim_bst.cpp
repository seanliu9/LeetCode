#include <cstddef>
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
    TreeNode* rTrimBST(TreeNode* root, int low, int high)
    {
        if (root == nullptr)
        {
            return NULL;
        }
        if (low <= root->val && root->val <= high)
        {
            root->left = this->rTrimBST(root->left, low, high);
            root->right = this->rTrimBST(root->right, low, high);
            return root;
        }
        // root is not within bounds
        // Case 1: root is a leaf
        if (root->left == nullptr && root->right == nullptr)
        {
            return NULL;
        }
        // Case 2: root has only one child
        if (root->left == nullptr)
        {
            return this->rTrimBST(root->right, low, high);
        }
        if (root->right == nullptr)
        {
            return this->rTrimBST(root->left, low, high);
        }
        // Case 3: root has both children
        if (root->val < low)
        {
            return this->rTrimBST(root->right, low, high);
        }
        else if (root->val > high)
        {
            return this->rTrimBST(root->left, low, high);
        }
        return NULL;
    }

    TreeNode* trimBST(TreeNode* root, int low, int high) {
        return this->rTrimBST(root, low, high);
    }
};