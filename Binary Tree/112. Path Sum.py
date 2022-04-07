# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: Recursive approach, Depth-first Search
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        Sum = 0
        return self.helper(root, targetSum, Sum)
        
    def helper(self, root, targetSum, Sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            if Sum+root.val==targetSum:
                return True
            else:
                return False
        Sum += root.val
        return self.helper(root.left, targetSum, Sum) or self.helper(root.right, targetSum, Sum)


# Method 2: Iterative approach, Breadth-first Search
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        q = collections.deque()
        q.append((root, 0))
        while len(q):
            node, curSum = q.popleft()
            curSum += node.val
            if node.left is None and node.right is None:
                if curSum == targetSum:
                    return True
            if node.left:
                q.append((node.left, curSum))
            if node.right:
                q.append((node.right, curSum))
        return False

# Depth-first Search    
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        s = collections.deque()
        s.append((root, 0))
        while len(s):
            node, curSum = s.pop()
            curSum += node.val
            if node.left is None and node.right is None:
                if curSum == targetSum:
                    return True
            if node.left:
                s.append((node.left, curSum))
            if node.right:
                s.append((node.right, curSum))
        return False
