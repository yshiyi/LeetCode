# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        result = []
        seen = collections.defaultdict(int)
        def collect(root):
            if not root:
                return '#'
            l = str(root.val) + " " + collect(root.left) + " " + collect(root.right)
            seen[l] = seen.get(l, 0) + 1
            if seen[l] == 2:
                result.append(root)
            return l
        collect(root)
        return result
        
        count = collections.Counter()
        ans = []
        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans
        
        
