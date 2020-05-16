struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
};


class Solution{
public:
    bool isSymmetric(TreeNode* root){
        if(!root) return true;
        return isSymmetric(root->left, root->right);
    }
    bool isSymmetric(TreeNode* t1, TreeNode* t2){
        if(!t1 && !t2) return true;
        if(!t1 || !t2) return false;
        return t1->val == t2->val
            && isSymmetric(t1->left, t2->right) && isSymmetric(t1->right, t2->left);
    }
};