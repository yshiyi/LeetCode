# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        if root is None:
            return ans
        q = collections.deque()
        q.append(root)
        while len(q)!=0:
            n1 = n2 = len(q)
            sum = 0.0
            while n1!=0:
                root = q[0]
                q.popleft()
                sum += root.val
                if root.left is not None:
                    q.append(root.left)
                if root.right is not None:
                    q.append(root.right)
                n1 -= 1
            ans.append(sum/n2)
        return ans
        
