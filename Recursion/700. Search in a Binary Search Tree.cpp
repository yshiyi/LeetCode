/*
700. Search in a Binary Search Tree
Tree

Description:
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
            4
        2       7
      1   3

Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:
The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107

Similar Questions:Closest Binary Search Tree Value - Easy
Insert into a Binary Search Tree - Medium
*/

// Method 1: Recursive approach
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root==NULL){
            return NULL;
        }
        recurSearch(root, val);
        return res;
    }
    void recurSearch(TreeNode* root, int val){
        if(root==NULL){
            return;
        }
        if(root->val == val){
            res = root;
        }else{
            recurSearch(root->left, val);
            recurSearch(root->right, val);
        }
    }
private:
    TreeNode* res;
};
