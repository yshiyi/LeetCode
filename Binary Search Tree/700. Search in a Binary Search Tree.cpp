/*
700. Search in a Binary Search Tree

Description:
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.
 

Example 1:
          4
       /     \
      2       7
    /   \
   1     3
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107

Similar Questions:
Closest Binary Search Tree Value - Easy
Insert into a Binary Search Tree - Medium
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
private:
    struct TreeNode {
       int val;
       TreeNode *left;
       TreeNode *right;
       TreeNode() : val(0), left(nullptr), right(nullptr) {}
       TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
       TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
   };
    TreeNode* res;
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root==NULL){
            return NULL;
        }
        // recurSearch(root, val);
        // return res;
        
        queue<TreeNode*> q;
        q.push(root);
        while(q.size()){
            TreeNode* cur = q.front(); q.pop();
            if(cur->val==val){
                return cur;
            }
            if(cur->left != NULL){
                q.push(cur->left);
            }
            if(cur->right != NULL){
                q.push(cur->right);
            }
        }
        
        return NULL;
    }
    // void recurSearch(TreeNode* root, int val){
    //     if(root==NULL){
    //         return;
    //     }
    //     if(root->val == val){
    //         res = root;
    //     }else{
    //         recurSearch(root->left, val);
    //         recurSearch(root->right, val);
    //     }
    // }
};
