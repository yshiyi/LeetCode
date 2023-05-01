"""
235M. Lowest Common Ancestor of a Binary Search Tree.py

Description:
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Example:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

"""
Method: The common ancestor should be greater than min(p, q) and less than max(p, q).
        At each node, we compare the node.val with min(p, q) and max(p, q).
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.maxV = max(p.val, q.val)
        self.minV = min(p.val, q.val)
        return self.helper(root)
    
    def helper(self, node):
        if not node:
            return None
        if node.val < self.minV:
            return self.helper(node.right)
        if node.val > self.maxV:
            return self.helper(node.left)
        return node
