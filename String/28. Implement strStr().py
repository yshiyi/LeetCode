# Method 1: string.find(substr)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0;
        return haystack.find(needle)


'''
Method 2: Sliding Window
          Note: 1. create the dictionaries as defaultdic(int)
                2. check if key exists without updating the value, use if key in Dic
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        Dic_needle, Dic_window = defaultdict(int), defaultdict(int)
        match, r, l = 0, 0, 0
        for c in needle:
            Dic_needle[c] += 1
        
        while r < len(haystack):
            c = haystack[r]
            if c in Dic_needle:
                Dic_window[c] += 1
                if Dic_window[c] == Dic_needle[c]:
                    match += 1
            r += 1
            while match == len(Dic_needle):
                if haystack[l:r] == needle:
                    return l
                cl = haystack[l]
                if cl in Dic_needle:
                    Dic_window[cl] -= 1
                    if Dic_window[cl] < Dic_needle[cl]:
                        match -= 1
                l += 1
        
        return -1
