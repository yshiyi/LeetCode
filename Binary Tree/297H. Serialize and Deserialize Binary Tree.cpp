/*
297H. Serialize and Deserialize Binary Tree
Tree, Design

Description:
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
               1
          2         3
                4      5

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

Similar Questions:
Encode and Decode Strings - Medium
Serialize and Deserialize BST - Medium
Find Duplicate Subtrees - Medium
Serialize and Deserialize N-ary Tree - Hard
*/

/*
Method: Recursion
        We can use pre-order method to traverse the whole tree and save the node->val to a string.
        If the node is NULL, we can save a character to represent it, sush as 'N', '#', etc..
        Then we use the same traverse method to read values from the string.
        Note, use stringstream to iteratively read the data in the string.
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
class Codec {
public:
    string preOrder(TreeNode* root){
        if(root==NULL){
            s += "N ";
            return s;
        }
        s += to_string(root->val) + " ";
        preOrder(root->left);
        preOrder(root->right);
        return s;
    }
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        // string res = "";
        // if(root==NULL){
        //     return "N";
        // }
        // stack<TreeNode*> s;
        // s.push(root);
        // TreeNode* cur;
        // while(s.size()!=0){
        //     cur = s.top(); s.pop();
        //     if(cur==NULL){
        //         res += "N ";
        //         continue;
        //     }else{
        //         res += to_string(cur->val) + " ";
        //         s.push(cur->right);
        //         s.push(cur->left);
        //     }
        // }
        string res = preOrder(root);
        return res;
    }
    
    // string serialize(TreeNode* root) {
    //     if(root == NULL) return "N";
    //     return to_string(root->val) + " " + serialize(root->left) + " "+ serialize(root->right);
    // }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        stringstream ss(data);
        return helper(ss);  
    }

private:
    string s;
    TreeNode* helper(stringstream& ss){
        string s;
        ss >> s;
        if(s == "N") return NULL;
        TreeNode* node = new TreeNode(stoi(s));
        node->left = helper(ss);
        node->right = helper(ss);
        return node;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));



/*
Method 2: Post-order traverse
          Note: the sequence of pre-order is C-L-R, and the sequence of post-order is L-R-C.
*/
class Codec {
public:
    string preOrder(TreeNode* root){
        if(root==NULL){
            s += "N ";
            return s;
        }
        preOrder(root->left);
        preOrder(root->right);
        s += to_string(root->val) + " ";
        return s;
    }
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string res = preOrder(root);
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        reverse(data.begin(), data.end());
        stringstream ss(data);
        return helper(ss);  
    }

private:
    string s;
    TreeNode* helper(stringstream& ss){
        string s;
        ss >> s;
        if(s == "N") return NULL;
        TreeNode* node = new TreeNode(stoi(s));
        node->right = helper(ss);
        node->left = helper(ss);
        return node;
    }
};
