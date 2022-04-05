# Method 1: Recursive approach
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Method 2: using collections.deque()
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q = collections.deque()
        q.append(root)
        steps = 0
        while len(q):
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
            steps += 1
        return steps
