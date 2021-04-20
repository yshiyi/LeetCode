/*
114M. Flatten Binary Tree to Linked List
Tree, Depth-first Search

Description:
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
         1
     2       5
  3     4       6

         1 - 2 - 3 - 4 - 5 - 6
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Similar Questions:
Flatten a Multilevel Doubly Linked List - Medium
Correct a Binary Tree - Medium
*/

// Method 1: Recursive approach
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
    void flatten(TreeNode* root) {
        if(root==NULL){
            return;
        }
        // Flatten the left tree and the right tree sequentially
        flatten(root->left);
        flatten(root->right);
        
        // Save the flat subtress to temps
        TreeNode* tempLeft = root->left;
        TreeNode* tempRight = root->right;
        // Set the left of root to NULL
        root->left = NULL;
        // Connect the flat left tree to the right of root
        root->right = tempLeft;
        
        // Define a temp node and move it the end of the right tree
        TreeNode* cur = root;
        while(cur->right!=NULL){
            cur = cur->right;
        }
        // Connect the flat right tree to the end of right subtree
        cur->right = tempRight;
    }
};


// Method 2: Iterative approach
class Solution {
public:
    void flatten(TreeNode* root) {
        if(root==NULL){
            return;
        }
        stack<TreeNode*> s;
        s.push(root);
        TreeNode* ref = root;
        while(s.size()!=0){
            TreeNode* cur = s.top();
            s.pop();
            if(cur->right!=NULL){s.push(cur->right);}
            if(cur->left!=NULL){
                s.push(cur->left);
                cur->left = NULL;
            }
            
            // Connect the current node to the right of the previous node
            if(cur!=ref){
                ref->right = cur;
                ref = cur;
            }
        }
        return;
    }
};




