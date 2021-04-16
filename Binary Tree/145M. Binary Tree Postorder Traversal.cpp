/*
145M. Binary Tree Postorder Traversal.cpp
Stack, Tree

Description:
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

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
Output: [2,1]

Similar Questions:
Binary Tree Inorder Traversal - Medium
N-ary Tree Postorder Traversal - Easy
*/

// Method 1: Recursive approach
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        
        postorderRecur(ans, root);
        return ans;
    }
    void postorderRecur(vector<int> &ans, TreeNode* root){
        if (root==NULL){
            return;
        }
        postorderRecur(ans, root->left);
        postorderRecur(ans, root->right);
        ans.push_back(root->val);
    }
};

// Method 2: Iterative approach
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
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
            if(root->left!=NULL){
                st.push(root->left);
            }
            if(root->right!=NULL){
                st.push(root->right);
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
