"""
230M. Kth Smallest Element in a BST.py

Description:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

"""
Method: The inorder traverse of a BST is a monotonically increasing array.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.rank = 0
        self.ans = 0
        self.helper(root, k)
        return self.ans
    
    def helper(self, root, k):
        if not root:
            return
        self.helper(root.left, k)
        self.rank += 1
        if self.rank == k:
            self.ans = root.val
            return
        self.helper(root.right, k)
