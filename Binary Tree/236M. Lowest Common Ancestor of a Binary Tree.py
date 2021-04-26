# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: Recursive approach
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root==p or root==q:
            return root
        leftRoot = self.lowestCommonAncestor(root.left, p, q)
        rightRoot = self.lowestCommonAncestor(root.right, p, q)
        if leftRoot is not None and rightRoot is not None:
            return root
        if leftRoot is not None:
            return leftRoot
        if rightRoot is not None:
            return rightRoot


# Method 2: Iterative approach
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        m = {}
        m[root] = None
        s = collections.deque()
        s.append(root)
        while len(s)!=0:
            cur = s[-1]
            s.pop()
            if cur.right is not None:
                s.append(cur.right)
                m[cur.right] = cur
            if cur.left is not None:
                s.append(cur.left)
                m[cur.left] = cur
        
        s_ans = set()
        while m[p] is not None:
            s_ans.add(p)
            p = m[p]
        while m[q] is not None:
            if q in s_ans:
                break
            q = m[q]
        return q
