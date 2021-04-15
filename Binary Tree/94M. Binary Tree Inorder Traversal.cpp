/*
94M. Binary Tree Inorder Traversal.cpp
Hash Table, Stack, Tree

Description:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]

Similar Questions:
Validate Binary Search Tree - Medium
Binary Tree Preorder Traversal - Medium
Binary Tree Postorder Traversal - Medium
Binary Search Tree Iterator - Medium
Kth Smallest Element in a BST - Medium
Closest Binary Search Tree Value II - Hard
Inorder Successor in BST - Medium
Convert Binary Search Tree to Sorted Doubly Linked List - Medium
Minimum Distance Between BST Nodes - Easy
*/

// Method 1: Recursive approach
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (root==NULL){
            return ans;
        }
        inorderRecur(ans, root);
        return ans;
    }
    void inorderRecur(vector<int> &ans, TreeNode* root){
        if(root==NULL){
            return;
        }
        inorderRecur(ans, root->left);
        ans.push_back(root->val);
        inorderRecur(ans, root->right);
    }
};

// Method 2: Iterative approach
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        stack<TreeNode*> st;
        while(root!=NULL || st.size()!=0){
            while(root!=NULL){
                st.push(root);
                root = root->left;
            }
            root = st.top();
            ans.push_back(root->val);
            st.pop();
            root = root->right;
        }
        return ans;
    }
};
