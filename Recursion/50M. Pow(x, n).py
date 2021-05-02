class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            if n == 0:
                return 1.0
            if n == 1:
                return x
            temp = helper(x, n/2)
            if n % 2==0:
                return temp * temp
            else:
                return temp * temp * x
        if n >=0:
            return helper(x, abs(n))
        else:
            return 1.0/helper(x, abs(n))
        
