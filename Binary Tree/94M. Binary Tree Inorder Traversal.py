# Method 1: Recursive approach
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        if root==None:
            return self.ans
        self.inorderRecur(root)
        return self.ans
        
    def inorderRecur(self, root):
        if root==None:
            return
        self.inorderRecur(root.left)
        self.ans.append(root.val)
        self.inorderRecur(root.right)
 
# Method 2: Iterative approach
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root==None:
            return ans
        st = collections.deque()
        while root!=None or len(st)!=0:
            while root!=None:
                st.append(root)
                root = root.left
            root = st[-1]
            st.pop()
            ans.append(root.val)
            root = root.right
        return ans
