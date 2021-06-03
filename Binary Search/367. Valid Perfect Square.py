class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        left, right = 1, num//2
        while left <= right:
            mid = (right+left)//2
            if mid**2==num:
                return True
            if mid**2>num:
                right = mid-1
            else:
                left = mid+1
        return False
