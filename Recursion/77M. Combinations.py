class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        ans = []
        check = [0]*(n+1)
        def backtrack(n, k, ans, start, check):
            if len(ans)==k:
                self.res.append(deepcopy(ans))
                return
            for i in range(start, n+1):
                if check[i]==0:
                    ans.append(i)
                    check[i]=1
                    backtrack(n, k, ans, i+1, check)
                    check[i]=0
                    ans.pop()
        
        backtrack(n, k, ans, 1, check)
        return self.res
