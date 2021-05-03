# Method 1: Recursive approach
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
        

"""
Method 2: Iterative approach
          This doesn't work in C++, because it will exceed the limit of int when n is super large.
          Note: every number can be represented as a combination of even powers.
                e.g. x^5 = x^1 * x^4, x^9 = x^1 + x^8 
"""
class Solution(object):
    def myPow(self, x, n):
        res = 1.0
        if n<0:
            x = 1/x
            n = -n
        while n:
            if n%2==1:
                res *= x
            x *= x
            n /= 2
        return res
