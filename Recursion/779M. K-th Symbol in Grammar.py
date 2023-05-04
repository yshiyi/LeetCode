# This is a recursive approach
"""
If n is 1, the only element in the row is 0, so we return 0. 
Otherwise, we recursively find the value of the k-th symbol in the n-1 row. 
Let mid be the middle index of the n-1 row, which is 2^(n-2). 
If k is less than or equal to mid, then the k-th symbol in the n row is the same as the k-th symbol in the n-1 row. 
Otherwise, the k-th symbol in the n row is the complement of the k-mid-th symbol in the n-1 row.
"""
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==1:
            return 0
        mid = 2**(n-2)
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            return 1 - self.kthGrammar(n-1, k - mid)


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N==1:
            return 0
        if K%2==0:
            pre = self.kthGrammar(N-1, K/2)
        else:
            pre = self.kthGrammar(N-1, K/2+1)
        if pre==0 and K%2==0:
            return 1
        elif pre==0 and K%2==1:
            return 0
        elif pre==1 and K%2==0:
            return 0
        else:
            return 1
        
