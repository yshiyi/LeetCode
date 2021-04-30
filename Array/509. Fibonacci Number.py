# This is a recursive solution
class Solution(object):
    m = {}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        if n-1 not in Solution.m:
            Solution.m[n-1] = self.fib(n-1)
        if n-2 not in Solution.m:
            Solution.m[n-2] = self.fib(n-2)
        return Solution.m[n-1] + Solution.m[n-2]
