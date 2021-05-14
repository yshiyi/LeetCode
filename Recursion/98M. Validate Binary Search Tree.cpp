/*
98M. Validate Binary Search Tree
Tree, Depth-first Search, Recursion

Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
       5
  1         4
         3     6
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

Similar Questions:
Binary Tree Inorder Traversal - Easy
Find Mode in Binary Search Tree - Easy
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
    
    /* 
       If we don't use a global variable, we can define the function like:
       void traverse(TreeNode* root, vector<int>& res)
       Note: it must be the reference of res.
    */
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
