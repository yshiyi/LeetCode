class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left<right:
            mid = (left+right)//2
            if not isBadVersion(mid):
                left = mid+1
            else:
                right = mid
        return left
