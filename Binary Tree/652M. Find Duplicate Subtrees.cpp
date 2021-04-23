/*
652M. Find Duplicate Subtrees
Tree

Description:
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
          1
     2         3
 4         2       4
        4

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]

Similar Questions:
Serialize and Deserialize Binary Tree - Hard
Serialize and Deserialize BST - Medium
Construct String from Binary Tree - Easy
*/

/*
Method: Create an unordered_map to hold the subtrees.
        Using recursive approach to construct subtree as to_string(root->val) + ',' + Recur(root->left)
        + ',' + Recur(root->right).
        Keep in mind that don't save duplicate results when one appears more than two times.
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
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        find(root);
        return res;
    }
    string find(TreeNode* root){
        if(root==NULL){
            return " ";
        }
        string s = to_string(root->val) + ',' + find(root->left) + ',' + find(root->right);
        m[s]++;
        if(m[s]==2){
            res.push_back(root);
        }
        return s;
    }
private:
    unordered_map<string, int> m;
    vector<TreeNode*> res;    
};
