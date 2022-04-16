"""
111. Minimum Depth of Binary Tree

Description:
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
 

Example 1:
            3
       9        20
             15    7 
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:
The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

# Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q = collections.deque()
        q.append((root, 1))
        while len(q):
            size = len(q)
            for _ in range(size):
                node, level = q.popleft()
                if node.left is None and node.right is None:
                    return level
                if node.left is not None:
                    q.append((node.left, level+1))
                if node.right is not None:
                    q.append((node.right, level+1))
        return -1
