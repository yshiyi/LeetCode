class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        ans = []
        def backtrack(n, k, ans, start):
            if len(ans)==k:
                self.res.append(deepcopy(ans))
                return
            for i in range(start, n+1):
                ans.append(i)
                backtrack(n, k, ans, i+1)
                ans.pop()

        backtrack(n, k, ans, 1)
        return self.res
    
    def combine(self, n, k):
        self.ans = []
        tmp = []
        self.helper(n, 1, tmp, k)
        return self.ans
    
    def helper(self, n, start, tmp, k):
        if len(tmp)==k:
            self.ans.append(copy.deepcopy(tmp))
            return
        for i in range(start, n+1):
            tmp.append(i)
            self.helper(n, i+1, tmp, k)
            tmp.pop()
