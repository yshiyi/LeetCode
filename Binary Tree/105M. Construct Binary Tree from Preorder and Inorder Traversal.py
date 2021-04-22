# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        
    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd:
           return None
        rootVal = preorder[preStart]
        for i in range(inStart, inEnd+1):
            if inorder[i]==rootVal:
                index = i
                break
        root = TreeNode(rootVal)
        length_left = index - inStart
        root.left = self.build(preorder, preStart+1, preStart+length_left, inorder, inStart, index-1)
        root.right = self.build(preorder, preStart+length_left+1, preEnd, inorder, index+1, inEnd)
        return root
