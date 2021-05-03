# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def recurGen(left, right):
            if left==right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            res = []
            for i in range(left, right+1):
                L = recurGen(left, i-1)
                R = recurGen(i+1, right)
                for l in L:
                    for r in R:
                        cur = TreeNode(i)
                        cur.left = l
                        cur.right = r
                        res.append(cur)
            return res
        
        return recurGen(1, n)
