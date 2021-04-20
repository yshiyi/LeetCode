"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Method 1: Recursive approach
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def findNext(node):
            if node is None:
                return None
            if node.left:
                return node.left
            if node.right:
                return node.right
            return findNext(node.next)

        def helper(root):
            if root is None:
                return
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = findNext(root.next)
            if root.right:
                root.right.next = findNext(root.next)
            helper(root.right)
            helper(root.left)
        helper(root)
        return root

# Method 2: Iterative approach
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None;
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n1 = n2 = len(q)
            while n2!=0:
                cur = q[0]
                q.popleft()
                n2 -= 1
                if n2!=0:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
