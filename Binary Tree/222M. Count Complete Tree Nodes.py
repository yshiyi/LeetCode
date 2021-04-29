# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftTree, rightTree = root, root
        hl, hr = 0, 0
        while leftTree is not None:
            leftTree = leftTree.left
            hl += 1
        while rightTree is not None:
            rightTree = rightTree.right
            hr += 1
        if hl == hr:
            return 2 ** hl - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
