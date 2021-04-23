# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        
    def build(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd:
            return None
        rootVal = postorder[postEnd]
        for i in range(inStart, inEnd+1):
            if inorder[i]==rootVal:
                index = i
                break
        root = TreeNode(rootVal)
        length_left = index - inStart
        root.left = self.build(inorder, inStart, index-1, postorder, postStart, postStart+length_left-1)
        root.right = self.build(inorder, index+1, inEnd, postorder, postStart+length_left, postEnd-1)
        return root
        
        
