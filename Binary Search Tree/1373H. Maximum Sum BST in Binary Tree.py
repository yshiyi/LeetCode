# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = 0
        self.traverse(root)
        return self.maxSum
    
    def traverse(self, root):
        if root is None:
            return [1, float('-inf'), float('inf'), 0]
        leftTree = self.traverse(root.left)
        rightTree = self.traverse(root.right)
        res = [0] * 4
        if leftTree[0]==1 and rightTree[0]==1 and root.val>leftTree[1] and root.val<rightTree[2]:
            res[0] = 1
            res[1] = max(root.val, rightTree[1])
            res[2] = min(root.val, leftTree[2])
            res[3] = root.val + leftTree[3] + rightTree[3]
            if res[3] > self.maxSum:
                self.maxSum = res[3]
        return res
        
