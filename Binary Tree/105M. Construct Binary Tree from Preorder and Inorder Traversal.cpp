/*
105M. Construct Binary Tree from Preorder and Inorder Traversal
Tree, Array, Depth-first Search

Description:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Constraints:
1. preorder and inorder consist of unique values.
2. Each value of inorder also appears in preorder.
3. preorder is guaranteed to be the preorder traversal of the tree.
4. inorder is guaranteed to be the inorder traversal of the tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
          3
      9       20
           15    7


Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Similar Question:
Construct Binary Tree from Inorder and Postorder Traversal - Medium
*/

/*
Method: The structure of preorder is C - L - R, and the structure of inorder is L - C - R.
        We can use preorder to determine the root value, and use inorder to determine the subtrees.
        We need to figure out what we need to do for the root.
        1. Determine the root. It is the first value in preorder.
        2. Determine the left array and the right array for the left side of and the right side of the tree, respectively.
        3. We can do this by using inorder array. We first find the root in the inorder, and then split the array into two subtrees.
        4. The subtrees in preorder can be determined using the length of them.
        5. The termination condition is preStart(prelo) > preEnd(prehi).
        6. Carefully define the start and the end positions.
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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return build(preorder, 0, preorder.size()-1, inorder, 0, inorder.size()-1);
    }
    TreeNode* build(vector<int>& preorder, int prelo, int prehi, vector<int>& inorder, int inlo, int inhi){
        if(prelo > prehi){
            return NULL;
        }
        int rootVal = preorder[prelo], index;
        for(int i=inlo;i<=inhi;i++){
            if(inorder[i]==rootVal){
                index = i;
                break;
            }
        }
        TreeNode* root = new TreeNode(rootVal);
        int inStart_left = inlo, inEnd_left = index - 1, inStart_right = index+1, inEnd_right = inhi;
        int preStart_left = prelo+1, preEnd_left = prelo+index-inlo, preStart_right = prelo+index-inlo+1, preEnd_right = prehi;
        root->left = build(preorder, preStart_left, preEnd_left, inorder, inStart_left, inEnd_left);
        root->right = build(preorder, preStart_right, preEnd_right, inorder, inStart_right, inEnd_right);
        return root;
    }
};
