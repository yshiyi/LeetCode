"""
1650M. Lowest Common Ancestor of a Binary Tree III.py

Description:
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: 
“The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as 
descendants (where we allow a node to be a descendant of itself).”


Constraints:
1. The number of nodes in the tree is in the range [2, 10^5].
2. -10^9 <= Node.val <= 10^9
3. All Node.val are unique.
4. p != q
5. p and q exist in the tree.
"""

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        cur1, cur2 = p, q
        while cur1 != cur2:
            if not cur1: cur1 = q
            else: cur1 = cur1.parent
            if not cur2: cur2 = p
            else: cur2 = cur2.parent
        return cur1
