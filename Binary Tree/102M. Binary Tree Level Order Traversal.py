# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root is None:
            return ans
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n = len(q)
            l = []
            while n!=0:
                root = q[0]
                q.popleft()
                l.append(root.val)
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
                n -= 1
            ans.append(l)
        return ans
        
