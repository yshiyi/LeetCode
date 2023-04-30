"""
889M. Construct Binary Tree from Preorder and Postorder Traversal

Description:
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values 
and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
If there exist multiple answers, you can return any of them.

Example:
       1
      /  \
     2    3
    / \  / \
   4  5 6   7
preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

Constraints:
1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
"""

"""
Method: There is no unique solution, because we can't determine the exact left branch or right branch.
        Then we choose the value right behind preorder[preleft] as the value of the root.left.
        Then we use this value to determine the left branch and the right branch in postorder.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(preorder, 0, len(preorder)-1, postorder, 0, len(postorder)-1)
    
    def helper(self, preorder, preleft, preright, postorder, postleft, postright):
        if preleft > preright:
            return None
        if preleft == preright:
            return TreeNode(preorder[preleft])
        rootVal = preorder[preleft]
        targetVal = preorder[preleft+1]
        for i in range(postleft, postright+1):
            if postorder[i] == targetVal:
                index = i
                break
        
        postleftstart, postleftend = postleft, index
        postrightstart, postrightend = index+1, postright-1
        preleftstart, preleftend = preleft+1, preleft+1+index-postleft
        prerightstart, prerightend = preleft+2+index-postleft, preright

        root = TreeNode(rootVal)
        root.left = self.helper(preorder, preleftstart, preleftend, postorder, postleftstart, postleftend)
        root.right = self.helper(preorder, prerightstart, prerightend, postorder, postrightstart, postrightend)
        return root


