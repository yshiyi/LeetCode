/*
112. Path Sum
Tree, Depth-first Search

Description:
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
                      5
              4               8
         11               13      4
      7      2                      1

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

Similar Questions:
Path Sum II - Medium
Binary Tree Maximum Path Sum - Hard
Sum Root to Leaf Numbers - Medium
Path Sum III - Medium
Path Sum IV - Medium
*/

/*
Method 1: Recursive approach
          Depth-first search
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
    bool hasPathSum(TreeNode* root, int targetSum) {
        checkSum(root, targetSum, sum);
        return res;
    }
    void checkSum(TreeNode* root, int targetSum, int sum){
        if(root==NULL){
            return;
        }
        sum += root->val;
        if(sum==targetSum && root->left==NULL && root->right==NULL){
            res = true;
        }
        checkSum(root->left, targetSum, sum);
        checkSum(root->right, targetSum, sum);
    }
private:
    int sum = 0;
    bool res = false;
};


/*
Method 2: Iterative approach, Breadth-first Search
          Using queue, and the elements in queue are the pairs of node and the current sum till this node.
          Then we create a vector to save the sum when we reaches to the end of a subtree.
*/
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root==NULL){
            return false;
        }
        vector<int> res;
        queue<pair<TreeNode*, int>> q;
        q.push(make_pair(root, root->val));
        while(q.size()!=0){
            auto [node, curSum] = q.front(); q.pop();
            if(node->left==NULL && node->right==NULL){
                res.push_back(curSum);
            }
            if(node->left!=NULL){
                q.push({node->left, curSum+node->left->val});
            }
            if(node->right!=NULL){
                q.push({node->right, curSum+node->right->val});
            }
        }
        for(auto v:res){
            if(v==targetSum){
                return true;
            }
        }
        return false;
    }
};
