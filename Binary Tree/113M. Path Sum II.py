"""
113. Path Sum II

Description:
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. 
A leaf is a node with no children.
 

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
            1
         2     3
Input: root = [1,2,3], targetSum = 5
Output: []


Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

# Method: Recursive approach
class Solution(object):
    def pathSum(self, root, targetSum):
        ans = []
        if not root:
            return ans
        path = []
        self.helper(root, targetSum, 0, path, ans)
        return ans
    
    def helper(self, root, targetSum, curSum, path, ans):
        if root is None:
            return
        path.append(root.val)
        curSum += root.val
        if root.left is None and root.right is None:
            if curSum==targetSum:
                ans.append(copy.deepcopy(path))
        self.helper(root.left, targetSum, curSum, path, ans)
        self.helper(root.right, targetSum, curSum, path, ans)
        path.pop()
