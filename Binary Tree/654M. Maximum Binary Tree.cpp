/*
654M. Maximum Binary Tree
Tree

Description:
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.


Example 1:
Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
           6
     3          5
       2      0
         1

Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

Example 2:
Input: nums = [3,2,1]
Output: [3,null,2,null,1]

Similar Questions:
Maximum Binary Tree II - Medium
*/


/*
Solution: Find the max element, and create a new node using this max. Then work on the left and the right subarray recursively.
          The terminate condition is when lo > hi.
          To find the max element, we need to loop from i=lo to i=hi.
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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return buildTree(nums, 0, nums.size()-1);
    }
    
    TreeNode* buildTree(vector<int>& nums, int lo, int hi){
        if(lo > hi){
            return NULL;
        }
        int maxVal = INT_MIN, index;
        for(int i=lo;i<=hi;i++){
            if(nums[i]>maxVal){
                maxVal = nums[i];
                index = i;
            }
        }
        TreeNode* root = new TreeNode(maxVal);
        root->left = buildTree(nums, lo, index-1);
        root->right = buildTree(nums, index+1, hi);
        return root;
    }
};


/*
Method 2: Iterative approach
The key idea is:
1. We scan numbers from left to right, build the tree one node by one step;
2. We use a stack to keep some (not all) tree nodes and ensure a decreasing order;
3. For each number, we keep pop the stack until empty or a bigger number; 
   The bigger number (if exist, it will be still in stack) is current number's root, 
   and the last popped number (if exist) is current number's left child 
   (temporarily, this relationship may change in the future); Then we push current number into the stack.
*/
class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        vector<TreeNode*> stk;
        for (int i = 0; i < nums.size(); ++i)
        {
            TreeNode* cur = new TreeNode(nums[i]);
            while (!stk.empty() && stk.back()->val < nums[i])
            {
                cur->left = stk.back();
                stk.pop_back();
            }
            if (!stk.empty())
                stk.back()->right = cur;
            stk.push_back(cur);
        }
        return stk.front();
    }
};




