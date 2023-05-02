"""
95M. Unique Binary Search Trees II.py

Description:
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Constraints:
1 <= n <= 8
"""

"""
Method: Consider what we need to do at each node.
        We call helper() to find out the list of possible BST from left branch and right branch.
        For each value between low and high, create a new node and connect its left and right node.
        Return the list.
        Corner cases: when lo == hi, return [TreeNode(lo)]; 
                      when lo > hi, return [None]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1, n)
    
    def helper(self, lo, hi):
        if lo == hi:
            return [TreeNode(lo)]
        if lo > hi:
            return [None]
        res = []
        for i in range(lo, hi+1):
            left = self.helper(lo, i-1)
            right = self.helper(i+1, hi)
            for node1 in left:
                for node2 in right:
                    newNode = TreeNode(i)
                    newNode.left = node1
                    newNode.right = node2
                    res.append(newNode)
        return res

