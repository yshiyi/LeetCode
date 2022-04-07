"""
543. Diameter of Binary Tree

Description:
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.


Example 1:
            1
      2           3
  4      5
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

"""
Method: Recursion
        Post-process. helper will return the max length of left and that of right.
        Update maxLen, and return max(l, r)+1.
        Note: we don't add 1 when updating maxLen.
        Time complexity: O(N)
        Space complexity: O(N), this is a kind of stack, the maximum elements in the stack is N
"""
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLen = 0
        self.helper(root)
        return self.maxLen
    
    def helper(self, root):
        if not root:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.maxLen = max(self.maxLen, l+r)
        return max(l+1, r+1)

