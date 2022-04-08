"""
662. Maximum Width of Binary Tree


Description:
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), ]
where the null nodes between the end-nodes that would be present in a complete binary tree extending down to 
that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.
 

Example 1:
        1
     3     2
  5    3     9
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:
              1
         3        2
    5                  9
  6                  7
Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:
            1
       3        2
    5
Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:
The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100
"""

# Solution:# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = collections.deque([(root, 0)])
        steps = 0
        cur_depth = leftmost = ans = 0

        while q:
            for _ in range(len(q)):
                node, pos = q.popleft()
                if node:
                    q.append((node.left, pos * 2))
                    q.append((node.right, pos * 2 + 1))
                    if cur_depth != steps:
                        cur_depth = steps
                        leftmost = pos
                    print(pos, leftmost)
                    ans = max(ans, pos - leftmost + 1)
            steps += 1
        return ans