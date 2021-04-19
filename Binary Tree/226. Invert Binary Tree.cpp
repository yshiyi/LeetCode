/*
226. Invert Binary Tree
Tree

Description:
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
*/

/* 
Solution: This is a question to practice recursive approach to solve tree problems
          Note: the swap function can be operated at pre-order or post-order, but can't be done in-order.
                Pre-order: Swap left and right first, and then go to left and right sequentially
                Post-order: invert left and right first, then swap left and right
                In-order: invert left first, then swap left and right. Then go to right and invert that node again.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL){
            return NULL;
        }
        
        swap(root->right, root->left);
        // root->right = invertTree(root->right);
        invertTree(root->left);
        
        // root->left = invertTree(root->left);
        invertTree(root->right);
        
        return root;
    }
};
