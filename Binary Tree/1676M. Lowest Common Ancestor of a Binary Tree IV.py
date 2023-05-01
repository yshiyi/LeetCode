"""
1676M. Lowest Common Ancestor of a Binary Tree IV.py

Description:
Given the root of a binary tree and an array of TreeNode objects nodes, 
return the lowest common ancestor (LCA) of all the nodes in nodes. 
All the nodes will exist in the tree, and all values of the tree’s nodes are unique.

Extending the definition of LCA on Wikipedia: 
“The lowest common ancestor of n nodes p_1, p_2, …, p_n in a binary tree T is the lowest node 
that has every p_i as a descendant (where we allow a node to be a descendant of itself) 
for every valid i”. A descendant of a node x is a node y that is on the path from node x to some leaf node.

Constraints:
1. The number of nodes in the tree is in the range [1, 10^4].
2. -10^9 <= Node.val <= 10^9
3. All Node.val are unique.
4. All nodes[i] will exist in the tree.
5. All nodes[i] are distinct.
"""

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        self.set = set(nodes)
        return self.helper(root)
    
    def helper(self, root):
        if not root:
            return None
        if root.val in self.set:
            return root
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left and right:
            return root
        return left if left else right


