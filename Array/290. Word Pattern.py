'''
290. Word Pattern
Hash Table, String

Description:
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

Similar Questions:
205. Isomorphic Strings
'''

# Solution:
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        sl = s.split(' ')
        if len(pattern)!=len(sl):
            return False
        dic_p = defaultdict(int)
        dic_s = defaultdict(int)
        for i in range(len(pattern)):
            c, w = pattern[i], sl[i]
            if c not in dic_p and w not in dic_s:
                dic_p[c] = i
                dic_s[w] = i
            elif c in dic_p and w in dic_s:
                if dic_p[c] != dic_s[w]:
                    return False
                else:
                    dic_p[c] = i
                    dic_s[w] = i
            else:
                return False
        return True
        
