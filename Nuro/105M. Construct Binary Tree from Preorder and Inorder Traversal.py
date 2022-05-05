"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Description:
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""


"""
Method: The structure of preorder is C - L - R, and the structure of inorder is L - C - R.
        We can use preorder to determine the root value, and use inorder to determine the subtrees.
        We need to figure out what we need to do for the root.
        1. Determine the root. It is the first value in preorder.
        2. Determine the left array and the right array for the left side of and the right side of the tree, respectively.
        3. We can do this by using inorder array. We first find the root in the inorder, and then split the array into two subtrees.
        4. The subtrees in preorder can be determined using the length of them.
        5. The termination condition is preStart(prelo) > preEnd(prehi).
        6. Carefully define the start and the end positions.
"""
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
    
    def build(self, preorder, prelow, prehigh, inorder, inlow, inhigh):
        if prelow>prehigh:
            return None
        
        rootVal = preorder[prelow]
        index = 0
        for i in range(inlow, inhigh+1):
            if inorder[i]==rootVal:
                index = i
                break
        
        rootNode = TreeNode(rootVal)
        inleft_start, inleft_end = inlow, index-1
        inright_start, inright_end = index+1, inhigh
        preleft_start, preleft_end = prelow+1, prelow + index - inlow
        preright_start, preright_end = prelow+index-inlow+1, prehigh
        rootNode.left = self.build(preorder, preleft_start, preleft_end, inorder, inleft_start, inleft_end)
        rootNode.right = self.build(preorder, preright_start, preright_end, inorder, inright_start, inright_end)
        return rootNode
        
