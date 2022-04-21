"""
515. Find Largest Value in Each Tree Row

Description:
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).


Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
"""

"""
Method: Use BFS
        Time complexity: O(N), N is the number of nodes
        Space complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
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
            max_node = float('-inf')
            for _ in range(size):
                node = q.popleft()
                max_node = max(max_node, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max_node)
        return ans
