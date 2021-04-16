# Method 1: Recursive approach
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        if root==None:
            return self.ans
        self.postorderRecur(root)
        return self.ans
        
    def postorderRecur(self, root):
        if root==None:
            return
        self.postorderRecur(root.left)
        self.postorderRecur(root.right)
        self.ans.append(root.val)

# Method 2: Iterative approach
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root==None:
            return ans
        st = collections.deque()
        st.append(root)
        while len(st)!=0:
            root = st[-1]
            st.pop()
            ans.append(root.val)
            if root.left!=None:
                st.append(root.left)
            if root.right!=None:
                st.append(root.right)
        
        return ans[::-1]
