# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: Recursive approach, Depth-first Search
#           Note: define sum as a general variable. 
#           If we define it as self.sum (global variable), it will keep accumlating every time we call it.
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        self.res = False
        Sum = 0
        self.checkSum(root, targetSum, Sum)
        return self.res
    
    def checkSum(self, node, targetSum, Sum):
        if node is None:
            return
        Sum += node.val
        if node.left is None and node.right is None and Sum == targetSum:
            self.res = True
        self.checkSum(node.left, targetSum, Sum)
        self.checkSum(node.right, targetSum, Sum)


# Method 2: Iterative approach, Breadth-first Search
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        q = collections.deque()
        q.append((root, root.val))
        res = []
        while len(q)!=0:
            cur, curSum = q[0]
            q.popleft()
            if cur.left is None and cur.right is None:
                res.append(curSum)
            if cur.left is not None:
                q.append((cur.left, curSum+cur.left.val))
            if cur.right is not None:
                q.append((cur.right, curSum+cur.right.val))
        
        for v in res:
            if v == targetSum:
                return True
        return False
