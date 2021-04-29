/*
222M. Count Complete Tree Nodes
Binary Tree, Tree

Description:
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6
          1
    2          3
 4    5     6   


Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.

Follow up: 
Traversing the tree to count the number of nodes in the tree is an easy solution but with O(n) complexity. Could you find a faster algorithm?

Similar Question:
Closest Binary Search Tree Value - Easy
*/

/*
Method 1: Traverse the tree using Breadth-first Search
*/
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(root==NULL){
            return 0;
        }
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* cur;
        int res = 0;
        while(q.size()!=0){
            cur = q.front(); q.pop();
            res++;
            if(cur->left!=NULL){
                q.push(cur->left);
            }
            if(cur->right!=NULL){
                q.push(cur->right);
            }
        }
        return res;
    }
};

/*
Method 2: Recursive approach
*/
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == NULL) return 0;
        TreeNode *leftTree = root, *rightTree = root;
        int hl = 0, hr = 0;
        while(leftTree!=NULL){
            leftTree = leftTree->left;
            hl++;
        }
        while(rightTree!=NULL){
            rightTree = rightTree->right;
            hr++;
        }
        if(hl==hr){
            return pow(2, hl) - 1;
        }
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
