"""
314M. Binary Tree Vertical Order Traverse

Description:
Given a binary tree, return thevertical ordertraversal of its nodes' values. 
(ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.


Examples 1:
Input:
[3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:
[
  [9],
  [3,15],
  [20],
  [7]
]


Examples 2:
Input: 
[3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]


Examples 3:
Input:
[3,9,8,4,0,1,7,null,null,null,2,5]
 (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
Output:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

"""
Method: Similar to 987H
        In this problem, for those nodes in the same column, we save them from top to bottom and from left to right.
        Therefore, we can use bfs to traverse the tree and use use a hashmap to save them.
        The key is the col, and the value is a list.
        Time complexity: O(NlogN), mainly due to the sorting part at the end
        Space complexity: O(N), hashmap
"""
# Solution:
import collections
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def verticalOrder(self, root):
        dic = collections.defaultdict(list)
        q = collections.deque()
        q.append((0, root))
        while len(q):
            col, node = q.popleft()
            dic[col].append(node.val)
            if node.left is not None:
                q.append((col-1, node.left))
            if node.right is not None:
                q.append((col+1, node.right))
        
        ans = []
        for key in sorted(dic.keys()):
            ans.append(dic[key])
        return ans
