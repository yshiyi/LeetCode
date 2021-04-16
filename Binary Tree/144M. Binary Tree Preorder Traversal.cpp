/*
144M. Binary Tree Preorder Traversal.cpp
Stack, Tree

Description:
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example 5:
Input: root = [1,null,2]
Output: [1,2]

Similar Questions:
Binary Tree Inorder Traversal - Medium
Verify Preorder Sequence in Binary Search Tree - Medium
N-ary Tree Preorder Traversal - Easy
*/

// Method 1: Recursive
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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        preorderRecur(ans, root);
        return ans;
    }
    void preorderRecur(vector<int>& ans, TreeNode* root){
        if(root==NULL){
            return;
        }
        ans.push_back(root->val);
        preorderRecur(ans, root->left);
        preorderRecur(ans, root->right);
    }
};

// Method 2: Iterative, use stack to save the root
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        stack<TreeNode*> st;
        while(true){
            while(root!=NULL){
                st.push(root);
                ans.push_back(root->val);
                root = root->left;
            }
            if(st.size()==0){
                break;
            }
            root = st.top();
            st.pop();
            root = root->right;
        }
        return ans;
    }
};

// Method 3: Iterative approach
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        stack<TreeNode*> st;
        st.push(root);
        while(st.size()!=0){
            root = st.top();
            st.pop();
            ans.push_back(root->val);
            if(root->right!=NULL){
                st.push(root->right);
            }
            if(root->left!=NULL){
                st.push(root->left);
            }
        }
        return ans;
    }
};
