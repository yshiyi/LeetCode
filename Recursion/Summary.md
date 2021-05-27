# Recursion
<!-- GFM-TOC -->
* [Leetcode Recursion](#Recursion)
    * [1. Introduction to Recursion](#1-Introduction-to-Recursion)
       * [100. Same Tree](#100-Same-Tree) 
       * [344. Reverse String](#344-Reverse-String)
       * [24M. Swap Nodes in Pairs](#24M-Swap-Nodes-in-Pairs)
       * [206. Reverse Linked List](#206-Reverse-Linked-List)
       * [119. Pascal's Triangle II](#119-Pascals-Triangle-II)
       * [700. Search in a Binary Search Tree](#700-Search-in-a-Binary-Search-Tree)
       * [21. Merge Two Sorted Lists](#21-Merge-Two-Sorted-Lists)
       * [779M. K-th Symbol in Grammar](#779M-Kth-Symbol-in-Grammar)
       * [95M. Unique Binary Search Trees II](#95M-Unique-Binary-Search-Trees-II)
       * [33. Search in Rotated Sorted Array](#33-Search-in-Rotated-Sorted-Array)
    * [2. Memoization](#2-Memoization)
       * [509. Fibonacci Number](#509-Fibonacci-Number)
       * [70. Climbing Stairs](#70-Climbing-Stairs)
    * [3. Complexity Analysis](#3-Complexity-Analysis)
       * [3.1 Time Complexity](#31-Time-Complexity)
       * [3.2 Space Complexity](#32-Space-Complexity)
          * [3.2.1 Recursion Related Space](#321-Recursion-Related-Space)
          * [3.2.2 Non-Recursion Related Space](#322-Non-Recursion-Related-Space)
       * [3.3 Tail Recursion](#33-Tail-Recursion)
       * [50M. Pow(x, n)](#50M-Powx-n)
       * [104. Maximum Depth of Binary Tree](#104-Maximum-Depth-of-Binary-Tree)
    * [4. Divide and Conquer](#4-Divide-and-Conquer)
       * [912M. Sort an Array](#912M-Sort-an-Array)
       * [98M. Validate Binary Search Tree](#98M-Validate-Binary-Search-Tree)
       * [240M. Search a 2D Matrix II](#240M-Search-a-2D-Matrix-II)
       * [215M. Kth Largest Element in an Array](#215M-Kth-Largest-Element-in-an-Array)
       * [241. Different Ways to Add Parentheses](#241-Different-Ways-to-Add-Parentheses)
    * [5. Backtracking](#5-Backtracking)
       * [22M. Generate Parentheses](#22M-Generate-Parentheses)
       * [51H. N-Queens](#51H-NQueens)
       * [52H. N-Queens II](#52H-NQueens-II)
       * [489H. Robot Room Cleaner](#489H-Robot-Room-Cleaner)
       * [37H. Sudoku Solver](#37H-Sudoku-Solver)
       * [77M. Combinations](#77M-Combinations)
       * [78M. Subsets](#78M-Subsets)
       * [46M. Permutations](#46M-Permutations)
       * [47M. Permutations II](#46M-Permutations-II)
       * [17M. Letter Combinations of a Phone Number](#17M-Letter-Combinations-of-a-Phone-Number)
       * [698M. Partition to K Equal Sum Subsets](#698M-Partition-to-K-Equal-Sum-Subsets)
    * [6. Divide and Conquer vs Backtracking](#6-Divide-and-Conquer-vs-Backtracking)
    * [7. Unfold Recursion to Iteration](#7-Unfold-Recursion-to-Iteration)
<!-- GFM-TOC -->

# 1. Introduction to Recursion
A recursive function should have the following properties so that it does not result in an infinite loop:
1. A simple base case (or cases) — a terminating scenario that does not use recursion to produce an answer.
2. A set of rules, also known as recurrence relation that reduces all other cases towards the base case.

## 100. Same Tree
Tree, Depth-first Search\
**Description:**\
Given the roots of two binary trees p and q, write a function to check if they are the same or not.\
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/100.%20Same%20Tree.cpp)
```
// Method 1: Recursive approach
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p==NULL && q==NULL){
            return true;
        }
        if(p==NULL || q==NULL){
            return false;
        }
        if(p->val != q->val){
            return false;
        }
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

// Method 2: Iterative approach
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<TreeNode*> qP, qQ;
        qP.push(p); qQ.push(q);
        TreeNode *cur1, *cur2;
        while(qP.size()>0 && qQ.size()>0){
            cur1 = qP.front(); qP.pop();
            cur2 = qQ.front(); qQ.pop();
            if(!isValid(cur1, cur2)){
                return false;
            }
            if(cur1 != NULL){
                if(!isValid(cur1->left, cur2->left)){
                    return false;
                }
                if(cur1->left != NULL){
                    qP.push(cur1->left);
                    qQ.push(cur2->left);
                }
                if(!isValid(cur1->right, cur2->right)){
                    return false;
                }
                if(cur1->right != NULL){
                    qP.push(cur1->right);
                    qQ.push(cur2->right);
                }
            }
        }
        return true;
    }
    bool isValid(TreeNode* n1, TreeNode* n2){
        if(n1==NULL && n2==NULL){
            return true;
        }
        if(n1==NULL || n2==NULL){
            return false;
        }
        if(n1->val != n2->val){
            return false;
        }
        return true;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/100.%20Same%20Tree.py)
```
class Solution(object):
    def isSameTree(self, p, q):
        dp = collections.deque()
        dq = collections.deque()
        dp.append(p)
        dq.append(q)
        
        def isValid(n1, n2):
            if n1==None and n2==None:
                return True
            if n1==None or n2==None:
                return False
            if n1.val != n2.val:
                return False
            return True
        
        while len(dp)>0:
            n1 = dp.popleft()
            n2 = dq.popleft()
            if not isValid(n1, n2):
                return False
            if n1 is not None:
                dp.append(n1.left)
                dp.append(n1.right)
                dq.append(n2.left)
                dq.append(n2.right)
        return True
```


## 344. Reverse String
Two Pointers, String\
**Description:**\
Write a function that reverses a string. The input string is given as an array of characters s.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/344.%20Reverse%20String.cpp)
```
class Solution {
public:
    void reverseString(vector<char>& s) {
        helper(s, 0, s.size()-1);
        return;
    }
    void helper(vector<char>& str, int left, int right){
        if(left>right){
            return;
        }
        swap(str[left], str[right]);
        helper(str, ++left, --right);
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/344.%20Reverse%20String.py)
```
class Solution(object):
    def reverseString(self, s):
        def helper(s, left, right):
            if left > right:
                return
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            helper(s, left, right)
        helper(s, 0, len(s)-1)
        return
```

## 24M. Swap Nodes in Pairs
**Description:**\
Given a linked list, swap every two adjacent nodes and return its head.\
**Example:**\
Input: head = \[1,2,3,4\]\
Output: \[2,1,4,3\]\
**Method:**\
To solve a recursive problem, we only need to consider two things:
1. What is the base case? In this problem, the base case is head is NULL or head->next is NULL.
2. What should we do in the current step? Save head->next->next as a temp, swap head and head->next, and call recursive function.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/24M.%20Swap%20Nodes%20in%20Pairs.cpp)
```
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        ListNode *head2 = head->next, *tmp = head->next->next;
        head2->next = head;
        head->next = swapPairs(tmp);
        
        return head2;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/24M.%20Swap%20Nodes%20in%20Pairs.py)
```
class Solution(object):
    def swapPairs(self, head):
        # Method 1
        def recurSwap(head):
            if head is None or head.next is None:
                return head
            temp = head.next.next
            head2 = head.next
            head2.next = head
            head.next = recurSwap(temp)
            return head2
        return recurSwap(head)
      
        # Method 2
        if head is None or head.next is None:
            return head
        temp = head.next.next
        head2 = head.next
        head2.next = head
        head.next = self.swapPairs(temp)
        return head2
```

## 206. Reverse Linked List
**Description:**\
Given the head of a singly linked list, reverse the list, and return the reversed list.\
**Method:**\
We only show the recursive approach here.
There are two recursive approach we can use:
1. For each single node, we call the recursive function with cur->next.\
   The return of the recursion function should be a reversed linked list.\
   Then, cur node is pointing to the end of the reversed linked list, because the original cur->next is now at the end of the list.\
   Now, we only need to move cur node to the end of the list. \
   cur->next->next = cur, let cur->next point to cur itself\
   cur->next = NULL, make cur be the last node in the list
2. In this approach, we create a new list with a pseudo head.\
   The basic idea of this approach is that we iterate through the original list and add each cur node to the next of head2.\
   e.g. head = 1-2, head2 = 0\
   head = 2, head2 = 0-1\
   head = NULL, head2 = 0-2-1

[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/206.%20Reverse%20Linked%20List.cpp)
```
// Method 1:
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL || head->next==NULL){
            return head;
        }
        ListNode* last = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        return last;
    }
};

// Method 2:
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL){
            return head;
        }
        ListNode *head2 = new ListNode(0);
        head2 = recurReverse(head, head2);
        return head2->next;
    }
    ListNode* recurReverse(ListNode* head, ListNode* head2){
        if(head==NULL){
            return head;
        }
        ListNode* temp1 = head->next;
        ListNode* temp2 = head2->next;
        head2->next = head;
        head->next = temp2;
        recurReverse(temp1, head2);
        return head2;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/206.%20Reverse%20Linked%20List.py)
```
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return head
        head2 = ListNode(0)
        
        def recurReverse(head, head2):
            if head is None:
                return head
            temp1, temp2 = head.next, head2.next
            head2.next = head
            head.next = temp2
            recurReverse(temp1, head2)
            return head2
        
        head2 = recurReverse(head, head2)
        return  head2.next
```

## 119. Pascals Triangle II
Array\
**Description:**\
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.\
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:\
1\
11\
121\
1331\
14641\
**Method:**\
We first create a vector to store the values and assign 1 to the first and the last position.\
We then inquire the values in the previous row.\
Finally, construct the current row based on the values from the previous row.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/119.%20Pascal's%20Triangle%20II.cpp)
```
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(rowIndex+1);
        res[0] = 1;
        if(rowIndex==0){
            return res;
        }
        res[rowIndex] = 1;
        vector<int> preRow = getRow(rowIndex-1);
        for(int i=1; i<rowIndex; i++){
            res[i] = preRow[i-1] + preRow[i];
        }
        return res;
      }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/119.%20Pascal's%20Triangle%20II.py)
```
class Solution(object):
    def getRow(self, rowIndex):
        res = [0] * (rowIndex+1)
        res[0] = 1
        if rowIndex==0:
            return res
        res[rowIndex] = 1
        preRow = self.getRow(rowIndex-1)
        for i in range(1, rowIndex):
            res[i] = preRow[i-1] + preRow[i]
        return res
```

## 700. Search in a Binary Search Tree
Tree\
**Description:**\
You are given the root of a binary search tree (BST) and an integer val.\
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/700.%20Search%20in%20a%20Binary%20Search%20Tree.cpp)
```
// Method 1: Recursive approach
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root==NULL){
            return NULL;
        }
        recurSearch(root, val);
        return res;
    }
    void recurSearch(TreeNode* root, int val){
        if(root==NULL){
            return;
        }
        if(root->val == val){
            res = root;
        }else{
            recurSearch(root->left, val);
            recurSearch(root->right, val);
        }
    }
private:
    TreeNode* res;
};

// Method 2: Iterative approach
class Solution {
public:
    TreeNode* searchBST(TreeNode* root, int val) {
        if(root==NULL){
            return NULL;
        }
        queue<TreeNode*> q;
        q.push(root);
        while(q.size()){
            TreeNode* cur = q.front(); q.pop();
            if(cur->val==val){
                return cur;
            }
            if(cur->left != NULL){
                q.push(cur->left);
            }
            if(cur->right != NULL){
                q.push(cur->right);
            }
        }
        return NULL;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/700.%20Search%20in%20a%20Binary%20Search%20Tree.py)
```
class Solution(object):
    def searchBST(self, root, val):
        self.res = None
        def recurSearch(root, val):
            if root is None:
                return
            if root.val == val:
                self.res = root
            else:
                recurSearch(root.left, val)
                recurSearch(root.right, val)
        recurSearch(root, val)
        return self.res
```

## 21. Merge Two Sorted Lists
Linked List\
**Description:**\
Merge two sorted linked lists and return it as a new sorted list. \
The new list should be made by splicing together the nodes of the first two lists.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/21.%20Merge%20Two%20Sorted%20Lists.cpp)
```
class Solution {
public:
    ListNode *ans = new ListNode(0);
    ListNode *cur = ans;
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        recurMerge(l1, l2);
        return ans->next;
    }
    void recurMerge(ListNode *l1, ListNode *l2){
        if(l1==NULL){
            cur->next = l2;
            return;
        }else if(l2==NULL){
            cur->next = l1;
            return;
        }
        if(l1->val <= l2->val){
            cur->next = l1;
            cur = cur->next;
            recurMerge(l1->next, l2);
        }else{
            cur->next = l2;
            cur = cur->next;
            recurMerge(l1, l2->next);
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/21.%20Merge%20Two%20Sorted%20Lists.py)
```
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        ans = ListNode(None)
        self.l = ans
        def recurMerge(l1, l2):
            if l1 is None:
                self.l.next = l2
                return
            if l2 is None:
                self.l.next = l1
                return
            if l1.val <=l2.val:
                self.l.next = l1
                self.l = self.l.next
                recurMerge(l1.next, l2)
            else:
                self.l.next = l2
                self.l = self.l.next
                recurMerge(l1, l2.next)
            
        recurMerge(l1, l2)
        return ans.next
```

## 779M. Kth Symbol in Grammar
Recursion\
**Description:**\
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.\
Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).\
**Method:**\
Consider the base case first, where we should return 0 when N==1.\
Then the recurrence relation, if K is an even number then, we should inquire the K/2 th number in the previous row.\
If K is an odd number, then we should inquire the K/2+1 th number in the previous row.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/779M.%20K-th%20Symbol%20in%20Grammar.cpp)
```
class Solution {
public:
    int pre;
    int kthGrammar(int N, int K) {
        if(N==1){
            return 0;
        }
        if(K%2==0){
            pre = kthGrammar(N-1, K/2);
        }else{
            pre = kthGrammar(N-1, K/2+1);
        }
        if(pre==0 && K%2==0){
            return 1;
        }else if(pre==0 && K%2==1){
            return 0;
        }else if(pre==1 && K%2==0){
            return 0;
        }else{
            return 1;
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/779M.%20K-th%20Symbol%20in%20Grammar.py)
```
class Solution(object):
    def kthGrammar(self, N, K):
        if N==1:
            return 0
        if K%2==0:
            pre = self.kthGrammar(N-1, K/2)
        else:
            pre = self.kthGrammar(N-1, K/2+1)
        if pre==0 and K%2==0:
            return 1
        elif pre==0 and K%2==1:
            return 0
        elif pre==1 and K%2==0:
            return 0
        else:
            return 1
```

## 95M. Unique Binary Search Trees II
Dynamic Programming, Tree\
**Description:**\
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.\
**Method:**\
The basic structure of a binary search tree is that all the nodes in the left subtrees are less than the root and all the nodes in the right subtrees are greater than the root.\
For the target number n, we will treat each of the number between 1 to n as a root.\
Therefore, we should create a recursive function to take a range of numbers.\
Then basic case is when the left limit is equal to the right limit, then we just return the node with that value. If left is greater than right, we return null.\
The recurrence relation is for each number between left and right, we send all numbers between left and i-1 to the recursive function and send all the number between i+1 and right to recursive function.\
We are supposed to obtain a constructed left subtree and a constructed right subtree.\
For each node in the left subtree we connect it to the left of the root node. For each node in the right subtree we connect it to the right of the root node.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/95M.%20Unique%20Binary%20Search%20Trees%20II.cpp)
```
class Solution {
public:
    vector<TreeNode*> recurGen(int left, int right){
        if(left==right){
            return {new TreeNode(left)};
        }else if(left > right){
            return {NULL};
        }
        vector<TreeNode*> res;
        for(int i=left; i<=right; i++){
            vector<TreeNode*> L = recurGen(left, i-1);
            vector<TreeNode*> R = recurGen(i+1, right);
            for(auto l:L){
                for(auto r:R){
                    TreeNode* cur = new TreeNode(i);
                    cur->left = l;
                    cur->right = r;
                    res.push_back(cur);
                }
            }
        }
        return res;
    }
    vector<TreeNode*> generateTrees(int n) {
        return recurGen(1, n);
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/95M.%20Unique%20Binary%20Search%20Trees%20II.py)
```
class Solution(object):
    def generateTrees(self, n):
        def recurGen(left, right):
            if left==right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            res = []
            for i in range(left, right+1):
                L = recurGen(left, i-1)
                R = recurGen(i+1, right)
                for l in L:
                    for r in R:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        res.append(cur)
            return res
            
        return recurGen(1, n)
```

## 33M. Search in Rotated Sorted Array
Array, Binary Search\
**Description:**\
There is an integer array nums sorted in ascending order (with distinct values).\
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is \[nums\[k\], nums\[k+1\], ..., nums\[n-1\], nums\[0\], nums\[1\], ..., nums\[k-1\]\] (0-indexed).\
For example, \[0,1,2,4,5,6,7\] might be rotated at pivot index 3 and become \[4,5,6,7,0,1,2\].\
Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.\
**Method:**\
We can still use the conventional binary search approach. \
Notice, if the mid is less than right, then the right part is an ascending sequence. Otherwise, the left part is.\
Comparing to the conventional binary search, there are four scenarios we need to consider.\
Also note, since mid = left+(right-left)/2, mid could be equal to left. We need to consider this scenario as well.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/33M.%20Search%20in%20Rotated%20Sorted%20Array.cpp)
```
// Solution 1: Compare mid to right
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size()-1, target);
    }
    int binarySearch(vector<int>& nums, int left, int right, int target){
        if (left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid] < nums[right]){
                if(target>nums[mid] && target<=nums[right]){
                    return binarySearch(nums, mid+1, right, target);
                }else{
                    return binarySearch(nums, left, mid-1, target);
                }
            }else{
                if(target<nums[mid] && target>=nums[left]){
                    return binarySearch(nums, left, mid-1, target);
                }else{
                    return binarySearch(nums, mid+1, right, target);
                }
            }
        }
        return -1;
    }
};

// Solution 2: Compare mid to left
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size()-1, target);
    }
    int binarySearch(vector<int>& nums, int left, int right, int target){
        if (left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid] >= nums[left]){
                if(target<nums[mid] && target>=nums[left]){
                    return binarySearch(nums, left, mid-1, target);
                }else{
                    return binarySearch(nums, mid+1, right, target);
                }
            }else{
                if(target>nums[mid] && target<=nums[right]){
                    return binarySearch(nums, mid+1, right, target);
                }else{
                    return binarySearch(nums, left, mid-1, target);
                }
            }
        }
        return -1;
    }
};

// Solution: Iterative approach
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        while(left<=right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid] < nums[right]){
                if(target>nums[mid] && target<=nums[right]){
                    left = mid + 1;
                }else{
                    right = mid - 1;
                }
            }else{
                if(target<nums[mid] && target>=nums[left]){
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }
        }
        return -1;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/33M.%20Search%20in%20Rotated%20Sorted%20Array.py)
```
class Solution(object):
    def search(self, nums, target):
        def binarySearch(nums, left, right, target):
            if left <= right:
                mid = int(left + (right-left)/2)
                if nums[mid] == target:
                    return mid
                if nums[mid] < nums[right]:
                    if nums[mid]<target and target<=nums[right]:
                        return binarySearch(nums, mid+1, right, target)
                    else:
                        return binarySearch(nums, left, mid-1, target)
                else:
                    if nums[left]<=target and target<nums[mid]:
                        return binarySearch(nums, left, mid-1, target)
                    else:
                        return binarySearch(nums, mid+1, right, target)
            return -1
        return binarySearch(nums, 0, len(nums)-1, target)
```

# 2. Memoization
In some cases, we may encounter the duplicate calculations problem where some intermediate results are calculated multiple times.\
To eliminate the duplicate calculation in the recursion, one of the idea would be to store the intermediate results in the cache so that we could reuse them later without re-calculation.\
This idea is also known as memoization, which is a technique that is frequently used together with recursion.

## 509. Fibonacci Number
Array\
**Description:**\
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,\
F(0) = 0, F(1) = 1\
F(n) = F(n - 1) + F(n - 2), for n > 1.\
Given n, calculate F(n).\
**Method:**\
If we use the standard recursive approach, the time complexity will be O(2^N).\
Therefore, we need a dictionary to store the values that we have calculated.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/509.%20Fibonacci%20Number.cpp)
```
class Solution {
public:
    map<int, int> m;
    int fib(int n) {
        if(n<2){
            m[n] = n;
            return n;
        }
        if(m.find(n-1)==m.end()){
            m[n-1] = fib(n-1);
        }
        if(m.find(n-2)==m.end()){
            m[n-2] = fib(n-2);
        }
        return m[n-1] + m[n-2];
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/509.%20Fibonacci%20Number.py)
```
class Solution(object):
    m = {}
    def fib(self, n):
        if n<2:
            Solution.m[n] = n
            return n
        if n-1 not in Solution.m:
            Solution.m[n-1] = self.fib(n-1)
        if n-2 not in Solution.m:
            Solution.m[n-2] = self.fib(n-2)
        return Solution.m[n-1] + Solution.m[n-2]
```

## 70. Climbing Stairs
Dynamic Programming\
**Description:**\
You are climbing a staircase. It takes n steps to reach the top.\
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?\
**Method:**\
Consider the basic case in which there are only 1 step or 2 steps left.\
When there is only 1 step left, there is only 1 way. When there are 2 steps left, there are 2 different ways (i.e.m 1+1 and 2).\
The recursive procedure is no. of ways to reach n is equal to the sum of no. of ways to reach n-1 and that to reach to n-2.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/70.%20Climbing%20Stairs.cpp)
```
class Solution {
public:
    map<int, int> m;
    int climbStairs(int n) {
        if(n<3){
            m[n] = n;
            return n;
        }
        if(m.find(n-1)==m.end()){
            m[n-1] = climbStairs(n-1);
        }
        if(m.find(n-2)==m.end()){
            m[n-2] = climbStairs(n-2);
        }
        return m[n-1] + m[n-2];
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/70.%20Climbing%20Stairs.py)
```
class Solution(object):
    m = {}
    def climbStairs(self, n):
        if n<3:
            Solution.m[n] = n
            return n
        if n-1 not in Solution.m:
            Solution.m[n-1] = self.climbStairs(n-1)
        if n-2 not in Solution.m:
            Solution.m[n-2] = self.climbStairs(n-2)
        return Solution.m[n-1] + Solution.m[n-2]
```


# 3. Complexity Analysis
## 3.1 Time Complexity
Given a recursion algorithm, its time complexity O(T) is typically the product of the number of recursion invocations (denoted as R) and the time complexity of calculation (denoted as O(s)) that incurs along with each recursion call:\
O(T) = R \* O(s)

### Execution Tree
Execution tree is a tree that is used to denote the execution flow of a recursive function in particular. Each node in the tree represents an invocation of the recursive function. Therefore, the total number of nodes in the tree corresponds to the number of recursion calls during the execution.\
Recall the example of Fibonacci number. In a full binary tree with n levels, the total number of nodes would be 2^n − 1. Therefore, the upper bound (though not tight) for the number of recursion in f(n) would be 2^n - 1, as well. As a result, we can estimate that the time complexity for f(n) would be O(2^n).\
Memoization can reduce the time complexity to O(1)\*n = O(n)


## 3.2 Space Complexity
There are mainly two parts of the space consumption that one should bear in mind when calculating the space complexity of a recursive algorithm: recursion related and non-recursion related space.\

### 3.2.1 Recursion Related Space
The recursion related space refers to the memory cost that is incurred directly by the recursion, i.e. the stack to keep track of recursive function calls. In order to complete a typical function call, the system allocates some space in the stack to hold three important pieces of information:
1. The returning address of the function call. Once the function call is completed, the program must know where to return to, i.e. the line of code after the function call.
2. The parameters that are passed to the function call. 
3. The local variables within the function call.

This space in the stack is the minimal cost that is incurred during a function call. However, once the function call is done, this space is freed.\
For recursive algorithms, the function calls chain up successively until they reach a base case (a.k.a. bottom case). This implies that the space that is used for each function call is accumulated.\
For example, in the exercise of printReverse, we don't have extra memory usage outside the recursive call, since we simply print a character. For each recursive call, let's assume it can use space up to a constant value. And the recursive calls will chain up to n times, where n is the size of the input string. So the space complexity of this recursive algorithm is O(n).\
It is due to recursion-related space consumption that sometimes one might run into a situation called stack overflow, where the stack allocated for a program reaches its maximum space limit and the program crashes. Therefore, when designing a recursive algorithm, one should carefully check if there is a possibility of stack overflow when the input scales up.\


### 3.2.2 Non Recursion Related Space
As suggested by the name, the non-recursion related space refers to the memory space that is not directly related to recursion, which typically includes the space (normally in heap) that is allocated for the global variables.\
Recursion or not, you might need to store the input of the problem as global variables, before any subsequent function calls. And you might need to save the intermediate results from the recursive calls as well. The latter is also known as memoization as we saw in the previous chapters. Therefore, in the space complexity analysis, we must take the space cost incurred by the memoization into consideration. \

## 3.3 Tail Recursion
Tail recursion is a recursion where the recursive call is the final instruction in the recursion function. And there should be only one recursive call in the function.\
The difference between non-tail-recursion and tail-recursion is that in the non-tail-recursion example there is an extra computation after the very last recursive call. For example, we would like to calculate the sum of a list of numbers:
```
def sum_non_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    if len(ls) == 0:
        return 0
    
    # not a tail recursion because it does some computation after the recursive call returned.
    return ls[0] + sum_non_tail_recursion(ls[1:])


def sum_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    def helper(ls, acc):
        if len(ls) == 0:
            return acc
        # this is a tail recursion because the final instruction is a recursive call.
        return helper(ls[1:], ls[0] + acc)
    
    return helper(ls, 0)
```
The benefit of having tail recursion is that it could avoid the accumulation of stack overheads during the recursive calls, since the system could reuse a fixed amount space in the stack for each recursive call.\
Note that in tail recursion, we know that as soon as we return from the recursive call we are going to immediately return as well, so we can skip the entire chain of recursive calls returning and return straight to the original caller. That means we don't need a call stack at all for all of the recursive calls, which saves us space.\
A tail recursion function can be executed as non-tail-recursion functions, i.e. with piles of call stacks, without impact on the result. Often, the compiler recognizes tail recursion pattern, and optimizes its execution. However, not all programming languages support this optimization. For instance, C, C++ support the optimization of tail recursion functions. On the other hand, Java and Python do not support tail recursion optimization.

## 50M. Pow(x, n)
Math, Binary Search\
**Dexcription:**\
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).\
**Method:**\
If we use the brute force approach, the time complexity will be O(n).\
To accelerate the calculation process, we can use divide and conquer approach. The time complexity is O(log(n)).
1. Divid the whole list into two pieces, and calculate the result for each of them.
2. If n is even number, then just return temp * temp. If n is an odd number, then return temp * temp * x.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/50M.%20Pow(x,%20n).cpp)
```
class Solution {
public:
    double myPow(double x, int n) {
        if(n>=0){
            return helper(x, n);
        }else {
            return 1/helper(x, abs(n));
        }
    }
    double helper(double x, int n){
        if(n==0){
            return 1.0;
        }else if(n == 1){
            return x;
        }
        double temp = helper(x, n/2);
        if (n % 2 == 0) {
            return temp * temp;
        }else{
            return temp * temp * x;
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/50M.%20Pow(x%2C%20n).py)
```
# Method 1: Recursive approach
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            if n == 0:
                return 1.0
            if n == 1:
                return x
            temp = helper(x, n/2)
            if n % 2==0:
                return temp * temp
            else:
                return temp * temp * x
        if n >=0:
            return helper(x, abs(n))
        else:
            return 1.0/helper(x, abs(n))
        

"""
Method 2: Iterative approach
          This doesn't work in C++, because it will exceed the limit of int when n is super large.
          Note: every number can be represented as a combination of even powers.
                e.g. x^5 = x^1 * x^4, x^9 = x^1 + x^8 
"""
class Solution(object):
    def myPow(self, x, n):
        res = 1.0
        if n<0:
            x = 1/x
            n = -n
        while n:
            if n%2==1:
                res *= x
            x *= x
            n /= 2
        return res
```

## 104. Maximum Depth of Binary Tree
**Description:**\
Given the root of a binary tree, return its maximum depth.\
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.\
[C++]
```
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

# 4. Divide and Conquer
Divide-and-conquer algorithm is naturally implemented in the form of recursion. Another subtle difference that tells a divide-and-conquer algorithm apart from other recursive algorithms is that we break the problem down into two or more subproblems in the divide-and-conquer algorithm, rather than a single smaller subproblem.\
There are in general three steps that one can follow in order to solve the problem in a divide-and-conquer manner.
1. Divide. Divide the problem S into a set of subproblems: {S_1, S_2, ... S_n} where n>=2, i.e. there are usually more than one subproblem.
2. Conquer. Solve each subproblem recursively. 
3. Combine. Combine the results of each subproblem.

## 912M. Sort an Array
**Description:**\
Given an array of integers nums, sort the array in ascending order.\
**Method:**\
Here, we just apply merge sort method which is a typical example of using divide and conquer method.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/912M.%20Sort%20an%20Array.cpp)
```
class Solution {
public:
    int pivot;
    vector<int> sortArray(vector<int>& nums) {
        if(nums.size()<2){
            return nums;
        }
        vector<int> left, right;
        // Choose the middle value as a pivot
        pivot = nums.size()/2;
        for(int i=0; i<pivot; i++){
            left.push_back(nums[i]);
        }
        for(int i=pivot; i<nums.size();i++){
            right.push_back(nums[i]);
        }
        // Sort left array and right array first, and then merge them
        return merge(sortArray(left), sortArray(right));
    }
    vector<int> merge(vector<int> left, vector<int> right){
        int l = 0, r = 0;
        vector<int> res;
        while(l<left.size() && r<right.size()){
            if(left[l]<=right[r]){
                res.push_back(left[l]);
                l++;
            }else{
                res.push_back(right[r]);
                r++;
            }
        }
        if(l==left.size()){
            for(int i=r;r<right.size(); r++){
                res.push_back(right[r]);
            }
        }
        if(r==right.size()){
            for(int i=l; l<left.size(); l++){
                res.push_back(left[l]);
            }
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/912M.%20Sort%20an%20Array.py)
```
class Solution(object):
    def sortArray(self, nums):
        if len(nums)==1:
            return nums
        pivot = int(len(nums)/2)
        return self.mergeSort(self.sortArray(nums[0:pivot]), self.sortArray(nums[pivot:]))
    
    def mergeSort(self, left, right):
        l, r = 0, 0
        res = []
        while l<len(left) and r<len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        res.extend(left[l:])
        res.extend(right[r:])
        return res
```

## 98M. Validate Binary Search Tree
Tree, Depth-first Search, Recursion\
**Description:**\
Given the root of a binary tree, determine if it is a valid binary search tree (BST).\
A valid BST is defined as follows:\
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

**Method:**\
The base case is when the node is null. 
Note the last node is not necessary a valid BST, it can be greater its root.
There are four conditions to be satisfied:
1. root->val > minVal. 
   For the left subtree, the minVal is just the INT_MIN.
   For the right subtree, the minVal is the root->val.
2. root->val < maxVal. 
   For the left subtree, the maxVal is the root->val.
   For the right subtree, the maxVal is INT_MAX.
3. root->left and root->right are both valid BST.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/98M.%20Validate%20Binary%20Search%20Tree.cpp)
```
// Method 1: Recursive approach
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        long minVal = INT64_MIN, maxVal = INT64_MAX;
        return helper(root, minVal, maxVal);
    }
    bool helper(TreeNode* root, long minVal, long maxVal){
        if(root==NULL){
            return true;
        }
        if(root->val > minVal && root->val < maxVal && helper(root->left, minVal, root->val) 
           && helper(root->right, root->val, maxVal)){
            return true;
        }else{
            return false;
        }
    }
};

// Method 2: Iterative approach, use in-order traverse method
class Solution {
public:
    vector<int> res;
    bool isValidBST(TreeNode* root) {
        traverse(root);
        for(int i=0; i<res.size()-1; i++){
            if(res[i]>=res[i+1]){
                return false;
            }
        }
        return true;
    }
    
    /* 
       If we don't use a global variable, we can define the function like:
       void traverse(TreeNode* root, vector<int>& res)
       Note: it must be the reference of res.
    */
    void traverse(TreeNode* root){
        if(root==NULL){
            return;
        }
        traverse(root->left);
        res.push_back(root->val);
        traverse(root->right);
        return;
    }
    
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/98M.%20Validate%20Binary%20Search%20Tree.py)
```
class Solution(object):
    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, low, high):
        if root is None:
            return True
        if root.val > low and root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high):
            return True
        else:
            return False
```


## 240M. Search a 2D Matrix II
Binary Search, Divide and Conquer\
**Description:**\
Write an efficient algorithm that searches for a target value in an m x n integer matrix. \
The matrix has the following properties:\
Integers in each row are sorted in ascending from left to right.\
Integers in each column are sorted in ascending from top to bottom.\
**Method:**\
The solution of this problem is a little tricky.\
We start the search from the top right corner. If the target is less than the current value, we move to the left. If the target is greater than the current value, we move below.\

[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/240M.%20Search%20a%202D%20Matrix%20II.cpp)
```
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0, col = matrix[0].size()-1;
        while(row<matrix.size() && col>=0){
            if(matrix[row][col]==target){
                return true;
            }
            if(matrix[row][col]>target){
                col--;
            }else{
                row++;
            }
        }
        return false;
    }
}
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/240M.%20Search%20a%202D%20Matrix%20II.py)
```
class Solution(object):
    def searchMatrix(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        r, c = 0, col-1
        while r<row and c>=0:
            print(matrix[r][c])
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False
```

## 215M. Kth Largest Element in an Array
Divide and Conquer, Heap\
**Description:**\
Given an integer array nums and an integer k, return the kth largest element in the array.\
Note that it is the kth largest element in the sorted order, not the kth distinct element.\
**Method:**\
Quickselect approach\
Instead of sweeping the vector from left, we sweep the vector from right.\
At the end of partition function, we should swap nums\[++i\] and nums\[pivot_index\] to ensure all the values on the right side of pivot are greater than it.\
In this script, we select the most rightmost value as the pivot. The run time is about 40 ms.\
If we select a random pivot, we can increase the run time to 4-8 ms.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/215M.Kth%20Largest%20Element%20in%20an%20Array.cpp)
```
// Method 1:
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return quickSelect(nums, 0, nums.size()-1, k);
    }
    int quickSelect(vector<int>& nums, int left, int right, int k){
        // if(k<=right-left+1){
        if(right>=left){ 
            int pivot_index = partition(nums, left, right);
            if(right - pivot_index == k-1){
                return nums[pivot_index];
            }
            if(right - pivot_index > k-1){
                return quickSelect(nums, pivot_index+1, right, k);
            }else{
                return quickSelect(nums, left, pivot_index-1, k-(right-pivot_index+1));
            }
        }
        return -1;
    }
    int partition(vector<int>& nums, int left, int right){
        int pivot = nums[right];
        int pivot_index = right-1;
        for(int i=right-1; i>=left; i--){
            if(nums[i] >= pivot){
                swap(nums[i], nums[pivot_index]);
                pivot_index--;
            }
        }
        swap(nums[++pivot_index], nums[right]);
        return pivot_index;
    }
};

/*
Method 2: In this script, we randomly select the pivot.
          Note, we need to record the new position of the pivot.
          To generate a random number between a and a+b-1, we use rand()% b + a.
          The run time is about 4-8 ms.
*/
int partition(vector<int>& nums, int left, int right){
    if(right==left){
        return left;
    }
    int pivot_index = rand() % (right-left+1) + left;
    int pivot = nums[pivot_index];
    int i = right;
    for(int j=right;j>=left;j--){
        if(nums[j]>=pivot){
            swap(nums[j], nums[i]);
            if(j==pivot_index){
                pivot_index = i;
            }
            i--;
        }
    }
    swap(nums[++i], nums[pivot_index]);
    return i;
}
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/215M.Kth%20Largest%20Element%20in%20an%20Array.py)
```
class Solution(object):
    def findKthLargest(self, nums, k):
        def partition(nums, left, right):
            pivot_index = randint(left, right)
            pivot = nums[pivot_index]
            i = right
            for j in range(right, left-1, -1):
                if nums[j]>=pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    if j==pivot_index:
                        pivot_index = i
                    i -= 1
            i += 1
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            return i
        def quickSelect(nums, left, right, k):
            if left<=right:
                index = partition(nums, left, right)
                if right - index == k - 1:
                    return nums[index]
                if right - index > k - 1:
                    return quickSelect(nums, index+1, right, k)
                else:
                    return quickSelect(nums, left, index-1, k-(right-index+1))
            return -1
        return quickSelect(nums, 0, len(nums)-1, k)
```


## 241. Different Ways to Add Parentheses
Divide and Conquer\
**Description:**\
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. \
You may return the answer in any order.\
**Method:**\
Given an example: 2-1-1. The two possible solutions are:\
(2-1) - (1) = 0\
(2) - (1-1) = 2\
We can see we seperate the equation at the any operator.\
The final solution is the combination of the result from the left and that from the right.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/241M.%20Different%20Ways%20to%20Add%20Parentheses.cpp)
```
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        vector<int> res;
        for(int i=0; i<expression.size(); i++){
            char c = expression[i];
          
            // If there is an operator, we seperate the expression into left part and right part.
            if(c=='+'||c=='-'||c=='*'){
                // Both left and right part contains all possible results.
                vector<int> left = diffWaysToCompute(expression.substr(0, i));
                vector<int> right = diffWaysToCompute(expression.substr(i+1));
                
                // We then combine the results from left and right based on the operator.
                for(auto vl:left){
                    for(auto vr:right){
                        if(c=='+'){
                            res.push_back(vl+vr);
                        }else if(c=='-'){
                            res.push_back(vl-vr);
                        }else if(c=='*'){
                            res.push_back(vl*vr);
                        }
                    }
                }
            }
        }
        
        /* This part defines the base case.
           If there is nothing added to the res, it means there is no operator.
           It means the expression only contains a sinlge number.
        */
        if(res.empty()){
            res.push_back(stoi(expression));
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/241M.%20Different%20Ways%20to%20Add%20Parentheses.py)
```
class Solution(object):
    def diffWaysToCompute(self, expression):
        res = []
        for i in range(len(expression)):
            c = expression[i]
            if c=='+' or c=='-' or c=='*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for vl in left:
                    for vr in right:
                        if c=='+':
                            res.append(vl+vr)
                        elif c=='-':
                            res.append(vl-vr)
                        elif c=='*':
                            res.append(vl*vr)
            
        if len(res)==0:
            res.append(int(expression))
        return res
```


# 5. Backtracking
Backtracking is a general algorithm for finding all (or some) solutions to some computational problems (notably Constraint satisfaction problems or CSPs), which incrementally builds candidates to the solution and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot lead to a valid solution. \
A pseudocode template for backtracking algorithm:
```
# Python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
```
Here are a few notes about the above pseudocode.
1. Overall, the enumeration of candidates is done in two levels: 1). at the first level, the function is implemented as recursion. At each occurrence of recursion, the function is one step further to the final solution.  2). as the second level, within the recursion, we have an iteration that allows us to explore all the candidates that are of the same progress to the final solution.
2. The backtracking should happen at the level of the iteration within the recursion. 
3. Unlike brute-force search, in backtracking algorithms we are often able to determine if a partial solution candidate is worth exploring further (i.e. is_valid(next_candidate)), which allows us to prune the search zones. This is also known as the constraint, e.g. the attacking zone of queen in N-queen game. 
4. There are two symmetric functions that allow us to mark the decision (place(candidate)) and revert the decision (remove(candidate)).  

The basic idea of the backtracking method is similar to traversing a decision tree. There are three things that we need to consider:
1. The terminal condition. When to stop the recursion.
2. The path. All the decisions that have been taken.
3. The candidates. The list of candidates.

## 22M. Generate Parentheses
**Description:**\
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.\
**Example:**\
Input: n = 3\
Output: \["((()))","(()())","(())()","()(())","()()()"\]\
**Method:**\
backtrack
1. setting up the base case, when the total length of the string is equal to 2*n
2. if it is possible, insert "(" first.
3. whenever the number of "(" is greater than ")", insert ")"

Note: don't use if-else, in that case, we will only insert ")" when the number of "(" is equal to n.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/22M.%20Generate%20Parentheses.cpp)
```
class Solution {
public:
    vector<string> res; 
    vector<string> generateParenthesis(int n) {
        backTrack(0, 0, n, "");
        return res;
    }
    void backTrack(int left, int right, int n, string S){
        if(S.size()==n*2){
            res.push_back(S);
            return;
        }
        if(left < n){
            backTrack(left+1, right, n, S+'(');
        }
        if(left > right){
            backTrack(left, right+1, n, S+')');
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/22M.%20Generate%20Parentheses.py)
```
class Solution(object):
    def generateParenthesis(self, n):
        S = ""
        res = []
        left, right = 0, 0
        def backTracking(left, right, S):
            if len(S)==n*2:
                res.append(S)
                return
            else:
                if left < n:
                    backTracking(left+1, right, S+'(')
                if left > right:
                    backTracking(left, right+1, S+')')
                
        backTracking(left, right, S)
        return res
```

## 51H. N-Queens
**Description:**\
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.\
Given an integer n, return all distinct solutions to the n-queens puzzle.\
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.\
**Method:**\
Create a vector\<string\> to hold the layout of the board.\
Then we check the board row by row.\
In each row, we also check each column and also check if the cell is a valid position to place the queen.\
Once we place the queen, then we call the recursion to check the following rows.\
Once it is done, we take out the queen from the current cell and move to the next one.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/51H.%20N-Queens.cpp)
```
class Solution {
public:
    vector<vector<string>> res;
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        backtrack(board, 0);
        return res;
    }
    void backtrack(vector<string>& board, int row){
        if(row == board.size()){
            res.push_back(board);
            return;
        }
        int n = board.size();
        for(int col=0; col < n; col++){
            if(is_valid(board, row, col)){
                board[row][col] = 'Q';
                backtrack(board, row+1);
                board[row][col] = '.';
            }
        }
    }
    bool is_valid(vector<string>& board, int row, int col){
        // Check if there is queen in the same column
        for(int i=0; i<board.size(); i++){
            if(board[i][col]=='Q'){
                return false;
            }
        }
        // Check upper right side
        for(int i=row-1, j=col+1; i>=0 && j<board.size(); i--, j++){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        // Check upper left side
        for(int i=row-1, j=col-1; i>=0 && j>=0; i--, j--){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        return true;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/51H.%20N-Queens.py)
```
'''
Method:
1. Create a board. board = [list('.'*n) for i in range(n)]
   Note: we convert a string to a list, because the string doesn't support item assignment in Python.
2. Save a valid solution.
   Res = []
   for r in board:
       Res.append(''.join(deepcopy(r)))
       Res.append(''.join(list(r)))  # this also works and is faster than deepcopy()
   res.append(Res)
   Note: need to first deepcopy the result, otherwise it will be kept modifying the element values
         also need to convert the list back to the string. Using ''.join(list).
'''
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [list('.'*n) for i in range(n)]
        def isValid(board, row, col):
            for i in range(len(board)):
                if board[i][col]=='Q':
                    return False
            i, j = row-1, col+1
            while i>=0 and j<len(board):
                if board[i][j]=='Q':
                    return False
                i -= 1
                j += 1
            i, j = row-1, col-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i -= 1
                j -= 1
            return True
        
        def backtrack(board, row):
            if row == len(board):
                Res = []
                for r in board:
                    Res.append(''.join(list(r)))
                res.append(Res)
                return
            for col in range(len(board[0])):
                if isValid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'
        
        backtrack(board, 0)
        return res
```

## 52H. N-Queens II
**Description:**\
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.\
Given an integer n, return the number of distinct solutions to the n-queens puzzle.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/52H.%20N-Queens%20II.cpp)
```
class Solution {
public:
    int res=0;
    int totalNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        backtrack(board, 0);
        return res;
    }
    void backtrack(vector<string>& board, int row){
        if(row==board.size()){
            ++res;
            return;
        }
        for(int col=0; col<board[0].size(); col++){
            if(isValid(board, row, col)){
                board[row][col] = 'Q';
                backtrack(board, row+1);
                board[row][col] = '.';
            }
        }
    }
    bool isValid(vector<string>& board, int row, int col){
        for(int i=0; i<board.size(); i++){
            if(board[i][col]=='Q'){
                return false;
            }
        }
        for(int i=row-1, j=col+1; i>=0 && j<board.size(); i--, j++){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        for(int i=row-1, j=col-1; i>=0 && j>=0; i--, j--){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        return true;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Recursion/52H.%20N-Queens%20II.py)
```
class Solution(object):
    def totalNQueens(self, n):
        self.res = 0
        board = [list('.'*n) for i in range(n)]
        def isValid(board, row, col):
            for i in range(len(board)):
                if board[i][col]=='Q':
                    return False
            i, j = row-1, col+1
            while i>=0 and j<len(board):
                if board[i][j]=='Q':
                    return False
                i -= 1
                j += 1
            i, j = row-1, col-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i -= 1
                j -= 1
            return True
        
        def backtrack(board, row):
            if row == len(board):
                self.res += 1
                return
            for col in range(len(board[0])):
                if isValid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'
        
        backtrack(board, 0)
        return self.res
```

## 489H. Robot Room Cleaner
**Description:**\
Given a robot cleaner in a room modeled as a grid.\
Each cell in the grid can be empty or blocked.\
The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.\
When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.\
Design an algorithm to clean the entire room using only the 4 given APIs shown below.
```
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();
  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();
  // Clean the current cell.
  void clean();
}
```
**Method:**\
As usual, three things need to be concerned.
1. The base case. In this case, we don't have the map, so we don't have any ending condition.
2. The path. We need to mark the cell as visited when the robot passes by.
3. Create four directions. For each direction, we try to move the robot.
   If the next cell has been visited or it is blocked/boundary, we try the next direction.

Note: we need to move the robot back to the previous position after backtracking.
[C++](https://github.com/yshiyi/LeetCode/blob/main/Recursion/489H.%20Robot%20Room%20Cleaner.cpp)
```
class Solution {
public:
    // Define movements in four different directions: left, up, right and down
    // -1, 0, 1 represent the changes in the row or column
    vector<vector<int>> dirs{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    void cleanRoom(Robot& robot) {
        // Define a set to record the cells that are visited
        unordered_set<string> visited;
        backtrack(robot, 0, 0, 0, visited);
    }
    void backtrack(Robot& robot, int x, int y, int dir, unordered_set<string>& visited) {
        // When enter a cell, the robot cleans it
        robot.clean();
        // Record this cell and mark it as cleaned
        visited.insert(to_string(x) + "-" + to_string(y));
        // Try different four directions
        for (int i = 0; i < 4; ++i) {
            // This is a tricky part. The current the direction is the direction of the movement from the last cell.
            // In this solution, i=0 represent the current direction.
            int cur = (i + dir) % 4, newX = x + dirs[cur][0], newY = y + dirs[cur][1];
            
            // Use .count() to check if we have visited this cell
            // Use robot.move() to check if the next is open or an obstacle.
            if (!visited.count(to_string(newX) + "-" + to_string(newY)) && robot.move()) {
                backtrack(robot, newX, newY, cur, visited);
              
                // The following lines of command make the robot move back the last cell.
                robot.turnRight();
                robot.turnRight();
                robot.move();
                robot.turnLeft();
                robot.turnLeft();
            }
            // If the next cell has been visited or is an obstacle, the robot simply turns right and trys next direction.
            robot.turnRight();
        }
    }
};
```

## 37H. Sudoku Solver
## 77M. Combinations
## 78M. Subsets
## 46M. Permutations
## 47M. Permutations II
## 17M. Letter Combinations of a Phone Number
## 698M. Partition to K Equal Sum Subsets


# 6. Divide and Conquer vs Backtracking
1. Often the case, the divide-and-conquer problem has a sole solution, while the backtracking problem has unknown number of solutions. For example, when we apply the merge sort algorithm to sort a list, we obtain a single sorted list, while there are many solutions to place the queens for the N-queen problem.
2. Each step in the divide-and-conquer problem is indispensable to build the final solution, while many steps in backtracking problem might not be useful to build the solution, but serve as atttempts to search for the potential solutions. For example, each step in the merge sort algorithm, i.e. divide, conquer and combine, are all indispensable to build the final solution, while there are many trials and errors during the process of building solutions for the N-queen problem.
3. When building the solution in the divide-and-conquer algorithm, we have a clear and predefined path, though there might be several different manners to build the path. While in the backtracking problems, one does not know in advance the exact path to the solution. For example, in the top-down merge sort algorithm, we first recursively divide the problems into two subproblems and then combine the solutions of these subproblems. The steps are clearly defined and the number of steps is fixed as well. While in the N-queen problem, if we know exactly where to place the queens, it would only take N steps to do so. When applying the backtracking algorithm to the N-queen problem, we try many candidates and many of them do not eventually lead to a solution but abandoned at the end. As a result, we do not know beforehand how many steps exactly it would take to build a valid solution. 


# 7. Unfold Recursion to Iteration
To convert a recursion approach to an iteration one, we could perform the following two steps:
1. We use a stack or queue data structure within the function, to replace the role of the system call stack. At each occurrence of recursion, we simply push the parameters as a new element into the data structure that we created, instead of invoking a recursion.
2. In addition, we create a loop over the data structure that we created before. The chain invocation of recursion would then be replaced with the iteration within the loop.

















