class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window = {}
        need = {}
        left, right, match = 0, 0, 0
        start, min_len = 0, float('Inf')
        for i in range(len(t)):
            if t[i] not in need:
                need[t[i]] = 1
            else:
                need[t[i]] += 1
                
        while right < len(s):
            if s[right] in need:
                if s[right] not in window:
                    window[s[right]] = 1
                else:
                    window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    match += 1
            while match == len(need):
                if right - left < min_len:
                    start = left
                    min_len = right - left
                if s[left] in need:
                    if window[s[left]]==need[s[left]]:
                        match -= 1
                    window[s[left]] -= 1
                left += 1
            right += 1
            
        if min_len != float('Inf'):
            return s[start:start+min_len+1]
        else:
            return ""
