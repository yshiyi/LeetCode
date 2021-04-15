class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        st = collections.deque()
        while True:
            while root!=None:
                ans.append(root.val)
                st.append(root)
                root = root.left
            if len(st)==0:
                break
            root = st[-1]
            st.pop()
            root = root.right
        
        return ans
