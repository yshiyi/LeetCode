class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        window, need = {}, {}
        left, right, match = 0, 0, 0
        target_len = len(s1)
        window_size = 0
        for c in s1:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
                
        while (right < len(s2)):
            c = s2[right]
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                
                if window[c]==need[c]:
                    match += 1
            right += 1
            
            while (match==len(need)):
                d = s2[left]
                if d in need:
                    if window[d]==need[d]:
                        match -= 1
                    window[d] -= 1
                if right - left == target_len:
                    return True
                left += 1
        return False
        
