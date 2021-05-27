# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left<=right:
            mid = int(left+right)/2
            if guess(mid)==0:
                return mid
            if guess(mid)==1:
                left = mid + 1
            if guess(mid)==-1:
                right = mid - 1
