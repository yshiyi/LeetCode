# Method 1: Recursive approach
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, low, high):
        if root is None:
            return True
        if root.val > low and root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high):
            return True
        else:
            return False


# Method 2: Iterative approach
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        traverse(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False
        return True
