# Method 1:
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, c = 0, 0
        l = []
        while i<len(s):
            while i<len(s) and s[i] == '0':
                c += 1
                i += 1
            if c != 0:
                l.append(c)
                c = 0
            while i<len(s) and s[i] == '1':
                c += 1
                i += 1
            if c!= 0:
                l.append(c)
                c = 0
        
        ans = 0
        for j in range(len(l)-1):
            ans += min(l[j], l[j+1])
        return ans

# Method 2:
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        l = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                l[-1] +=1
            else:
                l.append(1)
        
        ans = 0
        for j in range(len(l)-1):
            ans += min(l[j], l[j+1])
        return ans
