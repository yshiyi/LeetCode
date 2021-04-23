/*
104. Maximum Depth of Binary Tree
Tree, Depth-first Search, Recursion

Description:
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
          3
     9        20
           15    7

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

Similar Questions:
Balanced Binary Tree - Easy
Minimum Depth of Binary Tree - Easy
Maximum Depth of N-ary Tree - Easy
Time Needed to Inform All Employees - Medium
*/

/*
Method 1: Using queue (similar to 102M. Binary Tree Level Order Traversal)
*/
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root==NULL){
            return NULL;
        }
        queue<TreeNode*> q;
        q.push(root);
        int res = 0;
        while(q.size()!=0){
            int n = q.size();
            while(n!=0){
                root = q.front();
                q.pop();
                if(root->right!=NULL){q.push(root->right);}
                if(root->left!=NULL){q.push(root->left);}
                n--;
            }
            res++;
        }
        return res;
    }
};

/*
Method 2: Recursive approach
*/
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int res = 1;
        if(root==NULL){
            return 0;
        }
        res = res + max(maxDepth(root->left), maxDepth(root->right));
        return res;
    }
};

