class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        left, right = 0, x
        while left <= right:
            mid = int(left+right)/2
            if mid*mid<=x and (mid+1)*(mid+1)>x:
                return mid
            if mid*mid>x:
                right = mid-1
            else:
                left = mid+1
        return -1
        
