# This is a recursive solution.
class Solution(object):
    m = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            Solution.m[n] = n
            return n
        if n-1 not in Solution.m:
            Solution.m[n-1] = self.climbStairs(n-1)
        if n-2 not in Solution.m:
            Solution.m[n-2] = self.climbStairs(n-2)
        return Solution.m[n-1] + Solution.m[n-2]
