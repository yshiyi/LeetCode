/*
637. Average of Levels in Binary Tree
Tree, Breadth-First-Search

Description:
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: root = [3,9,20,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Similar Questions:
Binary Tree Level Order Traversal - Medium
Binary Tree Level Order Traversal II - Medium
*/

// Solution:
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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ans;
        if(!root){
            return ans;
        }
        queue<TreeNode*> qt;
        qt.push(root);
        while(qt.size()){
            double n1 = qt.size(), n2 = n1;
            double sum=0.0;
            while(n1){
                root = qt.front();
                qt.pop();
                sum += (double)root->val;
                if(root->left){qt.push(root->left);}
                if(root->right){qt.push(root->right);}
                n1--;
            }
            ans.push_back(sum/n2);
        }
        return ans;
    }
};
