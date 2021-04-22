# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildTree(nums, 0, len(nums)-1)
    
    def buildTree(self, nums, lo, hi):
        if lo > hi:
            return None
        maxVal = float('-inf')
        for i in range(lo, hi+1):
            if nums[i] > maxVal:
                maxVal = nums[i]
                index = i
        root = TreeNode(maxVal)
        root.left = self.buildTree(nums, lo, index-1)
        root.right = self.buildTree(nums, index+1, hi)
        return root
