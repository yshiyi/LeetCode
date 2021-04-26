/*
236M. Lowest Common Ancestor of a Binary Tree
Tree

Description:
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
                3
         5            1
      6     2      0     8
          7   4

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.

Similar Questions:
Lowest Common Ancestor of a Binary Search Tree - Easy
Smallest Common Region - Medium
Lowest Common Ancestor of a Binary Tree II - Medium
Lowest Common Ancestor of a Binary Tree III - Medium
Lowest Common Ancestor of a Binary Tree IV - Medium
*/

/*
Method 1: Recursive approach
          When apply recursive approach, we only need to consider what we need to do for a single node.
          1. We need to check if the root is p or q. If so, root is the LCA.
          2. We inquire the left subtree recursion and the right subtree recursion.
          3. If both of them are not NULL, in other words, they are either p or q, then the root is LCA.
          4. The subtree that returns non-NULL value is the root. In other words, the other target root is
             in the subtree of this root.
*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==NULL)
            return NULL;
        if(root==p || root==q)
            return root;
        TreeNode* left=lowestCommonAncestor(root->left,p,q);
        TreeNode* right=lowestCommonAncestor(root->right,p,q);
        if(left!=NULL && right!=NULL)
            return root;
        else
        {
            if(left!=NULL)
                return left;
            return right;
        }
    }
};


/*
Method 2: Iterative approach
          Use a map to save the current node and its parent.
          We traverse the tree and save all the nodes and their corresponding parents to the map.
          Then, we create a set and save all the ancestors of p to the set.
          Finally, we check the ancestors of q and find the one that appears in the p's set.
*/
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==NULL){
            return NULL;
        }
        unordered_map<TreeNode*, TreeNode*> m;
        m.insert({root, NULL});
        stack<TreeNode*> s;
        s.push(root);
        TreeNode* cur;
        while(s.size()!=0){
            cur = s.top(); s.pop();
            if(cur->right!=NULL){
                s.push(cur->right);
                m.insert({cur->right, cur});
            }
            if(cur->left!=NULL){
                s.push(cur->left);
                m.insert({cur->left, cur});
            }
        }
        set<TreeNode*> s_anc;
        while(m[p]!=NULL){
            s_anc.insert(p);
            p = m[p];
        }
        while(m[q]!=NULL){
            if(s_anc.find(q)!=s_anc.end()){
                break;
            }
            q = m[q];
        }
        return q;
    }
};
