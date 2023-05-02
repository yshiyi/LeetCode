"""
96M. Unique Binary Search Trees.py

Description:
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Constraints:
1 <= n <= 19
"""

"""
Method: Consider what we need to do at each node.
        We call helper() to find out the number of combinations on left branch and right branch. 
        Then # of left * # of right is the total number of BST at this node.
        Create a dictionary to record the trees to save time.
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dic = collections.defaultdict(int)
        return self.helper(1, n)
    
    def helper(self, lo, hi):
        if lo > hi:
            return 1
        if self.dic[(lo, hi)] != 0:
            return self.dic[(lo, hi)]
        res = 0
        for i in range(lo, hi+1):
            left = self.helper(lo, i-1)
            right = self.helper(i+1, hi)
            res += left*right
        self.dic[(lo, hi)] = res
        return res
