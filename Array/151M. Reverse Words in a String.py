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
