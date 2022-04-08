# Binary Tree
<!-- GFM-TOC -->
* [Leetcode Binary Tree](#Binary-Tree)
    * [1. Introduction to Binary Tree](#1-Introduction-to-Binary-Tree)
       * [1.1 Preorder Traversal](#11-Preorder-Traversal)
          * [144M. Binary Tree Preorder Traversal](#144M-Binary-Tree-Preorder-Traversal)
          * [226. Invert Binary Tree](#226-Invert-Binary-Tree)
          * [116M. Populating Next Right Pointers in Each Node](#116M-Populating-Next-Right-Pointers-in-Each-Node)
          * [117M. Populating Next Right Pointers in Each Node II](#117M-Populating-Next-Right-Pointers-in-Each-Node-II)
          * [654M. Maximum Binary Tree](#654M-Maximum-Binary-Tree)
          * [101. Symmetric Tree](#101-Symmetric-Tree)
          * [112. Path Sum](#112-Path-Sum)
       * [1.2 Inorder Traversal](#12-Inorder-Traversal)
          * [94M. Binary Tree Inorder Traversal](#94M-Binary-Tree-Inorder-Traversal)
       * [1.3 Postorder Traversal](#13-Postorder-Traversal)
          * [145M. Binary Tree Postorder Traversal](#145M-Binary-Tree-Postorder-Traversal)
          * [114M. Flatten Binary Tree to Linked List](#114M-Flatten-Binary-Tree-to-Linked-List)
          * [652M. Find Duplicate Subtrees](#652M-Find-Duplicate-Subtrees)
          * [104. Maximum Depth of Binary Tree](#104-Maximum-Depth-of-Binary-Tree)
       * [1.4 Breadth First Search](#14-Breadth-First-Search)
          * [102M. Binary Tree Level Order Traversal](#102M-Binary-Tree-Level-Order-Traversal)
          * [637. Average of Levels in Binary Tree](#637-Average-of-Levels-in-Binary-Tree)
          * [116M. Populating Next Right Pointers in Each Node](#116M-Populating-Next-Right-Pointers-in-Each-Node)
          * [117M. Populating Next Right Pointers in Each Node II](#117M-Populating-Next-Right-Pointers-in-Each-Node-II)
          * [297H. Serialize and Deserialize Binary Tree](#297H-Serialize-and-Deserialize-Binary-Tree)
          * [341M. Flatten Nested List Iterator](#341M-Flatten-Nested-List-Iterator)
          * [236M. Lowest Common Ancestor of a Binary Tree](#236M-Lowest-Common-Ancestor-of-a-Binary-Tree)
          * [222M. Count Complete Tree Nodes](#222M-Count-Complete-Tree-Nodes)
          * [101. Symmetric Tree](#101-Symmetric-Tree)
          * [104. Maximum Depth of Binary Tree](#104-Maximum-Depth-of-Binary-Tree)
          * [112. Path Sum](#112-Path-Sum)
       * [1.5 Depth First Search](#15-Depth-First-Search)
          * [114M. Flatten Binary Tree to Linked List](#114M-Flatten-Binary-Tree-to-Linked-List)
          * [797M. All Paths From Source to Target](#797M-All-Paths-From-Source-to-Target)
       * [1.6 Construct a Binary Tree](#16-Construct-a-Binary-Tree)
          * [105M. Construct Binary Tree from Preorder and Inorder Traversal](#105M-Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal)
          * [106M. Construct Binary Tree from Inorder and Postorder Traversal](#106M-Construct-Binary-Tree-from-Inorder-and-Postorder-Traversal)
<!-- GFM-TOC -->

# 1. Introduction to Binary Tree
Definition for a binary tree node/
```
struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode() : val(0), left(nullptr), right(nullptr) {}
   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
   TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
```

The frame of traversing a binary tree is:
```
/* 二叉树遍历框架 */
void traverse(TreeNode root) {
    // Preorder
    traverse(root.left)
    // Inorder
    traverse(root.right)
    // Postorder
}
```

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

### 226. Invert Binary Tree
**Description:**\
Given the root of a binary tree, invert the tree, and return its root.\
**Method:**\
This is a question to practice recursive approach to solve tree problems\
Note: the swap function can be operated at pre-order or post-order, but can't be done in-order.\
      Pre-order: Swap left and right first, and then go to left and right sequentially\
      Post-order: Invert left and right first, then swap left and right\

[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/226.%20Invert%20Binary%20Tree.cpp)
```
// Method 1: Recursive approach
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL){
            return NULL;
        }
        
        swap(root->right, root->left);
        // root->right = invertTree(root->right);
        invertTree(root->left);
        
        // root->left = invertTree(root->left);
        invertTree(root->right);
        
        return root;
    }
};

// Method 2: Iterative approach
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root==NULL){
            return NULL;
        }
        
        queue<TreeNode*> q;
        q.push(root);
        while(q.size()!=0){
            TreeNode* cur = q.front();
            q.pop();
            swap(cur->left, cur->right);
            if(cur->left!=NULL){q.push(cur->left);}
            if(cur->right!=NULL){q.push(cur->right);}
        }
        return root;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/226.%20Invert%20Binary%20Tree.py)
```
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```

### 116M. Populating Next Right Pointers in Each Node
**Description:**\
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.\ 
Populate each next pointer to point to its next right node. \
If there is no next right node, the next pointer should be set to NULL.\
Initially, all next pointers are set to NULL.\
**Method:**\
One recursive function is not enough to solve the problem, because we can't connect one node's right to another node's left.\
Hence, we define another seperate recursive function to connect two different nodes.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/116M.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node.cpp)
```
// Method 1: Recursive approach
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
          Using queue, the idea is similar with that of the Breadth-first search approach
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
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/116M.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node.py)
```
# Method 1: Recursive Approach
class Solution(object):
    def connect(self, root):
        if root is None:
            return None
        self.connectTwoNode(root.left, root.right)
        return root
    
    def connectTwoNode(self, node1, node2):
        if node2 is None:
            return
        node1.next = node2
        self.connectTwoNode(node1.left, node1.right)
        self.connectTwoNode(node2.left, node2.right)
        self.connectTwoNode(node1.right, node2.left)

# Method 2: Iterative approach
class Solution(object):
    def connect(self, root):
        if root is None:
            return None
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n = len(q)
            while n!=0:
                cur = q[0]
                q.popleft()
                if n!=1:
                    cur.next = q[0]
                else:
                    cur.next = None
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
                n -= 1
        return root
```

### 117M. Populating Next Right Pointers in Each Node II
**Description:**\
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.\
Initially, all next pointers are set to NULL.\
**Method:**\
For iterative approach, we can use the same method as the one for 116M.\
For recursive approach, since this is not a perfect binary tree, we need a seperate function to find the next node.\
Note: we need to connect the nodes from right to left.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/117M.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II.cpp)
```
// Method 1: Iterative approach
// Same as 116M
 
// Method 2: Recursive approach
class Solution {
public:
    Node* connect(Node* root) {
        if(root==NULL){
            return NULL;
        }
        if(root->left!=NULL){
            if(root->right!=NULL){
                root->left->next = root->right;
            }else{
                root->left->next = findNext(root->next);
            }
        }
        if(root->right!=NULL){
            root->right->next = findNext(root->next);
        }
        connect(root->right);
        connect(root->left);
        return root;
    }
    Node* findNext(Node* node){
        if(node==NULL){return NULL;}
        else if(node->left!=NULL){return node->left;}
        else if(node->right!=NULL){return node->right;}
        else{return findNext(node->next);}
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/117M.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II.py)
```
# Method: Iterative approach
class Solution(object):
    def connect(self, root):
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        while len(q):
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i==size-1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root

# Method: Recursive approach
class Solution(object):
    def connect(self, root):
        def findNext(node):
            if node is None:
                return None
            if node.left:
                return node.left
            if node.right:
                return node.right
            return findNext(node.next)

        def helper(root):
            if root is None:
                return
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = findNext(root.next)
            if root.right:
                root.right.next = findNext(root.next)
            helper(root.right)
            helper(root.left)
        helper(root)
        return root
```

### 654M. Maximum Binary Tree
**Description:**\
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:\
Create a root node whose value is the maximum value in nums.\
Recursively build the left subtree on the subarray prefix to the left of the maximum value.\
Recursively build the right subtree on the subarray suffix to the right of the maximum value.\
Return the maximum binary tree built from nums.\
**Method:**\
For recursive approach, find the max element, and create a new node using this max. Then work on the left and the right subarray recursively. The terminate condition is when lo > hi. To find the max element, we need to loop from i=lo to i=hi.\
For iterative approach, we can use a stack to keep some nodes and ensure a decreasing order. For each number, we keep pop the stack until empty or a bigger number. The bigger number is current number's root.\
Time Complexity: O(n^2), we call helper n times and at each time we traverse over all elements. The worst case is O(n^2). But in average, there is logN levels, so the time complexity is O(NlogN).\
Time Complexity: O(N), if we use iterative approach with stack.\
Space complexity: O(n), in the worst case. In average, O(logN)\


[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/654M.%20Maximum%20Binary%20Tree.cpp)
```
// Method 1: Recursive approach
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

// Method 2: Iterative approach
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
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/654M.%20Maximum%20Binary%20Tree.py)
```
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        return self.buildTree(nums, 0, len(nums)-1)
    
    def buildTree(self, nums, lo, hi):
        if lo > hi:
            return None
        maxVal = float('-inf')
        for i in range(lo, hi+1):
            if nums[i] > maxVal:
                maxVal = nums[i]
                index = i
        root = TreeNode(maxVal)
        root.left = self.buildTree(nums, lo, index-1)
        root.right = self.buildTree(nums, index+1, hi)
        return root
```

###  101. Symmetric Tree
**Description:**\
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).\
**Method:**\
*Recursive approach*\
Similar to 116M. Populating Next Right Pointers in Each Node We send two nodes to the recursive function in every iteration.\
*Iterative approach*\
Using queue. Take the first two elements from the queue in each iteration. The sequence of the nodes is important.\
Time Complexity: O(N), we have to traverse all the nodes.\
Space complexity: O(N)\
Space 
Space complexity: 
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/101.%20Symmetric%20Tree.cpp)
```
// Method 1: Recursive approach
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

// Method 2: Iterative approach
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
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/101.%20Symmetric%20Tree.py)
```
class Solution(object):
    def isSymmetric(self, root):
        return self.checkSymmetric(root.left, root.right)
    
    def checkSymmetric(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.checkSymmetric(node1.left, node2.right) and self.checkSymmetric(node1.right, node2.left)

```

### 112. Path Sum
**Description:**\
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum. A leaf is a node with no children.\
**Method:**\
*Recursive approach*\
Pre-order traverse. Check if the currrent sum is equal to the target sum and if both the left node and the right node are null. If so, then return true. Otherwise, call recursion function for left subtree and right subtree.\
*Iterative approach*\
Breadth-first Search. Save the current node and the current sum to a queue while traversing. When both the left and right node are null, save the current sum to a vector. Finally, check if the target sum is in the vector.\
Time complexity: O(N), traverse all the nodes.\
Space complexity: O(N)\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/112.%20Path%20Sum.cpp)
```
// Method 1: Recursive approach
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

// Method 2: Iterative approach
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
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/112.%20Path%20Sum.py)
```
# Method 1: Recursive approach, define sum as a general variable
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        Sum = 0
        return self.helper(root, targetSum, Sum)
        
    def helper(self, root, targetSum, Sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if Sum+root.val==targetSum:
                return True
            else:
                return False
        Sum += root.val
        return self.helper(root.left, targetSum, Sum) or self.helper(root.right, targetSum, Sum)


# Method 2: Iterative approach, Breadth-first Search
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        q = collections.deque()
        q.append((root, 0))
        while len(q):
            node, curSum = q.popleft()
            curSum += node.val
            if node.left is None and node.right is None:
                if curSum == targetSum:
                    return True
            if node.left:
                q.append((node.left, curSum))
            if node.right:
                q.append((node.right, curSum))
        return False
```



## 1.2 Inorder Traversal
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


## 1.3 Postorder Traversal
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

### 114M. Flatten Binary Tree to Linked List
**Description:**\
Given the root of a binary tree, flatten the tree into a "linked list":\
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.\
The "linked list" should be in the same order as a pre-order traversal of the binary tree.\
**Method:**\
For recursive approach, we first need to consider what to do for the current node.\
1. Flat the left subtree and the right subtree sequentially.
2. Connect the flatted left subtree to node->right, and connect the flatted right subtree to the end of flatted left subtree.

For iterative approach, we can use stack or preorder traverse method to traverse the tree. Meanwhile, create a new tree to connect each visited node.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/114M.%20Flatten%20Binary%20Tree%20to%20Linked%20List.cpp)
```
// Method 1: Recursive approach
class Solution {
public:
    void flatten(TreeNode* root) {
        if(root==NULL){
            return;
        }
        // Flatten the left tree and the right tree sequentially
        flatten(root->left);
        flatten(root->right);
        
        // Save the flat subtress to temps
        TreeNode* tempLeft = root->left;
        TreeNode* tempRight = root->right;
        // Set the left of root to NULL
        root->left = NULL;
        // Connect the flat left tree to the right of root
        root->right = tempLeft;
        
        // Define a temp node and move it the end of the right tree
        TreeNode* cur = root;
        while(cur->right!=NULL){
            cur = cur->right;
        }
        // Connect the flat right tree to the end of right subtree
        cur->right = tempRight;
    }
};

// Method 2: Iterative approach
class Solution {
public:
    void flatten(TreeNode* root) {
        if(root==NULL){
            return;
        }
        stack<TreeNode*> s;
        s.push(root);
        TreeNode* ref = root;
        while(s.size()!=0){
            TreeNode* cur = s.top();
            s.pop();
            if(cur->right!=NULL){s.push(cur->right);}
            if(cur->left!=NULL){
                s.push(cur->left);
                cur->left = NULL;
            }
            
            // Connect the current node to the right of the previous node
            if(cur!=ref){
                ref->right = cur;
                ref = ref->right;
            }
        }
        return;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/114M.%20Flatten%20Binary%20Tree%20to%20Linked%20List.py)
```
# Method 1: Iterative approach
class Solution(object):
    def flatten(self, root):
        if root is None:
            return None
        s = collections.deque()
        s.append(root)
        ref = root
        while len(s)!=0:
            cur = s[-1]
            s.pop()
            if cur.right is not None:
                s.append(cur.right)
            if cur.left is not None:
                s.append(cur.left)
                cur.left = None
            if ref!=cur:
                ref.right = cur
                ref = cur
        return root

# Method 2: Recursive approach
class Solution(object):
    def flatten(self, root):
        if root is None:
            return root
        leftTree = self.flatten(root.left)
        rightTree = self.flatten(root.right)
        root.right = leftTree
        root.left = None
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = rightTree
        return root
```

### 652M. Find Duplicate Subtrees
**Description:**|
Given the root of a binary tree, return all duplicate subtrees.\
For each kind of duplicate subtrees, you only need to return the root node of any one of them.\
Two trees are duplicate if they have the same structure with the same node values.\
**Method:**\
Recursive approach, consider what needs to be done for the current node:
1. What the left and right subtree looks like?
2. Does the format of the current node appears before?

As to the first one, we need to use the post-order traverse method. \
As to the second one, we need to create an unordered_map to save the subtrees as to_string(root->val) + ',' + Recur(root->left) + ',' + Recur(root->right).\
Keep in mind that don't save duplicate results when one appears more than two times.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/652M.%20Find%20Duplicate%20Subtrees.cpp)
```
class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        find(root);
        return res;
    }
    string find(TreeNode* root){
        if(root==NULL){
            return " ";
        }
        string left = find(root->left);
        string right = find(root->right);
        string s = to_string(root->val) + ',' + left + ',' + right;
        m[s]++;
        if(m[s]==2){
            res.push_back(root);
        }
        return s;
    }
private:
    unordered_map<string, int> m;
    vector<TreeNode*> res;    
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/652M.%20Find%20Duplicate%20Subtrees.py)
```
class Solution(object):
    def findDuplicateSubtrees(self, root):
        result = []
        seen = collections.defaultdict(int)
        def collect(root):
            if not root:
                return '#'
            l = str(root.val) + " " + collect(root.left) + " " + collect(root.right)
            seen[l] = seen.get(l, 0) + 1
            if seen[l] == 2:
                result.append(root)
            return l
        collect(root)
        return result
        
        count = collections.Counter()
        ans = []
        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans
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

### 297H. Serialize and Deserialize Binary Tree
**Description:**\
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.\
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.\
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.\
**Method:**\
*Breadth-first Search*\
Using queue to traverse the tree. Much faster than recursion.\
*Recursive approach*\
We can use pre-order method to traverse the whole tree and save the node->val to a string. If the node is NULL, we can save a character to represent it, sush as 'N', '#', etc..\
Then we use the same traverse method to read values from the string. Note, use stringstream to iteratively read the data in the string.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/297H.%20Serialize%20and%20Deserialize%20Binary%20Tree.cpp)
```
// Breadth-first Search
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string res = "";
        if(root==NULL){
            res = "# ";
            return res;
        }
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* cur;
        while(q.size()!=0){
            cur = q.front(); q.pop();
            if(cur==NULL){
                res += "# ";
            }else{
                res += to_string(cur->val) + " ";
                q.push(cur->left);
                q.push(cur->right);
            }
        }
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if(data[0]=='#'){
            return NULL;
        }
        cout << data << endl;
        stringstream ss(data);
        string s;
        ss >> s;
        TreeNode* root = new TreeNode(stoi(s));
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* cur;
        while(ss >> s){
            cur = q.front(); q.pop();
            if(s=="#"){
                cur->left = NULL;
            }else{
                cur->left = new TreeNode(stoi(s));
                q.push(cur->left);
            }
            ss >> s;
            if(s=="#"){
                cur->right = NULL;
            }else{
                cur->right = new TreeNode(stoi(s));
                q.push(cur->right);
            }
        }
        return root;  
    }
};

// Recursive approach
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
        string res = preOrder(root);
        return res;
    }

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
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/297H.%20Serialize%20and%20Deserialize%20Binary%20Tree.py)
```
class Codec:
    ans = []
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        self.help1(root, ans)
        return ans
    
    def help1(self, root, ans):
        if root is None:
            ans.append('#')
            return 
        ans.append(root.val)
        self.help1(root.left, ans)
        self.help1(root.right, ans)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        d = collections.deque(data)
        return self.helper2(d)
    
    def helper2(self, d):
        i = d[0]
        d.popleft()
        if i is None:
            return None
        if i=='#':
            return None
        node = TreeNode(str(i))
        node.left = self.helper2(d)
        node.right = self.helper2(d)
        return node
```

### 341M. Flatten Nested List Iterator
**Description:**\
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.\
**Method:**\ 
Recursive approach\
For each element in the nested list, it could be either an integer or another nested list.
1. If the current element is an integer, we save it to a queue.
2. If the current element is a nested list, we call the recursive function.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/341M.%20Flatten%20Nested%20List%20Iterator.cpp)
```
class NestedIterator {
public:
    queue<int> q;
    
    void flatten(vector<NestedInteger> &A){
        for (auto x: A){
            if (x.isInteger()){
                q.push(x.getInteger());
            }
            else{
                flatten(x.getList());
            }
        }
    }
    
    NestedIterator(vector<NestedInteger> &A) {
        flatten(A);
    }
    
    int next() {
        int n = q.front(); q.pop();
        return n;
    }
    
    bool hasNext() {
        return q.size() > 0;
    }
};

```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/341M.%20Flatten%20Nested%20List%20Iterator.py)
```
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.v = []
        self.flatten(nestedList)
        print(self.v)
    
    def flatten(self, nestedList):
        
        for node in nestedList:
            if node.isInteger():
                self.v.append(node.getInteger())
            else:
                self.flatten(node.getList())
        

    def next(self):
        """
        :rtype: int
        """
        return self.v.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.v)
```

### 236M. Lowest Common Ancestor of a Binary Tree
**Description:**\
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”\
**Method:**\
*Iterative approach*\
Use a map to save the current node and its parent. We traverse the tree and save all the nodes and their corresponding parents to the map.\
Then, we create a set and save all the ancestors of p to the set. Finally, we check the ancestors of q and find the one that appears in the p's set.\
*Recursive approach*\
When apply recursive approach, we only need to consider what we need to do for a single node.
1. We need to check if the root is p or q. If so, root is the LCA.
2. We inquire the left subtree recursion and the right subtree recursion.
3. If both of them are not NULL, in other words, they are either p or q, then the root is LCA.
4. The subtree that returns non-NULL value is the root. In other words, the other target root is in the subtree of this root.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/236M.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree.cpp)
```
// Method 1: Iterative approach
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==NULL){
            return NULL;
        }
        unordered_map<TreeNode*, TreeNode*> m;
        m.insert({root, NULL});
        stack<TreeNode*> s;
        s.push(root);
        TreeNode* cur;
        while(s.size()!=0){
            cur = s.top(); s.pop();
            if(cur->right!=NULL){
                s.push(cur->right);
                m.insert({cur->right, cur});
            }
            if(cur->left!=NULL){
                s.push(cur->left);
                m.insert({cur->left, cur});
            }
        }
        set<TreeNode*> s_anc;
        while(m[p]!=NULL){
            s_anc.insert(p);
            p = m[p];
        }
        while(m[q]!=NULL){
            if(s_anc.find(q)!=s_anc.end()){
                break;
            }
            q = m[q];
        }
        return q;
    }
};

// Method 2: Recursive approach
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==NULL)
            return NULL;
        if(root==p || root==q)
            return root;
        TreeNode* left=lowestCommonAncestor(root->left,p,q);
        TreeNode* right=lowestCommonAncestor(root->right,p,q);
        if(left!=NULL && right!=NULL)
            return root;
        else
        {
            if(left!=NULL)
                return left;
            return right;
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/236M.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree.py)
```
# Method 1: Recursive approach
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root==p or root==q:
            return root
        leftRoot = self.lowestCommonAncestor(root.left, p, q)
        rightRoot = self.lowestCommonAncestor(root.right, p, q)
        if leftRoot is not None and rightRoot is not None:
            return root
        if leftRoot is not None:
            return leftRoot
        if rightRoot is not None:
            return rightRoot


# Method 2: Iterative approach
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        m = {}
        m[root] = None
        s = collections.deque()
        s.append(root)
        while len(s)!=0:
            cur = s[-1]
            s.pop()
            if cur.right is not None:
                s.append(cur.right)
                m[cur.right] = cur
            if cur.left is not None:
                s.append(cur.left)
                m[cur.left] = cur
        
        s_ans = set()
        while m[p] is not None:
            s_ans.add(p)
            p = m[p]
        while m[q] is not None:
            if q in s_ans:
                break
            q = m[q]
        return q
```

### 222M. Count Complete Tree Nodes
**Description:**\
Given the root of a complete binary tree, return the number of the nodes in the tree.\
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.\
**Method:**\
*Breadth-first Search*\
Traverse the tree, the time complexity is O(N).\
*Recursive approach*\
Time complexity is O(log(N)\*log(N)).\
Check the level of the left subtree and that of the right subtree. If they are same, then the total number of nodes is  2^level - 1. If they are not same, then call the recursion function for left subtree and right subtree separately.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/222M.%20Count%20Complete%20Tree%20Nodes.cpp)
```
// Method 1: Traverse the tree using Breadth-first Search
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(root==NULL){
            return 0;
        }
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* cur;
        int res = 0;
        while(q.size()!=0){
            cur = q.front(); q.pop();
            res++;
            if(cur->left!=NULL){
                q.push(cur->left);
            }
            if(cur->right!=NULL){
                q.push(cur->right);
            }
        }
        return res;
    }
};

// Method 2: Recursive approach
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == NULL) return 0;
        TreeNode *leftTree = root, *rightTree = root;
        int hl = 0, hr = 0;
        while(leftTree!=NULL){
            leftTree = leftTree->left;
            hl++;
        }
        while(rightTree!=NULL){
            rightTree = rightTree->right;
            hr++;
        }
        if(hl==hr){
            return pow(2, hl) - 1;
        }
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/222M.%20Count%20Complete%20Tree%20Nodes.py)
```
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftTree, rightTree = root, root
        hl, hr = 0, 0
        while leftTree is not None:
            leftTree = leftTree.left
            hl += 1
        while rightTree is not None:
            rightTree = rightTree.right
            hr += 1
        if hl == hr:
            return 2 ** hl - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

### 104. Maximum Depth of Binary Tree
**Description:**\
Given the root of a binary tree, return its maximum depth.\
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.\
**Method:**\
*Iterative approach*\
Using queue (similar to 102M. Binary Tree Level Order Traversal).\
*Recursive approach*\
Using post-order traverse. Obtain the max depth of left subtree and that of the right subtree. Return max of those two depths plus one.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/104.%20Maximum%20Depth%20of%20Binary%20Tree.cpp)
```
// Method 1: Iterative approach
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root==NULL){
            return NULL;
        }
        queue<TreeNode*> q;
        q.push(root);
        int res = 0;
        while(q.size()!=0){
            int n = q.size();
            while(n!=0){
                root = q.front();
                q.pop();
                if(root->right!=NULL){q.push(root->right);}
                if(root->left!=NULL){q.push(root->left);}
                n--;
            }
            res++;
        }
        return res;
    }
};

// Method 2: Recursive approach
class Solution {
public:
    int maxDepth(TreeNode* root) {
        int res = 1;
        if(root==NULL){
            return 0;
        }
        res = res + max(maxDepth(root->left), maxDepth(root->right));
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/104.%20Maximum%20Depth%20of%20Binary%20Tree.py)
```
# Method 1: Recursive approach
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        res = 1
        res = res + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return res


# Method 2: using collections.deque()
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        res = 0
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n = len(q)
            while n!=0:
                root = q[0]
                q.popleft()
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
                n -= 1
            res += 1
        return res

```




## 1.5 Depth First Search
Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.\
Pre-order traverse, in-order traverse and post-order traverse are all belonged to Depth-first Search.

### 797M. All Paths From Source to Target
**Description:**\
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.\
The graph is given as follows: graph\[i\] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph\[i\]\[j\]).\
**Method:**\
*Recursive approach, Depth-first Search*\
Consider what we need to do for the current single node:
1. Push the current node/val to a path which saves all the nodes along the way to the terminal node.
2. Check if the current node/val is equal to the terminal one. If so, save the path to a vector and pop the last element in the path.
3. Call the recursion function for all the values in the current node.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Graph/797M.%20All%20Paths%20From%20Source%20to%20Target.cpp)
```
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> path;
        traverse(graph, 0, path);
        return res;
    }
    void traverse(vector<vector<int>> graph, int s, vector<int> path){
        // enter the node and save it to the path
        path.push_back(s);
        
        int n = graph.size();
        if(s==n-1){
            res.push_back(path);
            path.pop_back();
            return;
        }
        for(auto val:graph[s]){
            traverse(graph, val, path);
        }
        
        // Leave the node and remove it from the path
        path.pop_back();
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Graph/797M.%20All%20Paths%20From%20Source%20to%20Target.py)
```
# Note: We must use deepcopy(path) to save it to self.res. Otherwise, the elements in self.res will be changed in accordance with the changes of path.

class Solution(object):
    def allPathsSourceTarget(self, graph):
        self.res = []
        path = []
        self.traverse(graph, 0, path)
        return self.res
    
    def traverse(self, graph, s, path):
        path.append(s)
        if s==(len(graph)-1):
            self.res.append(deepcopy(path))
            path.pop()
            return
        for node in graph[s]:
            self.traverse(graph, node, path)
        path.pop()
```


## 1.6 Construct a Binary Tree
### 105M. Construct Binary Tree from Preorder and Inorder Traversal
**Description:**\
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.\
**Method:**\
The structure of preorder is C - L - R, and the structure of inorder is L - C - R.\
We can use preorder to determine the root value, and use inorder to determine the subtrees.\
We need to figure out what we need to do for the root.
1. Determine the root. It is the first value in preorder.
2. Determine the left array and the right array for the left side of and the right side of the tree, respectively.
3. We can do this by using inorder array. We first find the root in the inorder, and then split the array into two subtrees.
4. The subtrees in preorder can be determined using the length of them.
5. The termination condition is preStart(prelo) > preEnd(prehi).
6. Carefully define the start and the end positions.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/105M.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal.cpp)
```
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
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/105M.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal.py)
```
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd:
           return None
        rootVal = preorder[preStart]
        for i in range(inStart, inEnd+1):
            if inorder[i]==rootVal:
                index = i
                break
        root = TreeNode(rootVal)
        length_left = index - inStart
        root.left = self.build(preorder, preStart+1, preStart+length_left, inorder, inStart, index-1)
        root.right = self.build(preorder, preStart+length_left+1, preEnd, inorder, index+1, inEnd)
        return root

```

### 106M. Construct Binary Tree from Inorder and Postorder Traversal
**Desciption:**\
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.\
**Method:**\
The idea is similar to 105M.\
The structure of inorder is L - C - R, the structure of postorder is L - R - C.\
We can use postorder array to determine the root value, and use inorder array to determine the subtrees.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/106M.%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal.cpp)
```
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
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/106M.%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal.py)
```
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        
    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd:
            return None
        rootVal = postorder[postEnd]
        for i in range(inStart, inEnd+1):
            if inorder[i]==rootVal:
                index = i
                break
        root = TreeNode(rootVal)
        length_left = index - inStart
        root.left = self.build(inorder, inStart, index-1, postorder, postStart, postStart+length_left-1)
        root.right = self.build(inorder, index+1, inEnd, postorder, postStart+length_left, postEnd-1)
        return root
```









