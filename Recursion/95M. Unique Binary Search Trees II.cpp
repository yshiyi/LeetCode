/*
95M. Unique Binary Search Trees II
Dynamic Programming, Tree

Description:
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 8

Similar Questions:
Unique Binary Search Trees - Medium
Different Ways to Add Parentheses - Medium
*/

/*
Solution: This is a recursive approach
          The basic structure of a binary search tree is that all the nodes in the left subtrees are less than the root and all the nodes in the right subtrees are greater than the root.
          For the target number n, we will treat each of the number between 1 to n as a root.
          Therefore, we should create a recursive function to take a range of numbers.
          Then basic case is when the left limit is equal to the right limit, then we just return the node with that value.
          If left is greater than right, we return null.
          The recurrence relation is for each number between left and right, we send all numbers between left and i-1 to the recursive function and send all the number between i+1 and right to recursive function.
          We are supposed to obtain a constructed left subtree and a constructed right subtree.
          For each node in the left subtree we connect it to the left of the root node.
          For each node in the right subtree we connect it to the right of the root node.
*/
class Solution {
public:

    vector<TreeNode*> recurGen(int left, int right){
        if(left==right){
            return {new TreeNode(left)};
        }else if(left > right){
            return {NULL};
        }
        vector<TreeNode*> res;
        for(int i=left; i<=right; i++){
            vector<TreeNode*> L = recurGen(left, i-1);
            vector<TreeNode*> R = recurGen(i+1, right);
            for(auto l:L){
                for(auto r:R){
                    TreeNode* cur = new TreeNode(i);
                    cur->left = l;
                    cur->right = r;
                    res.push_back(cur);
                }
            }
        }
        
        return res;
    }
    vector<TreeNode*> generateTrees(int n) {
        return recurGen(1, n);
    }
};
