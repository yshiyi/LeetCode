# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    ans = []
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        self.help1(root, ans)
        return ans
    
    def help1(self, root, ans):
        if root is None:
            ans.append('#')
            return 
        ans.append(root.val)
        self.help1(root.left, ans)
        self.help1(root.right, ans)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return None
        d = collections.deque(data)
        return self.helper2(d)
    
    def helper2(self, d):
        i = d[0]
        d.popleft()
        if i is None:
            return None
        if i=='#':
            return None
        node = TreeNode(str(i))
        node.left = self.helper2(d)
        node.right = self.helper2(d)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
