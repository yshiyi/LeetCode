/*
98M. Validate Binary Search Tree


*/

/*
Method 1: Recursive approach
          The base case is when the node is null. 
          Note the last node is not necessary a valid BST, it can be greater its root.
          There are four conditions to be satisfied:
          1. root->val > minVal. For the left subtree, the minVal is just the INT_MIN.
                                 For the right subtree, the minVal is the root->val.
          2. root->val < maxVal. For the left subtree, the maxVal is the root->val.
                                 For the right subtree, the maxVal is INT_MAX.
          3. root->left and root->right are both valid BST.
*/
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        long minVal = INT64_MIN, maxVal = INT64_MAX;
        return helper(root, minVal, maxVal);
    }
    bool helper(TreeNode* root, long minVal, long maxVal){
        if(root==NULL){
            return true;
        }
        if(root->val > minVal && root->val < maxVal && helper(root->left, minVal, root->val) 
           && helper(root->right, root->val, maxVal)){
            return true;
        }else{
            return false;
        }
    }
};

// Method 2: Iterative approach, use in-order traverse method
class Solution {
public:
    vector<int> res;
    bool isValidBST(TreeNode* root) {
        traverse(root);
        for(int i=0; i<res.size()-1; i++){
            if(res[i]>=res[i+1]){
                return false;
            }
        }
        return true;
    }

    void traverse(TreeNode* root){
        if(root==NULL){
            return;
        }
        traverse(root->left);
        res.push_back(root->val);
        traverse(root->right);
        return;
    }
    
};
