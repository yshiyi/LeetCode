# Binary Tree
<!-- GFM-TOC -->
* [Leetcode Binary Tree](#Binary-Tree)
    * [1. Introduction to Binary Tree](#1-Introduction-to-Binary-Tree)
       * [1.1 Preorder Traversal](#11-Preorder-Traversal)
          * [144M. Binary Tree Preorder Traversal](#144M-Binary-Tree-Preorder-Traversal)
       * [1.2 Inorder Traversal](#12-Inorder-Traversal)
          * [94M. Binary Tree Inorder Traversal](#94M-Binary-Tree-Inorder-Traversal)
       * [1.3 Postorder Traversal](#13-Postorder-Traversal)
          * [145M. Binary Tree Postorder Traversal](#145M-Binary-Tree-Postorder-Traversal)
       * [1.4 Breadth First Search](#14-Breadth-First-Search)
          * [102M. Binary Tree Level Order Traversal](#102M-Binary-Tree-Level-Order-Traversal)
          * [637. Average of Levels in Binary Tree](#637-Average-of-Levels-in-Binary-Tree)
    * [2. Recursive](#2-Recursive)
       * [67. Add Binary](#67-Add-Binary)
<!-- GFM-TOC -->

# 1. Introduction to Binary Tree
## 1.1 Preorder Traversal
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
```
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

// Method 3: Iterative approach
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        stack<TreeNode*> st;
        st.push(root);
        while(st.size()!=0){
            root = st.top();
            st.pop();
            ans.push_back(root->val);
            if(root->right!=NULL){
                st.push(root->right);
            }
            if(root->left!=NULL){
                st.push(root->left);
            }
        }
        return ans;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/144M.%20Binary%20Tree%20Preorder%20Traversal.py)
```
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        st = collections.deque()
        while True:
            while root!=None:
                ans.append(root.val)
                st.append(root)
                root = root.left
            if len(st)==0:
                break
            root = st[-1]
            st.pop()
            root = root.right
        
        return ans
```

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
### 94M. Binary Tree Inorder Traversal
**Description:**\
Given the root of a binary tree, return the inorder traversal of its nodes' values.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/94M.%20Binary%20Tree%20Inorder%20Traversal.cpp)
```
// Method 1: Recursive approach
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (root==NULL){
            return ans;
        }
        inorderRecur(ans, root);
        return ans;
    }
    void inorderRecur(vector<int> &ans, TreeNode* root){
        if(root==NULL){
            return;
        }
        inorderRecur(ans, root->left);
        ans.push_back(root->val);
        inorderRecur(ans, root->right);
    }
};

// Method 2: Iterative approach
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        stack<TreeNode*> st;
        while(root!=NULL || st.size()!=0){
            while(root!=NULL){
                st.push(root);
                root = root->left;
            }
            root = st.top();
            ans.push_back(root->val);
            st.pop();
            root = root->right;
        }
        return ans;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/94M.%20Binary%20Tree%20Inorder%20Traversal.py)
```
# Method 1: Recursive approach
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        if root==None:
            return self.ans
        self.inorderRecur(root)
        return self.ans
        
    def inorderRecur(self, root):
        if root==None:
            return
        self.inorderRecur(root.left)
        self.ans.append(root.val)
        self.inorderRecur(root.right)
 
# Method 2: Iterative approach
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root==None:
            return ans
        st = collections.deque()
        while root!=None or len(st)!=0:
            while root!=None:
                st.append(root)
                root = root.left
            root = st[-1]
            st.pop()
            ans.append(root.val)
            root = root.right
        return ans
```


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
### 145M. Binary Tree Postorder Traversal
**Description:**\
Given the root of a binary tree, return the postorder traversal of its nodes' values.\
**Method:**\
Notice: The order of preorder traversal is center - left - right, the the order of postorder traversal is left - right - center. The reverse order is center - left - right.\
Hence, we only need to modify the order of the stack in the while-loop and return the reverse order of ans.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/145M.%20Binary%20Tree%20Postorder%20Traversal.cpp)
```
// Method 1: Recursive approach
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        
        postorderRecur(ans, root);
        return ans;
    }
    void postorderRecur(vector<int> &ans, TreeNode* root){
        if (root==NULL){
            return;
        }
        postorderRecur(ans, root->left);
        postorderRecur(ans, root->right);
        ans.push_back(root->val);
    }
};

// Method 2: Iterative approach
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL){
            return ans;
        }
        stack<TreeNode*> st;
        st.push(root);
        while(st.size()!=0){
            root = st.top();
            st.pop();
            ans.push_back(root->val);
            if(root->left!=NULL){
                st.push(root->left);
            }
            if(root->right!=NULL){
                st.push(root->right);
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/145M.%20Binary%20Tree%20Postorder%20Traversal.py)
```
# Method 1: Recursive approach
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        if root==None:
            return self.ans
        self.postorderRecur(root)
        return self.ans
        
    def postorderRecur(self, root):
        if root==None:
            return
        self.postorderRecur(root.left)
        self.postorderRecur(root.right)
        self.ans.append(root.val)

# Method 2: Iterative approach
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root==None:
            return ans
        st = collections.deque()
        st.append(root)
        while len(st)!=0:
            root = st[-1]
            st.pop()
            ans.append(root.val)
            if root.left!=None:
                st.append(root.left)
            if root.right!=None:
                st.append(root.right)
        
        return ans[::-1]
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

### 102M. Binary Tree Level Order Traversal
**Description:**\
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).\
**Method:**\
1. Using queue (First-In-First-Out). 
2. On each level, we push each node's value to a vector and save their leaves to the queue (from left to right). 
3. After pushing the node to the vector, we need to pop it from the queue.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/102M.%20Binary%20Tree%20Level%20Order%20Traversal.cpp)
```
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(root==NULL){
            return ans;
        }
        queue<TreeNode*> qt;
        qt.push(root);
        while(qt.size()!=0){
            int n = qt.size();
            vector<int> v;
            while(n){
                root = qt.front();
                qt.pop();
                v.push_back(root->val);
                if(root->left){qt.push(root->left);}
                if(root->right){qt.push(root->right);}
                n--;
            }
            ans.push_back(v);
        }
        return ans;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/102M.%20Binary%20Tree%20Level%20Order%20Traversal.py)
```
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root is None:
            return ans
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n = len(q)
            l = []
            while n!=0:
                root = q[0]
                q.popleft()
                l.append(root.val)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
                n -= 1
            ans.append(l)
        return ans
```

### 637. Average of Levels in Binary Tree
**Description:**\
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.\
**Method:**\
Similar with 102M. Using queue.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/637.%20Average%20of%20Levels%20in%20Binary%20Tree.cpp)
```
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> ans;
        if(!root){
            return ans;
        }
        queue<TreeNode*> qt;
        qt.push(root);
        while(qt.size()){
            double n1 = qt.size(), n2 = n1;
            double sum=0.0;
            while(n1){
                root = qt.front();
                qt.pop();
                sum += (double)root->val;
                if(root->left){qt.push(root->left);}
                if(root->right){qt.push(root->right);}
                n1--;
            }
            ans.push_back(sum/n2);
        }
        return ans;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/637.%20Average%20of%20Levels%20in%20Binary%20Tree.py)
```
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        if root is None:
            return ans
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n1 = n2 = len(q)
            sum = 0.0
            while n1!=0:
                root = q[0]
                q.popleft()
                sum += root.val
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
                n1 -= 1
            ans.append(sum/n2)
        return ans
```

















