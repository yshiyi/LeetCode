# Method 1: Recursive approach
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 1
        res = res + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return res


# Method 2: using collections.deque()
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res = 0
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n = len(q)
            while n!=0:
                root = q[0]
                q.popleft()
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
                n -= 1
            res += 1
        return res
