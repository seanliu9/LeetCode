struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    int total;
public:
    Solution()
    {
        this->total = 0;
    }

    bool isLeaf(const TreeNode* const root) const 
    {
        return root != nullptr && root->left == nullptr && root->right == nullptr;
    }

    void rSumOfLeftLeaves(const TreeNode* const root)
    {
        if (root == nullptr)
        {
            return;
        }

        if (this->isLeaf(root->left))
        {
            this->total += root->left->val; // We only want the values of the left leaves.
        }
        else
        {
            this->rSumOfLeftLeaves(root->left);
        }

        // If root's right child is a leaf, we don't need to consider it at all.
        if (!this->isLeaf(root->right))
        {
            this->rSumOfLeftLeaves(root->right);
        }
    }

    int sumOfLeftLeaves(TreeNode* root) {
        this->rSumOfLeftLeaves(root);
        return this->total;
    }
};