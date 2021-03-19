class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        window, need = {}, {}
        right, left, match = 0, 0, 0
        target_len = len(p)
        res = []
        for c in p:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
        
        while (right < len(s)):
            c = s[right]
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                if window[c]==need[c]:
                    match += 1
            right += 1
            
            while (match == len(need)):
                d = s[left]
                if d in need:
                    if window[d]==need[d]:
                        match -= 1
                    window[d] -= 1
                if right - left == target_len:
                    res.append(left)
                left += 1
        
        return res
