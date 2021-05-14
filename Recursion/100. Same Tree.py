# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        dp = collections.deque()
        dq = collections.deque()
        dp.append(p)
        dq.append(q)
        
        def isValid(n1, n2):
            if n1==None and n2==None:
                return True
            if n1==None or n2==None:
                return False
            if n1.val != n2.val:
                return False
            return True
        
        while len(dp)>0:
            n1 = dp.popleft()
            n2 = dq.popleft()
            if not isValid(n1, n2):
                return False
            if n1 is not None:
                dp.append(n1.left)
                dp.append(n1.right)
                dq.append(n2.left)
                dq.append(n2.right)
        return True
        
        
