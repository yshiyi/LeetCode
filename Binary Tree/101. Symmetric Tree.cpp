/*
101. Symmetric Tree
Tree, Depth-first Search, Breath-first Search

Description:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true
           1
      2         2
   3    4    4    3

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
*/

/*
Method 1: Recursive approach
          Similar to 116M. Populating Next Right Pointers in Each Node
          We send two nodes to the recursive function in every iteration.
*/
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return checkSymm(root->left, root->right);
    }
    bool checkSymm(TreeNode* node1, TreeNode* node2){
        if(node1==NULL && node2==NULL){
            return true;
        }else if(node1==NULL && node2!=NULL){
            return false;
        }else if(node1!=NULL && node2==NULL){
            return false;
        }
        if(node1->val!=node2->val){
            return false;
        }else{
            return checkSymm(node1->left, node2->right) && checkSymm(node1->right, node2->left);
        }
    }
};


/* =================================================================== */
/*
Method 2: Iterative approach
          Using queue. The sequence of the nodes is important.
*/
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        q.push(root);
        while(q.size()!=0){
            TreeNode *t1, *t2;
            t1 = q.front(); q.pop();
            t2 = q.front(); q.pop();
            if(t1==NULL && t2==NULL){
                continue;
            }
            if(t1!=NULL && t2==NULL){
                return false;
            }
            if(t1==NULL && t2!=NULL){
                return false;
            }
            if(t1->val!=t2->val){
                return false;
            }
            q.push(t1->left);
            q.push(t2->right);
            q.push(t1->right);
            q.push(t2->left);
        }
        return true;
    }
};
