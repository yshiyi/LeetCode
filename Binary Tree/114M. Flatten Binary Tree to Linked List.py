# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: Iterative approach
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        s = collections.deque()
        s.append(root)
        ref = root
        while len(s)!=0:
            cur = s[-1]
            s.pop()
            if cur.right is not None:
                s.append(cur.right)
            if cur.left is not None:
                s.append(cur.left)
                cur.left = None
            if ref!=cur:
                ref.right = cur
                ref = cur
        return root


# Method 2: Recursive approach
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        tempLeft = root.left
        tempRight = root.right
        root.left = None
        root.right = tempLeft
        cur = root
        while cur.right is not None:
            cur = cur.right
        cur.right = tempRight
        return root
