# Recursion
<!-- GFM-TOC -->
* [Leetcode Recursion](#Recursion)
    * [1. Introduction to Recursion](#1-Introduction-to-Recursion)
       * [344. Reverse String](#344-Reverse-String)
       * [24M. Swap Nodes in Pairs](#24M-Swap-Nodes-in-Pairs)
       * [206. Reverse Linked List](#206-Reverse-Linked-List)
       * [119. Pascal's Triangle II](#119-Pascals-Triangle-II)
       * [700. Search in a Binary Search Tree](#700-Search-in-a-Binary-Search-Tree)
    * [2. Memoization](#2-Memoization)
       * [509. Fibonacci Number](#509-Fibonacci-Number)
       * [70. Climbing Stairs](#70-Climbing-Stairs)
    * [3. Time Complexity](#3-Time-Complexity)
       * [50M. Pow(x, n)](#50M-Pow(x,-n))
    * [4. Space Complexity](#4-Space-Complexity)
       * [4.1 Recursion Related Space](#41-Recursion-Related-Space)
       * [4.2 Non-Recursion Related Space](#42-Non-Recursion-Related-Space)
    * [5. Tail Recursion](#5-Tail-Recursion)
    * [6. Divide and Conquer](#6-Divide-and-Conquer)
    * [7. Backtracking](#7-Backtracking)
    * [8. Divide and Conquer vs Backtracking](#8-Divide-and-Conquer-vs-Backtracking)
    * [9. Unfold Recursion to Iteration](#9-Unfold-Recursion-to-Iteration)
<!-- GFM-TOC -->

# 1. Introduction to Recursion
A recursive function should have the following properties so that it does not result in an infinite loop:
1. A simple base case (or cases) — a terminating scenario that does not use recursion to produce an answer.
2. A set of rules, also known as recurrence relation that reduces all other cases towards the base case.

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

[C++]()
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



# 3. Time Complexity
Given a recursion algorithm, its time complexity O(T) is typically the product of the number of recursion invocations (denoted as R) and the time complexity of calculation (denoted as O(s)) that incurs along with each recursion call:\
O(T) = R \* O(s)

## Execution Tree
Execution tree is a tree that is used to denote the execution flow of a recursive function in particular. Each node in the tree represents an invocation of the recursive function. Therefore, the total number of nodes in the tree corresponds to the number of recursion calls during the execution.\
Recall the example of Fibonacci number. In a full binary tree with n levels, the total number of nodes would be 2^n − 1. Therefore, the upper bound (though not tight) for the number of recursion in f(n) would be 2^n - 1, as well. As a result, we can estimate that the time complexity for f(n) would be O(2^n).\
Memoization can reduce the time complexity to O(1)\*n = O(n)

## 50M. Pow(x, n)
Pow(x, n)\
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


# 4. Space Complexity
There are mainly two parts of the space consumption that one should bear in mind when calculating the space complexity of a recursive algorithm: recursion related and non-recursion related space.\

## 4.1 Recursion Related Space
The recursion related space refers to the memory cost that is incurred directly by the recursion, i.e. the stack to keep track of recursive function calls. In order to complete a typical function call, the system allocates some space in the stack to hold three important pieces of information:
1. The returning address of the function call. Once the function call is completed, the program must know where to return to, i.e. the line of code after the function call.
2. The parameters that are passed to the function call. 
3. The local variables within the function call.

This space in the stack is the minimal cost that is incurred during a function call. However, once the function call is done, this space is freed.\
For recursive algorithms, the function calls chain up successively until they reach a base case (a.k.a. bottom case). This implies that the space that is used for each function call is accumulated.\
For example, in the exercise of printReverse, we don't have extra memory usage outside the recursive call, since we simply print a character. For each recursive call, let's assume it can use space up to a constant value. And the recursive calls will chain up to n times, where n is the size of the input string. So the space complexity of this recursive algorithm is O(n).\
It is due to recursion-related space consumption that sometimes one might run into a situation called stack overflow, where the stack allocated for a program reaches its maximum space limit and the program crashes. Therefore, when designing a recursive algorithm, one should carefully check if there is a possibility of stack overflow when the input scales up.\


## 4.2 Non Recursion Related Space
As suggested by the name, the non-recursion related space refers to the memory space that is not directly related to recursion, which typically includes the space (normally in heap) that is allocated for the global variables.\
Recursion or not, you might need to store the input of the problem as global variables, before any subsequent function calls. And you might need to save the intermediate results from the recursive calls as well. The latter is also known as memoization as we saw in the previous chapters. Therefore, in the space complexity analysis, we must take the space cost incurred by the memoization into consideration. \

# 5. Tail Recursion
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

# 6. Divide and Conquer
Divide-and-conquer algorithm is naturally implemented in the form of recursion. Another subtle difference that tells a divide-and-conquer algorithm apart from other recursive algorithms is that we break the problem down into two or more subproblems in the divide-and-conquer algorithm, rather than a single smaller subproblem.\
There are in general three steps that one can follow in order to solve the problem in a divide-and-conquer manner.
1. Divide. Divide the problem S into a set of subproblems: {S_1, S_2, ... S_n} where n>=2, i.e. there are usually more than one subproblem.
2. Conquer. Solve each subproblem recursively. 
3. Combine. Combine the results of each subproblem.


# 7. Backtracking
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


# 8. Divide and Conquer vs Backtracking
1. Often the case, the divide-and-conquer problem has a sole solution, while the backtracking problem has unknown number of solutions. For example, when we apply the merge sort algorithm to sort a list, we obtain a single sorted list, while there are many solutions to place the queens for the N-queen problem.
2. Each step in the divide-and-conquer problem is indispensable to build the final solution, while many steps in backtracking problem might not be useful to build the solution, but serve as atttempts to search for the potential solutions. For example, each step in the merge sort algorithm, i.e. divide, conquer and combine, are all indispensable to build the final solution, while there are many trials and errors during the process of building solutions for the N-queen problem.
3. When building the solution in the divide-and-conquer algorithm, we have a clear and predefined path, though there might be several different manners to build the path. While in the backtracking problems, one does not know in advance the exact path to the solution. For example, in the top-down merge sort algorithm, we first recursively divide the problems into two subproblems and then combine the solutions of these subproblems. The steps are clearly defined and the number of steps is fixed as well. While in the N-queen problem, if we know exactly where to place the queens, it would only take N steps to do so. When applying the backtracking algorithm to the N-queen problem, we try many candidates and many of them do not eventually lead to a solution but abandoned at the end. As a result, we do not know beforehand how many steps exactly it would take to build a valid solution. 


# 9. Unfold Recursion to Iteration
To convert a recursion approach to an iteration one, we could perform the following two steps:
1. We use a stack or queue data structure within the function, to replace the role of the system call stack. At each occurrence of recursion, we simply push the parameters as a new element into the data structure that we created, instead of invoking a recursion.
2. In addition, we create a loop over the data structure that we created before. The chain invocation of recursion would then be replaced with the iteration within the loop.

















