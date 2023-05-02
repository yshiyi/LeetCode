"""
450M. Delete Node in a BST.py

Description:
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1. Search for a node to remove.
2. If the node is found, delete the node.

Constraints:
1. The number of nodes in the tree is in the range [0, 104].
2. -105 <= Node.val <= 105
3. Each node has a unique value.
4. root is a valid binary search tree.
5. -105 <= key <= 105
"""

"""
Method: 
void BST(TreeNode root, int target) {
    if (root.val == target)
        // 找到目标，做点什么
    if (root.val < target) 
        BST(root.right, target);
    if (root.val > target)
        BST(root.left, target);
}
Use the basic structure to find the target node.
Consider three scenarios:
1. the target is at leaf: not root.left and not root.right. Then just delete it, return None.
2. the target has only one branch. Then if not root.left: return root.right; if not root.right: return root.left.
3. the target has both branch. Then we need to find the min value from the right branch and replace the target node with it.
   Note: the min of the right branch is at the left most.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == key:
            if not root.left and not root.right:
                return None
            if not root.left: return root.right
            if not root.right: return root.left

            minNode = self.getMin(root.right)
            root.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            minNode.right = root.right
            root = minNode

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def getMin(self, node):
        while node.left:
            node = node.left
        return node
