/*
116M. Populating Next Right Pointers in Each Node
Tree, Depth-first Search, Breadth-first Search

Description:
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

       1
  2        3
4   5    6   7

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), 
             your function should populate each next pointer to point to its next right node, just like in Figure B. 
             The serialized output is in level order as connected by the next pointers, 
             with '#' signifying the end of each level.

Similar Questions:
Populating Next Right Pointers in Each Node II - Medium
Binary Tree Right Side View - Medium
*/

/*
Method 1: Recursive approach
          One recursive function is not enough to solve the problem, 
          because we can't connect one node's right to another node's left.
          Hence, we define another seperate recursive function to connect two different nodes.
*/
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if(root==NULL){
            return NULL;
        }
        connectTwoNode(root->left, root->right);
        return root;
    }
    void connectTwoNode(Node* node1, Node* node2){
        if(node2==NULL){
        // if(node1==NULL || node2==NULL){
            return;
        }
        node1->next = node2;
        connectTwoNode(node1->left, node1->right);
        connectTwoNode(node2->left, node2->right);
        connectTwoNode(node1->right, node2->left);
    }
};


/* 
Method 2: Iterative Approach
          Using stack, the idea is similar with that of the Breadth-first search approach
          Connect q.front() to its next node
*/
class Solution {
public:
    Node* connect(Node* root) {
        if(root==NULL){
            return NULL;
        }
        queue<Node*> q;
        Node* cur = root;
        q.push(cur);
        while(q.size()!=0){
            int n = q.size();
            while(n!=0){
                cur = q.front();
                q.pop();
                if(n!=1){
                    cur->next = q.front();
                }else{
                    cur->next = NULL;
                }
                if(cur->left!=NULL){q.push(cur->left);}
                if(cur->right!=NULL){q.push(cur->right);}
                n--;
            }
        }
        return root;
    }
};

