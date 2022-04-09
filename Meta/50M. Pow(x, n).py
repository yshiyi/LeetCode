"""
50. Pow(x, n)

Description:
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""

"""
Method 1: Recursive approach
          Time complexity: O(logN)
          Space complexity: O(logN)
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n>0:
            return self.helper(x, n)
        else:
            return 1/self.helper(x, -n)
    
    def helper(self, x, n):
        if n == 0:
            return 1
        tmp = self.helper(x, n/2)
        if n%2==0:
            return tmp * tmp
        else:
            return tmp * tmp * x

# Method 2: Iterative approach
class Solution(object):
    def myPow(self, x, n):
        res = 1
        if n<0:
            x = 1/x
            n = -n
        while n:
            if n%2==1:
                res = res *x
            n /= 2
            x *= x
        return res
