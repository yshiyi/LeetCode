# This is a recursive approach
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
        
