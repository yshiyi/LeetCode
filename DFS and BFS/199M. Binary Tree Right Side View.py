"""
199. Binary Tree Right Side View

Description:
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.


Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

"""
Method: BFS, from right to left, and save the first node
        Time complexity: O(N)
        Space complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = collections.deque()
        q.append(root)
        ans = []
        while len(q):
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i==0:
                    ans.append(node.val)
                if node.right:
                    q.append(node.right)
                elif node.left:
                    q.append(node.left)
        return ans
