"""
20. Valid Parentheses

Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false


Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# Solution:
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<2:
            return False
        p = {')':'(', ']':'[', '}':'{'}
        stack = collections.deque()
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] in p.values():
                stack.append(s[i])
            elif s[i] in p.keys():
                if len(stack)==0 or stack[-1]!=p[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return True if len(stack)==0 else False
