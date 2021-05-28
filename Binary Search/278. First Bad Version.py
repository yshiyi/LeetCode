class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while(left < right):
            mid = int((left+right)/2)
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            if not isBadVersion(mid) and not isBadVersion(mid+1):
                left = mid + 1
            if isBadVersion(mid):
                right = mid
        if left==right and isBadVersion(left):
            return left
