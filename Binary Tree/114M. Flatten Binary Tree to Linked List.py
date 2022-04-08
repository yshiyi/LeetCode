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
        
        # Another approach:
        if root is None:
            return root
        s = collections.deque()
        s.append((root, 0))
        parent = root
        while len(s):
            cur, v = s.pop()
            if v==0:
                if cur.right:
                    s.append((cur.right, 0))
                if cur.left:
                    s.append((cur.left, 0))
                    cur.left = None
                s.append((cur, 1))
            else:
                if parent!=cur:
                    parent.right = cur
                    parent = cur
                
        return root


# Method 2: Recursive approach
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        leftTree = self.flatten(root.left)
        rightTree = self.flatten(root.right)
        root.right = leftTree
        root.left = None
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = rightTree
        return root
