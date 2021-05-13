# Recursion
<!-- GFM-TOC -->
* [Leetcode Recursion](#Recursion)
    * [1. Introduction to Recursion](#1-Introduction-to-Recursion)
    * [2. Memoization](#2-Memoization)
    * [3. Time Complexity](#3-Time-Complexity)
    * [4. Space Complexity](#4-Space-Complexity)
       * [4.1 Recursion Related Space](#41-Recursion-Related-Space)
       * [4.2 Non-Recursion Related Space](#42-Non-Recursion-Related-Space)
    * [5. Tail Recursion](#5-Tail-Recursion)
    * [6. Divide and Conquer](#6-Divide-and-Conquer)
    * [7. Backtracking](#7-Backtracking)
    * [8. Unfold Recursion to Iteration](#8-Unfold-Recursion-to-Iteration)
<!-- GFM-TOC -->

# 1. Introduction to Recursion
A recursive function should have the following properties so that it does not result in an infinite loop:
1. A simple base case (or cases) — a terminating scenario that does not use recursion to produce an answer.
2. A set of rules, also known as recurrence relation that reduces all other cases towards the base case.

# 2. Memoization
In some cases, we may encounter the duplicate calculations problem where some intermediate results are calculated multiple times.\
To eliminate the duplicate calculation in the recursion, one of the idea would be to store the intermediate results in the cache so that we could reuse them later without re-calculation.\
This idea is also known as memoization, which is a technique that is frequently used together with recursion.

# 3. Time Complexity
Given a recursion algorithm, its time complexity O(T) is typically the product of the number of recursion invocations (denoted as R) and the time complexity of calculation (denoted as O(s)) that incurs along with each recursion call:\
O(T) = R \* O(s)

## Execution Tree
Execution tree is a tree that is used to denote the execution flow of a recursive function in particular. Each node in the tree represents an invocation of the recursive function. Therefore, the total number of nodes in the tree corresponds to the number of recursion calls during the execution.\
Recall the example of Fibonacci number. In a full binary tree with n levels, the total number of nodes would be 2^n − 1. Therefore, the upper bound (though not tight) for the number of recursion in f(n) would be 2^n - 1, as well. As a result, we can estimate that the time complexity for f(n) would be O(2^n).\
Memoization can reduce the time complexity to O(1)\*n = O(n)

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


# 8. Unfold Recursion to Iteration
To convert a recursion approach to an iteration one, we could perform the following two steps:
1. We use a stack or queue data structure within the function, to replace the role of the system call stack. At each occurrence of recursion, we simply push the parameters as a new element into the data structure that we created, instead of invoking a recursion.
2. In addition, we create a loop over the data structure that we created before. The chain invocation of recursion would then be replaced with the iteration within the loop.

















