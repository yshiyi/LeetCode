"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# Method 1: Recursive Approach
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        self.connectTwoNode(root.left, root.right)
        return root
    
    def connectTwoNode(self, node1, node2):
        if node2 is None:
            return
        node1.next = node2
        self.connectTwoNode(node1.left, node1.right)
        self.connectTwoNode(node2.left, node2.right)
        self.connectTwoNode(node1.right, node2.left)

# Method 2: Iterative approach
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n = len(q)
            while n!=0:
                cur = q[0]
                q.popleft()
                if n!=1:
                    cur.next = q[0]
                else:
                    cur.next = None
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
                n -= 1
        return root
