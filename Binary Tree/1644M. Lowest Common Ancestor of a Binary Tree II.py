"""
1644M. Lowest Common Ancestor of a Binary Tree II.py

Description:
Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. 
If either node p or q does not exist in the tree, return null. 
All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q 
as descendants (where we allow a node to be a descendant of itself)”. 
A descendant of a node x is a node y that is on the path from node x to some leaf node.

Constraints:
1. The number of nodes in the tree is in the range [1, 10^4].
2. -10^9 <= Node.val <= 10^9
3. All Node.val are unique.
4. p != q
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        self.findP, self.findQ = False, False
        node = self.helper(root, p, q)
        if not self.findP or not self.findQ:
            return None
        return node
    
    def helper(self, node, p, q):
        if not node:
            return None
        
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)
        
        if left and right:
            return node
        if node == p or node == q:
            if node == p: self.findP = True
            if node == q: self.findQ = True
            return node
