# Method 1:
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Dis_s = collections.Counter(s)
        for c in t:
            if c in Dis_s:
                Dis_s[c] -= 1
            else:
                return False
        for c in Dis_s:
            if Dis_s[c] != 0:
                return False
        return True
        


# Method 2:
class Solution(object):
    def isAnagram(self, s, t):
        Dis_s = collections.Counter(s)
        Dis_t = collections.Counter(t)
        if Dis_s == Dis_t:
            return True
        else:
            return False

        
