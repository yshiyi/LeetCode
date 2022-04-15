"""
1249. Minimum Remove to Make Valid Parentheses

Description:
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:
1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""


"""
Method: Use a stack to save all the left bracket.
        When we see a right bracket, if len(stack)!=0 (there are some left brackets in front), we pop the last element in the stack.
        If len(stack)==0 (this is the first right bracket), we must remove it.
        NOTE: we can't pop, we have to set it to empty, i.e., s[i]="".
        At the end, we need to check len(stack) to make sure if there are any redundant left brackest.
"""
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        stack = collections.deque()
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            if s[i]==")":
                if len(stack):
                    stack.pop()
                else:
                    s[i]=""
        while len(stack):
            s.pop(stack.pop())
        res = ""
        for c in s:
            res += c
        return res
        
