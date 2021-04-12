class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xs = str(x)
        return xs[::-1]==xs
