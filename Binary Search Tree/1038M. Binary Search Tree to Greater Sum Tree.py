"""
1038M. Binary Search Tree to Greater Sum Tree.py

Description:
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of 
the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

Same as 538M.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.helper(root)
        return root
    
    def helper(self, root):
        if not root:
            return None
        self.helper(root.right)
        self.sum += root.val
        root.val = self.sum
        self.helper(root.left)
