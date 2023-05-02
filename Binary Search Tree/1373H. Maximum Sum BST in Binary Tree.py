"""
1373H. Maximum Sum BST in Binary Tree

Description:
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

"""
Method: The return values are the key!
        We need to return four values, [if this branch is a BST (1/0), maxValue, minValue, sum]
        At each node, we need to check if both left and right branch are BST, and leftmax < root.val < right.min.
        If so, update the values in the list and return.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = 0
        self.traverse(root)
        return self.maxSum
    
    def traverse(self, root):
        if root is None:
            return [1, float('-inf'), float('inf'), 0]
        leftTree = self.traverse(root.left)
        rightTree = self.traverse(root.right)
        res = [0] * 4
        if leftTree[0]==1 and rightTree[0]==1 and root.val>leftTree[1] and root.val<rightTree[2]:
            res[0] = 1
            res[1] = max(root.val, rightTree[1])  # right[1] is the max on right branch, this step obtains the max up to current node.
            res[2] = min(root.val, leftTree[2])  # left[2] is the min of left branch, this step obtains the min up to current node.
            res[3] = root.val + leftTree[3] + rightTree[3]
            if res[3] > self.maxSum:
                self.maxSum = res[3]
        return res
        
