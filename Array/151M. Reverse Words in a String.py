# Method: using string.split()
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = s.split()
        ans = ""
        for i in range(len(sl)-1, -1, -1):
            ans += sl[i] + " "

        return ans[:-1]
