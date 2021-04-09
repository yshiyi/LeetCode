# Method 1: using two pointers
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        for i, c in enumerate(s):
            if c.isspace():
                newStr = self.reverseStr(s[start:i])
                s = s[0:start] + newStr + s[i:]
                start = i+1
            if i==len(s)-1:
                newStr = self.reverseStr(s[start:i+1])
                s = s[0:start] + newStr
        return s
    
    def reverseStr(seld, s):
        return s[::-1]

      
'''
Method 2: Using string.split() to split a string into a list where each word is a list item
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = [x[::-1] for x in s.split()]
        ans = ""
        for str in sl:
            ans += str + " "
        return ans[:-1]
        
