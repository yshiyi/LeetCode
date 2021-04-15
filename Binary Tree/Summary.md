# Binary Tree
<!-- GFM-TOC -->
* [Leetcode Binary Tree](#Binary-Tree)
    * [1. Introduction to Binary Tree](#1-Introduction-to-Binary-Tree)
       * [1.1 Pre order Traversal](#11-Pre-Order-Traversal)
          * [144M. Binary Tree Preorder Traversal](#144M-Binary-Tree-Preorder-Traversal)
       * [1.2 In order Traversal](#12-In-Order-Traversal)
       * [1.3 Post order Traversal](#13-Post-Order-Traversal)
       * [1.4 Breadth First Search](#14-Breadth-First-Search)
    * [2. Recursive](#2-Recursive)
       * [67. Add Binary](#67-Add-Binary)
<!-- GFM-TOC -->

# 1. Introduction to Binary Tree
## 1.1 Pre Order Traversal
Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree. Here is an example:\
<pre>
          F
      B       G
    A   D       I
       C E     H
</pre>
**Preorder:F-B-A-D-C-E-G-I-H**\
**Note:**\
QuickSort is a kind of pre order traversal.\
To sort nums\[lo, ..., hi\] using quick sort, we first need to find a pivot value, and let nums\[lo, ..., p-1\] be less than p and nums\[p_1, ..., hi\] be greater than p by swap values.\ 
The frame of code is:
```
void sort(int[] nums, int lo, int hi) {
    /****** 前序遍历位置 ******/
    // 通过交换元素构建分界点 p
    int p = partition(nums, lo, hi);
    /************************/

    sort(nums, lo, p - 1);
    sort(nums, p + 1, hi);
}
```
### 144M. Binary Tree Preorder Traversal
**Description:**\
Given the root of a binary tree, return the preorder traversal of its nodes' values.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/144M.%20Binary%20Tree%20Preorder%20Traversal.cpp)
'''
// Method 1: Recursive
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        preorderRecur(ans, root);
        return ans;
    }
    void preorderRecur(vector<int>& ans, TreeNode* root){
        if(root==NULL){
            return;
        }
        ans.push_back(root->val);
        preorderRecur(ans, root->left);
        preorderRecur(ans, root->right);
    }
};

// Method 2: Iterative, use stack to save the root
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        stack<TreeNode*> st;
        while(true){
            while(root!=NULL){
                st.push(root);
                ans.push_back(root->val);
                root = root->left;
            }
            if(st.size()==0){
                break;
            }
            root = st.top();
            st.pop();
            root = root->right;
        }
        return ans;
    }
};
'''
[Python]

## 1.2 In Order Traversal
In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.\
<pre>
          F
      B       G
    A   D       I
       C E     H
</pre>
**Inorder:A-B-C-D-E-F-G-H-I**\
Typically, for binary search tree, we can retrieve all the data in sorted order using in-order traversal. 

## 1.3 Post Order Traversal
Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.\
<pre>
          F
      B       G
    A   D       I
       C E     H
</pre>
**Inorder:A-C-E-D-B-H-I-G-F**\
It is worth noting that when you delete nodes in a tree, deletion process will be in post-order. That is to say, when you delete a node, you will delete its left child and its right child before you delete the node itself.\
**Note:**\
Post-order is widely use in mathematical expression. It is easier to write a program to parse a post-order expression. Here is an example:
<pre>
          +
      *       5
    4   -       
       7 2     
</pre>
If you handle this tree in postorder, you can easily handle the expression using a stack. Each time when you meet a operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.\
MergeSort is a kind of post-order traversal.\
To sort nums\[lo, ..., hi\] using merge sort, we need to sort nums\[lo, ..., mid\] and nums\[mid+1, ..., hi\], and then merge these two sorted arrays.\
The frame of code is:
```
void sort(int[] nums, int lo, int hi) {
    int mid = (lo + hi) / 2;
    sort(nums, lo, mid);
    sort(nums, mid + 1, hi);

    /****** 后序遍历位置 ******/
    // 合并两个排好序的子数组
    merge(nums, lo, mid, hi);
    /************************/
}
```

## 1.4 Breadth First Search
Breadth-First Search is an algorithm to traverse or search in data structures like a tree or a graph. The algorithm starts with a root node and visit the node itself first. Then traverse its neighbors, traverse its second level neighbors, traverse its third level neighbors, so on and so forth.\
When we do breadth-first search in a tree, the order of the nodes we visited is in level order.\
Typically, we use a queue to help us to do BFS.\
Here is an example of level-order traversal:
<pre>
          F
      B       G
    A   D       I
       C E     H
</pre>
**Queue: F-B-G-A-D-I-C-E-H**\
**Ans: \[\[F\], \[B, G\], \[A, D, I\], \[C, E, H\]\]**




















