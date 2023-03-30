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

'''
Method 2: Two pointers
'''
class Solution(object):
    def reverseWords(self, s):str
        """
        left, right = 0, 0
        words = []
        while right < len(s):
            if s[right]==' ' and right!=left:
                words.append(s[left:right])
                left = right + 1
            elif s[right]==' ' and s[left]== ' ':
                left += 1
            elif right == len(s)-1:
                words.append(s[left:right+1])
            right += 1
        
        ans = ''
        for i in range(len(words)-1, 0, -1):
            ans = ans + words[i] + ' '
            
        return ans + words[0]

'''
Method 3:
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sub_str = ""
        l = []
        i = 0
        while i < len(s):
            if s[i] != " ":
                sub_str += s[i]
                i += 1
                continue
            else:
                l.append(sub_str+" ")
                sub_str = ""
                while i < len(s) and s[i] == " ":
                    i += 1
        if len(sub_str):
            l.append(sub_str+" ")
        res = ""
        while len(l):
            res += l.pop()
        while res[0] == " ":
            res = res[1:]
        while res[-1] == " ":
            res = res[:-1]
        return res
