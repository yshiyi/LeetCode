/*
106M. Construct Binary Tree from Inorder and Postorder Traversal
Tree, Array, Depth-first Search

Desciption:
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Constraints:
1. inorder and postorder consist of unique values.
2. Each value of postorder also appears in inorder.
3. inorder is guaranteed to be the inorder traversal of the tree.
4. postorder is guaranteed to be the postorder traversal of the tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
          3
      9       20
           15    7

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Similar Quetion:
Construct Binary Tree from Preorder and Inorder Traversal - Medium
*/

/*
Method: The idea is similar to 105M.
        The structure of inorder is L - C - R, the structure of postorder is L - R - C.
        We can use postorder array to determine the root value, and use inorder array to determine the subtrees.
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return build(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
    }
    
    TreeNode* build(vector<int>& inorder, int inStart, int inEnd, vector<int>& postorder, int postStart, int postEnd){
        if (inStart > inEnd){
            return NULL;
        }
        int rootVal = postorder[postEnd], index;
        for(int i=inStart;i<=inEnd;i++){
            if(inorder[i]==rootVal){
                index = i;
                break;
            }
        }
        TreeNode* root = new TreeNode(rootVal);
        int length_left = index - inStart;
        root->left = build(inorder, inStart, index-1, postorder, postStart, postStart+length_left-1);
        root->right = build(inorder, index+1, inEnd, postorder, postStart+length_left, postEnd-1);
        return root;
    }
};
