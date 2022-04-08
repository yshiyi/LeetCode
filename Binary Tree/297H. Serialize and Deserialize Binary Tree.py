# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "#"
        q = collections.deque()
        q.append(root)
        data = ""
        while len(q):
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node is None:
                    data += "#" + ","
                    continue
                else:
                    data += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)
        return data[:-1]
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "#":
            return None
        strs = data.split(",")
        root = TreeNode(int(strs[0]))
        i = 1
        q = collections.deque()
        q.append(root)
        while len(q):
            node = q.popleft()
            if strs[i]!="#":
                node.left = TreeNode(int(strs[i]))
            if strs[i+1]!="#":
                node.right = TreeNode(int(strs[i+1]))
            i += 2
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
