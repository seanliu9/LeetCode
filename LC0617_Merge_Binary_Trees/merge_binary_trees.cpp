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
    TreeNode* rMergeTrees(const TreeNode* const root1, const TreeNode* const root2) const
    {
        if (root1 == nullptr && root2 == nullptr)
        {
            return nullptr;
        }
        else
        {
            TreeNode* result = new TreeNode((root1 == nullptr ? 0 : root1->val) + (root2 == nullptr ? 0 : root2->val));
            result->left = this->rMergeTrees(root1 == nullptr ? nullptr : root1->left, root2 == nullptr ? nullptr : root2->left);
            result->right = this->rMergeTrees(root1 == nullptr ? nullptr : root1->right, root2 == nullptr ? nullptr : root2->right);
            return result;
        }
    }

    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        return this->rMergeTrees(root1, root2);
    }
};