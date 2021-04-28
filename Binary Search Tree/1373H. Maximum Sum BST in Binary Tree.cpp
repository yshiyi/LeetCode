/*
1373H. Maximum Sum BST in Binary Tree
Dynamic Programming, Binary Search Tree

Description:
Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
                  1
         4                  3
      2     4          2        5
                              4   6

Example 2:
Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:
Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.

Example 4:
Input: root = [2,1,3]
Output: 6

Example 5:
Input: root = [5,4,8,3,null,6,3]
Output: 7


Constraints:
The given binary tree will have between 1 and 40000 nodes.
Each node's value is between [-4 * 10^4 , 4 * 10^4].
*/

/*
Method: Recursive approach
        To apply recursive approach, we need to think through what we plan to do for the current single node.
        There are three things we need to consider:
        1. If the left and right subtree are valid BST.
        2. The maximum value of the left subtree and the minimum value of the right subtree.
        3. The summation of the left subtree and that of the right subtree.
        For this question, we apply post-order traverse method. And it returns four values after each iteration:
        1. valid BST 1/0
        2. max of left subtree
        3. min of right subtree
        4. sum
        Hence, if both sides of subtree are valid BST and the current node value is greater than the max of subtree and less than the min of the right subtree, then this is a valid BST and we can update the sum.
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
    int Maxsum = 0;
    int maxSumBST(TreeNode* root) {
        traverse(root);
        return Maxsum;
    }
    vector<int> traverse(TreeNode* root){
        if(root==NULL){
            // if root is BST, min of right, max of left, sum
            vector<int> res = {1, INT_MAX, INT_MIN, 0};
            return res;
        }
        vector<int> leftTree, rightTree;
        leftTree = traverse(root->left);
        rightTree = traverse(root->right);
        vector<int> res(4);
        if(leftTree[0]==1 && rightTree[0]==1 && root->val>leftTree[2] && root->val<rightTree[1]){
            res[0] = 1;
            res[1] = min(root->val, leftTree[1]);
            res[2] = max(root->val, rightTree[2]);
            res[3] = root->val + leftTree[3] + rightTree[3];
            Maxsum = max(Maxsum, res[3]);
        }else{
            res[0] = 0;
        }
        return res;
    }
};
