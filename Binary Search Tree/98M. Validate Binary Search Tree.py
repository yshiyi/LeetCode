"""
98M. Validate Binary Search Tree.py

Description:
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

# Method 1: post-traverse
class Solution(object):
    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, minV, maxV):
        if not root:
            return True
        if minV >= root.val:
            return False
        if maxV <= root.val:
            return False

        return self.helper(root.left, minV, root.val) and self.helper(root.right, root.val, maxV)

# Method 2: pre-traverse
class Solution(object):
    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, minV, maxV):
        if not root:
            return True
        left = self.helper(root.left, minV, root.val)
        right = self.helper(root.right, root.val, maxV)
        if right and left and root.val>minV and root.val<maxV:
            return True
        else:
            return False
