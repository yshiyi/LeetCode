/*
100. Same Tree
Tree, Depth-first Search

Description:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
*/

// This is a problem to practise how to convert a recursive algorithm to iterative one.
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

// Method 1: Recursive approach
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p==NULL && q==NULL){
            return true;
        }
        if(p==NULL || q==NULL){
            return false;
        }
        if(p->val != q->val){
            return false;
        }
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

// Method 2: Iterative approach
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<TreeNode*> qP, qQ;
        qP.push(p); qQ.push(q);
        TreeNode *cur1, *cur2;
        while(qP.size()>0 && qQ.size()>0){
            cur1 = qP.front(); qP.pop();
            cur2 = qQ.front(); qQ.pop();
            if(!isValid(cur1, cur2)){
                return false;
            }
            if(cur1 != NULL){
                if(!isValid(cur1->left, cur2->left)){
                    return false;
                }
                if(cur1->left != NULL){
                    qP.push(cur1->left);
                    qQ.push(cur2->left);
                }
                if(!isValid(cur1->right, cur2->right)){
                    return false;
                }
                if(cur1->right != NULL){
                    qP.push(cur1->right);
                    qQ.push(cur2->right);
                }
            }
        }
        return true;
    }
    bool isValid(TreeNode* n1, TreeNode* n2){
        if(n1==NULL && n2==NULL){
            return true;
        }
        if(n1==NULL || n2==NULL){
            return false;
        }
        if(n1->val != n2->val){
            return false;
        }
        return true;
    }
};
