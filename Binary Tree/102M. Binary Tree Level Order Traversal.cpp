/*
102M. Binary Tree Level Order Traversal
Tree, Breadth-First-Search

Description:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Similar Questions:
Binary Tree Zigzag Level Order Traversal - Medium
Binary Tree Level Order Traversal II - Medium
Minimum Depth of Binary Tree - Easy
Binary Tree Vertical Order Traversal - Medium
Average of Levels in Binary Tree - Easy
N-ary Tree Level Order Traversal - Medium
Cousins in Binary Tree - Easy
*/

/* 
Method: 
1. Using queue (First-In-First-Out). 
2. On each level, we push each node's value to a vector and save their leaves to the queue (from left to right). 
3. After pushing the node to the vector, we need to pop it from the queue.
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(root==NULL){
            return ans;
        }
        queue<TreeNode*> qt;
        qt.push(root);
        while(qt.size()!=0){
            int n = qt.size();
            vector<int> v;
            while(n){
                root = qt.front();
                qt.pop();
                v.push_back(root->val);
                if(root->left){qt.push(root->left);}
                if(root->right){qt.push(root->right);}
                n--;
            }
            ans.push_back(v);
        }
        return ans;
    }
};
