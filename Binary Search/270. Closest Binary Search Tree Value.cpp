/*
270. Closest Binary Search Tree Value
Binary Search Tree

Description:
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:
Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
*/

/*
Method 1: Traverse the tree, compare each node with the target, and keep the minimum difference
          In this method, we use preorder traversal method
*/
class Solution{
public:
    int closestValue(TreeNode *root, double target){
        double diff = numeric_limits<double>::max();
        int res = 0;
        stack<TreeNode*> st;
        st.push(root);
        while(st.size()!=0){
            TreeNode* cur = st.top();
            st.pop();
            if(diff>=abs(cur->val - target)){
                diff = abs(cur->val - target);
                res = cur->val;
            }
            if(cur->right){
                st.push(cur->right);
            }
            if(cur->left){
                st.push(cur->left);
            }
        }
        return res;
    }
}

/*
Method 2: Based on the property of the binary search tree, we can increse the runtime to O(log N).
          We compare cur->val with target. If target > cur->val, we go to right. Otherwise, we go left.
*/
class Solution{
public:
    int closestValue(TreeNode* root, double target){
        double diff = numeric_limits<double>::max();
        int res = 0;
        while(root){
            if(diff>=abs(target - root->val)){
                diff = abs(target - root->val);
                res = root->val;
            }
            root = target > root->val ? root->left : root->right;
        }
        return res;
    }
}

/*
Method 3: Iterative approach I
          1. Compare target with root->val, determine which direction we would go
          2. Call iterative function and obtain the cloest value from that side
          3. Determine which one (i.e., root or l) is closest to the target
*/
class Solution{
public:
    int closestValue(TreeNode* root, double target){
        int res = root->val;
        if(target>root->val && root->left){
            TreeNode* l = closestValue(root->left, target);
            res = abs(target - root->val)>=abs(target - l->val) ? l->val : root->val;
        }else if (target<root->val && root->right){
            TreeNode* r = closestValue(root->right, target);
            res = abs(target - root->val)>=abs(target - r->val) ? r->val : root->val;
        }
        return res;
    }
}

/*
Method 4: Iterative approach II
          1. Compare cur->val with target, and keep recording the minimum difference
          2. Check cur->left and cur->right;
*/
class Solution{
public:
    int closestValue(TreeNode* root, double target){
        double diff = numeric_limits<double>::max();
        int res = 0;
        helper(root, target, diff, res);
        return res;
    }
    void helper(TreeNode* root, double target, double& diff, int& res){
        if(root==NULL){return;}
        if(diff>=abs(target - root->val)){
            diff = abs(target - root->val);
            res = root->val;
        }
        helper(root->left, target, diff, res);
        helper(root->right, target, diff, res);
    }
}










