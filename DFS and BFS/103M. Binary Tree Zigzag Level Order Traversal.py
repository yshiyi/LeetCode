"""
103. Binary Tree Zigzag Level Order Traversal
Description:
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).
 
Example 1:
        3
    9      20
       15      7
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""

"""
Method: Use BFS. Also need to record the level/row.
        When in the odd row, we need to reverse the list.
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        q = collections.deque()
        q.append((root, 0))
        while len(q):
            size = len(q)
            l = []
            for _ in range(len(q)):
                node, row = q.popleft()
                l.append(node.val)
                if node.left:
                    q.append((node.left, row+1))
                if node.right:
                    q.append((node.right, row+1))
            if row%2==0:
                ans.append(l)
            else:
                ans.append(l[::-1])
        return ans
