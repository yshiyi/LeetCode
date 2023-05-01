"""
538M. Convert BST to Greater Tree.py

Description:
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the 
original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

Example:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Constraints:
1. The number of nodes in the tree is in the range [0, 104].
2. -104 <= Node.val <= 104
3. All the values in the tree are unique.
4. root is guaranteed to be a valid binary search tree.
"""

"""
Method: Note that the inorder traverse generates a monotonically increasing array.
        If we reverse the order of helper(root.left) and helper(root.right), we can generate a monotonically decreasing array.
        We can then calculate the sum and assign it to the current node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
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
