# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Method 1: Recursive approach
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self.res = None
        def recurSearch(root, val):
            if root is None:
                return
            if root.val == val:
                self.res = root
            else:
                recurSearch(root.left, val)
                recurSearch(root.right, val)
        recurSearch(root, val)
        return self.res

# Method 2: Iterative approach
        res = None
        q = collections.deque()
        q.append(root)
        while len(q):
            node = q.popleft()
            if node is None: break
            if node.val==val:
                res = node
                break
            elif node.val<val:
                q.append(node.right)
            else:
                q.append(node.left)
        return res
